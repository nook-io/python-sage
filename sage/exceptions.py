import six


class OpenApiException(Exception):
    pass


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None, key_type=None):
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None):
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):
    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        error_message = "({0})\nReason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)
        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)
        return error_message


def render_path(path_to_item):
    result = ""
    for pth in path_to_item:
        if isinstance(pth, six.integer_types):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result


class OAuth2Error(OpenApiException):
    pass


class AccessTokenExpiredError(OAuth2Error):
    pass


class OAuth2TokenGetterError(OAuth2Error):
    pass


class OAuth2TokenSaverError(OAuth2Error):
    pass
