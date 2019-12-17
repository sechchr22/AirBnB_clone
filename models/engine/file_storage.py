#!/usr/bin/python3
"""
File Storage Module
"""


import os
import json


class FileStorage:
    '''FileStorage Class'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Show all instances'''
        return FileStorage.__objects

    def new(self, obj):
        '''Create new instance'''
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def reload(self):
        '''Recover all the instance created'''

        if not os.path.isfile(FileStorage.__file_path):
            return FileStorage.__objects

        with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
            strjson = f.read()

            jobjects = json.loads(strjson)

            from models.base_model import BaseModel

            from models.state import State

            from models.entitys import entitys

            from models.city import City

            from models.amenity import Amenity

            from models.place import Place

            from models.review import Review

            for key, obj_json in jobjects.items():
                clase = key.split(".")[0]
                FileStorage.__objects[key] = entitys[clase](**obj_json)

        return FileStorage.__objects

    def save(self):
        '''Save instance in json format into a file'''

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            f.write("{")
            i = 0
            for key, value in FileStorage.__objects.items():
                json_obj = json.dumps(value.to_dict())
                if i == 0:
                    f.write(
                        "\"" +
                        value.__class__.__name__ +
                        "." +
                        value.id +
                        "\"" +
                        ":" +
                        json_obj)
                else:
                    f.write(
                        ",\"" +
                        value.__class__.__name__ +
                        "." +
                        value.id +
                        "\"" +
                        ":" +
                        json_obj)
                i += 1
            f.write("}")
