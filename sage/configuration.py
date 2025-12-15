from __future__ import absolute_import
import copy
import logging
import multiprocessing
import sys
import six
import urllib3
from six.moves import http_client as httplib


class Configuration(object):
    _default = None

    def __init__(
        self,
        host="https://api.accounting.sage.com/v3.1",
        api_key=None,
        api_key_prefix=None,
        username=None,
        password=None,
        discard_unknown_keys=False,
        oauth2_token=None,
    ):
        self.host = host
        self.temp_folder_path = None
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        self.username = username
        self.password = password
        self.oauth2_token = oauth2_token
        self.discard_unknown_keys = discard_unknown_keys
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("sage")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = "%(asctime)s %(levelname)s %(message)s"
        self.logger_stream_handler = None
        self.logger_file_handler = None
        self.logger_file = None
        self.debug = False
        self.verify_ssl = True
        self.ssl_ca_cert = None
        self.cert_file = None
        self.key_file = None
        self.assert_hostname = None
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        self.proxy = None
        self.proxy_headers = None
        self.safe_chars_for_path_param = ""
        self.retries = None
        self.client_side_validation = True

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ("logger", "logger_file_handler"):
                setattr(result, k, copy.deepcopy(v, memo))
        result.logger = copy.copy(self.logger)
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default):
        cls._default = copy.deepcopy(default)

    @classmethod
    def get_default_copy(cls):
        if cls._default is not None:
            return copy.deepcopy(cls._default)
        return Configuration()

    @property
    def logger_file(self):
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        self.__logger_file = value
        if self.__logger_file:
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value):
        self.__debug = value
        if self.__debug:
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            httplib.HTTPConnection.debuglevel = 1
        else:
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier):
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(basic_auth=username + ":" + password).get(
            "authorization"
        )

    def auth_settings(self, auth_type):
        auth_type = str(auth_type).lower()
        if auth_type == "oauth2":
            return self.oauth2_token.get_auth_settings()

    def to_debug_report(self):
        return (
            "Python SDK Debug Report:\n"
            "OS: {env}\n"
            "Python Version: {pyversion}\n"
            "Version of the API: 3.1\n"
            "SDK Package Version: 1.0.0".format(env=sys.platform, pyversion=sys.version)
        )

    def get_host_settings(self):
        return [
            {
                "url": "https://api.accounting.sage.com/v3.1",
                "description": "No description provided",
            }
        ]

    def get_host_from_settings(self, index, variables=None):
        variables = {} if variables is None else variables
        servers = self.get_host_settings()
        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers))
            )
        url = server["url"]
        for variable_name, variable in server["variables"].items():
            used_value = variables.get(variable_name, variable["default_value"])
            if "enum_values" in variable and used_value not in variable["enum_values"]:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name], variable["enum_values"]
                    )
                )
            url = url.replace("{" + variable_name + "}", used_value)
        return url
