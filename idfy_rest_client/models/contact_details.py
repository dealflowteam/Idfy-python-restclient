# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.contact_details

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class ContactDetails(object):

    """Implementation of the 'ContactDetails' model.

    TODO: type model description here.

    Attributes:
        email (string): TODO: type description here.
        name (string): TODO: type description here.
        phone (string): TODO: type description here.
        url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email":'email',
        "name":'name',
        "phone":'phone',
        "url":'url'
    }

    def __init__(self,
                 email=None,
                 name=None,
                 phone=None,
                 url=None,
                 additional_properties = {}):
        """Constructor for the ContactDetails class"""

        # Initialize members of the class
        self.email = email
        self.name = name
        self.phone = phone
        self.url = url

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
        email = dictionary.get('email')
        name = dictionary.get('name')
        phone = dictionary.get('phone')
        url = dictionary.get('url')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(email,
                   name,
                   phone,
                   url,
                   dictionary)


