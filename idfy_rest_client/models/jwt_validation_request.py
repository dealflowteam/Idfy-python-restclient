# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.jwt_validation_request

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class JwtValidationRequest(object):

    """Implementation of the 'JwtValidationRequest' model.

    Jwt validation request

    Attributes:
        jwt (string): The JWT to be validated as an string

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "jwt":'jwt'
    }

    def __init__(self,
                 jwt=None,
                 additional_properties = {}):
        """Constructor for the JwtValidationRequest class"""

        # Initialize members of the class
        self.jwt = jwt

        # Add additional model properties to the instance
        self.additional_properties = additional_properties


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        jwt = dictionary.get('jwt')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(jwt,
                   dictionary)

