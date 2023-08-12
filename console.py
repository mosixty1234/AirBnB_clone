#!/usr/bin/python3
#!/usr/bin/env python3
"""Defines the HBnB console."""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter

    Attributes:
        prompt (str): The command prompt
    """
    prompt = "(hbnb) "
    __class_dict = {
        "BaseModel": BaseModel
    }

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """Does nothing when receiving an empty line"""
        pass

    def do_create(self, arg):
        """
        Usage: create <class>
        Create a new class instance and print its id.
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in HBNBCommand.__class_dict:
            print("** class doesn't exist **")
            return

        new_obj = HBNBCommand.__class_dict[class_name]()
        print(new_obj.id)
        storage.save()

    def do_show(self, arg):
        """
        Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        obj_dict = storage.all()

        class_name = args[0]
        if class_name not in HBNBCommand.__class_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        obj_dict = storage.all()

        class_name = args[0]
        if class_name not in HBNBCommand.__class_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in obj_dict:
            del obj_dict[key]
            storage.save
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Displays string representations of all instances of a given class.
        If no class is specified, displays all instantiated object
        """
        obj_dict = storage.all()
        if not arg:
            print([str(value) for value in obj_dict.values()])
            return

        class_name = arg.split()[0]
        if class_name not in HBNBCommand.__class_dict:
            print("** class doesn't exist **")
            return

        result = [
            str(value)
            for key, value in obj_dict.items()
            if class_name in key
        ]
        print(result)

    def do_update(self, arg):
        """Updates a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        obj_dict = storage.all()

        class_name = args[0]
        if class_name not in HBNBCommand.__class_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]

        obj = storage.all()[key]
        setattr(obj, attr_name, attr_value)
        storage.save


if __name__ == "__main__":
    HBNBCommand().cmdloop()
