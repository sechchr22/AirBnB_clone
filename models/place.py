#!/usr/bin/python3
"""place Module"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

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

        dictionary["city_id"] = self.city_id
        dictionary["user_id"] = self.user_id
        dictionary["name"] = self.name
        dictionary["description"] = self.description
        dictionary["number_rooms"] = self.number_rooms
        dictionary["number_bathrooms"] = self.number_bathrooms
        dictionary["max_guest"] = self.max_guest
        dictionary["price_by_night"] = self.price_by_night
        dictionary["latitude"] = self.latitude
        dictionary["longitude"] = self.longitude
        dictionary["amenity_ids"] = self.amenity_ids
        return dictionary
