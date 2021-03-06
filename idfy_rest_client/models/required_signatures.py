# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.required_signatures

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""
import idfy_rest_client.models.signature

class RequiredSignatures(object):

    """Implementation of the 'RequiredSignatures' model.

    TODO: type model description here.

    Attributes:
        list (list of Signature): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "list":'List'
    }

    def __init__(self,
                 list=None,
                 additional_properties = {}):
        """Constructor for the RequiredSignatures class"""

        # Initialize members of the class
        self.list = list

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
        list = None
        if dictionary.get('List') != None:
            list = list()
            for structure in dictionary.get('List'):
                list.append(idfy_rest_client.models.signature.Signature.from_dictionary(structure))

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(list,
                   dictionary)


