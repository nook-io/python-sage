import json
import time
from sage.exceptions import AccessTokenExpiredError


class TokenApi:
    client_credentials_token_url = "https://oauth.accounting.sage.com/token"
    refresh_token_url = "https://oauth.accounting.sage.com/token"
    revoke_token_url = "https://oauth.accounting.sage.com/revoke"

    def __init__(self, api_client, client_id, client_secret):
        self.api_client = api_client
        self.client_id = client_id
        self.client_secret = client_secret

    def refresh_token(self, refresh_token):
        post_data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = self.api_client.call_api(
            self.refresh_token_url,
            "POST",
            header_params={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            post_params=post_data,
            auth_settings=None,
            _preload_content=False,
        )
        if response.status != 200:
            raise Exception(
                "refresh token status {} {} {!r}".format(
                    response.status, response.data, response.headers
                )
            )
        return self.parse_token_response(response)

    def revoke_token(self, refresh_token):
        post_data = {
            "token": refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = self.api_client.call_api(
            self.revoke_token_url,
            "POST",
            header_params={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            post_params=post_data,
            auth_settings=None,
            _preload_content=False,
        )
        if response.status != 200:
            raise Exception(
                "refresh token status {} {} {!r}".format(
                    response.status, response.data, response.headers
                )
            )
        return response.status

    def get_client_credentials_token(self, app_store_billing):
        post_data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }
        if app_store_billing:
            post_data["scope"] = "marketplace.billing"
        response = self.api_client.call_api(
            self.client_credentials_token_url,
            "POST",
            header_params={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            post_params=post_data,
            auth_settings=None,
            _preload_content=False,
        )
        if response.status != 200:
            raise Exception(
                "refresh token status {} {} {!r}".format(
                    response.status, response.data, response.headers
                )
            )
        return self.parse_token_response(response)

    def parse_token_response(self, response):
        data = response.data.decode("utf-8")
        return json.loads(data)


class OAuth2Token:
    EXPIRATION_BUFFER_DEFAULT = 60

    def __init__(
        self,
        client_id=None,
        client_secret=None,
        expiration_buffer=EXPIRATION_BUFFER_DEFAULT,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.expiration_buffer = expiration_buffer
        self.token_type = "Bearer"
        self.access_token = self.id_token = self.refresh_token = self.scope = None
        self.expires_at = self.expires_in = None

    def get_auth_settings(self):
        return self.create_auth_settings

    def create_auth_settings(self, api_client):
        self.update_token(**api_client.get_oauth2_token())
        access_token = self.get_valid_access_token(api_client)
        return {
            "type": "oauth2",
            "in": "header",
            "key": "Authorization",
            "value": "{type} {token}".format(type=self.token_type, token=access_token),
        }

    def is_access_token_valid(self, at_time=None):
        at_time = at_time or time.time() + self.expiration_buffer
        if self.expires_at is None:
            return True
        return self.expires_at > at_time

    def get_valid_access_token(self, api_client=None, at_time=None):
        if not self.is_access_token_valid(at_time):
            if not self.refresh_access_token(api_client):
                raise AccessTokenExpiredError("Access Token has expired")
        return self.access_token

    def can_refresh_access_token(self):
        return (
            self.refresh_token
            and isinstance(self.scope, (list, tuple))
            and self.client_id
            and self.client_secret
        )

    def refresh_access_token(self, api_client):
        if not self.can_refresh_access_token():
            return False
        token_api = TokenApi(api_client, self.client_id, self.client_secret)
        new_token = self.fetch_access_token(token_api)
        self.update_token(**new_token)
        api_client.set_oauth2_token(new_token)
        return True

    def get_client_credentials_access_token(self, api_client, app_store_billing):
        token_api = TokenApi(api_client, self.client_id, self.client_secret)
        new_token = token_api.get_client_credentials_token(app_store_billing)
        self.update_token(**new_token)
        api_client.set_oauth2_token(new_token)
        return True

    def revoke_access_token(self, api_client):
        if not self.can_refresh_access_token():
            return False
        token_api = TokenApi(api_client, self.client_id, self.client_secret)
        token_api.revoke_token(self.refresh_token)
        new_token = {
            "access_token": None,
            "expires_in": None,
            "token_type": "Bearer",
            "refresh_token": None,
            "refresh_token_expires_in": None,
            "scope": None,
            "requested_by_id": None,
        }
        self.update_token(**new_token)
        api_client.set_oauth2_token(new_token)
        return True

    def update_token(
        self,
        access_token,
        expires_in,
        token_type,
        refresh_token,
        refresh_token_expires_in,
        scope,
        requested_by_id,
        expires_at=None,
    ):
        self.access_token = access_token
        self.expires_at = (
            expires_at
            if expires_at
            else (time.time() + expires_in if expires_in else expires_in)
        )
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.scope = scope
        self.token_type = token_type
        self.token_type = "Bearer" if self.token_type == "bearer" else self.token_type

    def fetch_access_token(self, token_api, token_valid_from=None):
        token = self.call_refresh_token_api(token_api)
        token_valid_from = token_valid_from or time.time()
        new_scope = token.get("scope")
        if new_scope:
            new_scope = str(new_scope).split()
            token["scope"] = new_scope
        expires_in = token.get("expires_in")
        if expires_in and "expires_at" not in token:
            token["expires_at"] = token_valid_from + expires_in
        return token

    def call_refresh_token_api(self, token_api):
        return token_api.refresh_token(self.refresh_token)
