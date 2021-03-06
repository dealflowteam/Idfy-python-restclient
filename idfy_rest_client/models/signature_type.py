# -*- coding: utf-8 -*-

"""
    idfy_rest_client.models.signature_type

    This file was automatically generated for Idfy by APIMATIC v2.0 ( https://apimatic.io )
"""


class SignatureType(object):

    """Implementation of the 'SignatureType' model.

    TODO: type model description here.

    Attributes:
        mechanism (Mechanism): TODO: type description here.
        signature_methods (list of SignatureMethod): Define which signature
            methods the signer are allowed to sign the document with, if empty
            all available methods for the account will be displayed to the
            user
        on_eaccept_use_hand_written_signature (bool): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mechanism":'mechanism',
        "signature_methods":'signatureMethods',
        "on_eaccept_use_hand_written_signature":'onEacceptUseHandWrittenSignature'
    }

    def __init__(self,
                 mechanism=None,
                 signature_methods=None,
                 on_eaccept_use_hand_written_signature=None,
                 additional_properties = {}):
        """Constructor for the SignatureType class"""

        # Initialize members of the class
        self.mechanism = mechanism
        self.signature_methods = signature_methods
        self.on_eaccept_use_hand_written_signature = on_eaccept_use_hand_written_signature

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
        mechanism = dictionary.get('mechanism')
        signature_methods = dictionary.get('signatureMethods')
        on_eaccept_use_hand_written_signature = dictionary.get('onEacceptUseHandWrittenSignature')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(mechanism,
                   signature_methods,
                   on_eaccept_use_hand_written_signature,
                   dictionary)


