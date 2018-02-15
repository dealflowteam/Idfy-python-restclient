# -*- coding: utf-8 -*-

"""
   idfy_rest_client.http.auth.oauth2

   This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""

import base64
import calendar
from datetime import datetime
from ...controllers.o_auth_authorization_controller import OAuthAuthorizationController
from ...configuration import Configuration

class OAuth2:

    @classmethod
    def apply(cls, http_request):
        """ Add OAuth2 authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication header will be added.

        """
        cls.check_auth()
        token = Configuration.o_auth_token.access_token
        http_request.headers['Authorization'] = "Bearer {}".format(token)

    @staticmethod
    def update_token(token):
        """ Sets the token object of the configuation class.

        Args:
            token (OAuthToken): The OAuth token.

        """
        if token.expires_in:
            utc_now = calendar.timegm(datetime.now().utctimetuple())
            token.expiry = (utc_now + int(token.expires_in))
        Configuration.o_auth_token = token
        if Configuration.o_auth_callback:
            Configuration.o_auth_callback(token)

    @staticmethod
    def build_basic_auth_header():
        """ Builds the basic auth header for endpoints in the
            OAuth Authorization Controller.

        Returns:
            str: The value of the Authentication header.

        """
        username = Configuration.o_auth_client_id
        password = Configuration.o_auth_client_secret
        joined = "{}:{}".format(username, password)
        encoded = base64.b64encode(str.encode(joined)).decode('iso-8859-1')
        return "Basic {}".format(encoded)

    @classmethod
    def check_auth(cls):
        """ Checks if OAuth token is valid."""
        if not Configuration.o_auth_token:
            cls.authorize()

    @classmethod
    def authorize(cls, scope=None, additional_params=None):
        """ Authorizes the client.

        Args:
            scope (str | list of str): The scope required for the access token.
            additional_params (dict):  Any additional form parameters.

        Returns:
            OAuthToken: The OAuth token.

        """
        token = OAuthAuthorizationController().request_token(
            cls.build_basic_auth_header(),
            ' '.join(scope) if (isinstance(scope, list)) else scope,
            additional_params
        )
        cls.update_token(token)
        return token
