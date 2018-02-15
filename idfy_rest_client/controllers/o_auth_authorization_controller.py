# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.o_auth_authorization_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.o_auth_token import OAuthToken
from ..exceptions.o_auth_provider_exception import OAuthProviderException

class OAuthAuthorizationController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def request_token(self,
                      authorization,
                      scope=None,
                      _optional_form_parameters=None):
        """Does a POST request to /oauth/connect/token.

        Create a new OAuth 2 token.

        Args:
            authorization (string): Authorization header in Basic auth format
            scope (string, optional): Requested scopes as a space-delimited
                list.
            _optional_form_parameters (Array, optional): Additional optional
                form parameters are supported by this endpoint

        Returns:
            OAuthToken: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(authorization=authorization)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/oauth/connect/token'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Authorization': authorization
        }

        # Prepare form parameters
        _form_parameters = {
            'grant_type': 'client_credentials',
            'scope': scope
        }
        if _form_parameters != None and _optional_form_parameters != None:
            _form_parameters.update(APIHelper.form_encode_parameters(_optional_form_parameters,
                Configuration.array_serialization))
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise OAuthProviderException('OAuth 2 provider returned an error.', _context)
        elif _context.response.status_code == 401:
            raise OAuthProviderException('OAuth 2 provider says client authentication failed.', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OAuthToken.from_dictionary)
