# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.lei_extension

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.lei_normalizations

class LeiExtension(object):

    """Implementation of the 'LeiExtension' model.

    TODO: type model description here.

    Attributes:
        normalizations (LeiNormalizations): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "normalizations":'Normalizations'
    }

    def __init__(self,
                 normalizations=None,
                 additional_properties = {}):
        """Constructor for the LeiExtension class"""

        # Initialize members of the class
        self.normalizations = normalizations

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
        normalizations = idfy_rest_client.models.lei_normalizations.LeiNormalizations.from_dictionary(dictionary.get('Normalizations')) if dictionary.get('Normalizations') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(normalizations,
                   dictionary)


