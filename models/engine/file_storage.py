#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        fileobj_dict = FileStorage.__objects
        cls_obj = {}
        if cls is None:
            return fileobj_dict
        for key, value in fileobj_dict.items():
            if cls.__name__ in key:
                cls_obj[key] = value
        if '_sa_instance_state' in cls_obj.keys():
            cls_obj.pop('_sa_instance_state')
        return cls_obj

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
                    if '_sa_instance_state' in FileStorage.__objects.keys():
                        FileStorage.__objects.pop('_sa_instance_state')
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ public instance method: def delete(self, obj=None):
        to delete obj from __objects if it’s inside"""
        if obj is None:
            return
        obj_dict = obj.to_dict()
        all_dict = self.all()
        key = "{}.{}".format(obj_dict['__class__'], obj_dict['id'])
        if key in all_dict:
            all_dict.pop(key)

    def close(self):
        """A method for deserializing the JSON file to objects"""
        self.reload()
