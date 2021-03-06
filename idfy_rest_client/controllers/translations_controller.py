# -*- coding: utf-8 -*-

"""
    idfy_rest_client.controllers.translations_controller

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.translation_dto import TranslationDTO

class TranslationsController(BaseController):

    """A Controller to access Endpoints in the idfy_rest_client API."""


    def list_translations(self,
                          language_set_id,
                          language=None,
                          format=None):
        """Does a GET request to /text/language-sets/{languageSetId}/translations.

        Returns a list of all your translations for the given language set.

        Args:
            language_set_id (int): TODO: type description here. Example: 
            language (string, optional): TODO: type description here. Example:
                            format (Format, optional): TODO: type description here. Example: 

        Returns:
            list of TranslationDTO: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(language_set_id=language_set_id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/text/language-sets/{languageSetId}/translations'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'languageSetId': language_set_id
        })
        _query_parameters = {
            'language': language,
            'format': format
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, TranslationDTO.from_dictionary)

    def update_translation(self,
                           language_set_id,
                           id,
                           translation_update=None):
        """Does a PATCH request to /text/language-sets/{languageSetId}/translations/{id}.

        Updates the specified translation with the parameters passed.

        Args:
            language_set_id (int): TODO: type description here. Example: 
            id (int): TODO: type description here. Example: 
            translation_update (TranslationUpdateDTO, optional): TODO: type
                description here. Example: 

        Returns:
            void: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(language_set_id=language_set_id,
                                 id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/text/language-sets/{languageSetId}/translations/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'languageSetId': language_set_id,
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(translation_update))
        _context = self.execute_request(_request)
        self.validate_response(_context)

    def retrieve_translation(self,
                             language_set_id,
                             id):
        """Does a GET request to /text/language-sets/{languageSetId}/translations/{id}.

        Retrieves the details of a single translation.

        Args:
            language_set_id (int): TODO: type description here. Example: 
            id (int): TODO: type description here. Example: 

        Returns:
            TranslationDTO: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(language_set_id=language_set_id,
                                 id=id)

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/text/language-sets/{languageSetId}/translations/{id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'languageSetId': language_set_id,
            'id': id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, TranslationDTO.from_dictionary)
