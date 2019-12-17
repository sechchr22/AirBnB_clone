#!/usr/bin/python3
"""BaseModel Module"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init method

        Args:
            Recieve keyworded and non keyworded args
        """
        if kwargs is not None and len(kwargs) > 0:
            super().__init__(**kwargs)

        elif args is not None and len(args) > 0:
            print('im using args')

        else:
            super().__init__()

    def to_dict(self):
        """
        to_dict method

        Return: dictionary containing all keys/values
        of __dict__ of an instance
        """
        dictionary = super().to_dict()

        dictionary["name"] = self.name
        return dictionary
