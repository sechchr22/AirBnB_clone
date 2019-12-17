#!/usr/bin/python3

"""
User class module
"""

from models.base_model import BaseModel


class User(BaseModel):
    '''User class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        ''' init method of User'''

        if kwargs is not None and len(kwargs) > 0:
            super().__init__(**kwargs)

        elif args is not None and len(args) > 0:
            print('im using args')

        else:
            super().__init__()

    def to_dict(self):
        '''to_dict method of User'''

        dictionary = super().to_dict()
        dictionary['__class__'] = self.__class__.__name__

        return dictionary
