#!/usr/bin/python3

"""
Console Module to handle Objects
"""

from cmd import Cmd
from models import storage
from models.entitys import entitys
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(Cmd):
    '''HBNBCommand Console class'''

    prompt = "(hbnb)"

    def do_quit(self, inp):
        '''Quit command to exit the program'''
        return True

    def do_show(self, inp):
        """
        Prints the string representation of an
        instance based on the class name and id
        """

        list_param = inp.split()

        if len(list_param) is 0:
            print('** class name missing **')
            return

        if list_param[0] not in entitys:
            print('** class doesn\'t exist **')
            return

        if len(list_param) < 2:
            print('** instance id missing **')
            return

        obj_key = list_param[0] + "." + list_param[1]
        all_objs = storage.all()

        if obj_key not in all_objs:
            print("** no instance found **")
            return

        print(all_objs[obj_key])
        return

    do_EOF = do_quit

    def do_all(self, inp):
        '''Prints all string representation of all instances'''
        list_param = inp.split()

        if inp == '' or list_param[0] not in entitys:
            print('** class doesn\'t exist **')
            return

        all_objs_list = []
        all_objs = storage.all()

        for key in all_objs.keys():

            class_names = key.split('.')

            if class_names[0] == list_param[0]:
                all_objs_list.append(all_objs[key].__str__())

        print(all_objs_list)
        return

    def do_create(self, inp):
        '''Creates a new instance of BaseModel'''
        if inp == '':
            print('** class name missing **')
            return
        if inp not in entitys:
            print("** class doesn't exist **")
            return
        base_model = globals()[inp]()

        base_model.save()
        print(base_model.id)

    def do_destroy(self, inp):
        '''Deletes an instance based on the class name and id'''
        if inp == '':
            print('** class name missing **')
            return
        list_param = inp.split()
        if list_param[0] not in entitys:
            print("** class doesn't exist **")
            return
        if len(list_param) < 2:
            print("** instance id missing **")
            return

        key_object = list_param[0] + "." + list_param[1]
        all_objects = storage.all()
        if key_object not in all_objects:
            print("** no instance found **")
            return
        del all_objects[key_object]
        storage.save()

    def do_update(self, inp):
        '''Update the instance'''

        list_param = inp.split()

        if inp == '':
            print('** class name missing **')
            return

        if list_param[0] not in entitys:
            print("** class doesn't exist **")
            return

        if len(list_param) < 2:
            print("** instance id missing **")
            return

        if len(list_param) < 3:
            print("** attribute name missing **")
            return

        if len(list_param) < 4:
            print("** value missing **")
            return

        all_objs = storage.all()
        key_obj = list_param[0] + "." + list_param[1]
        obj = all_objs[key_obj]

        if key_obj not in all_objs:
            print("** no instance found **")
            return

        setattr(obj, list_param[2], list_param[3])
        storage.save()

    def emptyline(self):
        return
    
    def do_count(self, inp):
        all_objs = storage.all()
        count_objs = 0
        for key in all_objs.keys():
            if inp in key:
                count_objs += 1
        print(count_objs)


    cmds = {"all()": do_all, "count()": do_count, "show()": do_show}
    def default(self, inp):
        args = inp.split(".")

        if len(args) > 1:
            if args[1].startswith("show"):
                replace = args[1][args[1].find('(') + 1 : args[1].find(')')]
                args[1] = args[1].replace(replace, "") 
                replace = replace.replace("\"", "")
                HBNBCommand.cmds[args[1]](self, args[0] + " " + replace)
                return
            if args[1] in HBNBCommand.cmds:

                HBNBCommand.cmds[args[1]](self, str(args[0]))
            else:
                print("*** Unknown syntax:" + inp)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
