#!/usr/bin/python3
"""
Module Console
"""
import cmd
import shlex
import sys
import re
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# Constants for error messages
ERROR_CLASS_MISSING = "** class name missing **"
ERROR_CLASS_DOES_NOT_EXIST = "** class doesn't exist **"
ERROR_ID_MISSING = "** instance id missing **"
ERROR_NO_INSTANCE_FOUND = "** no instance found **"
ERROR_ATTRIBUTE_NAME_MISSING = "** attribute name missing **"
ERROR_VALUE_MISSING = "** value missing **"


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in shlex.split(arg)]
        else:
            lexer = shlex.split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = shlex.split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '

    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
            'State': State, 'Place': Place, 'Review': Review,
            'User': User, 'City': City}

    def do_quit(self, argument):
        """ Defines quit option"""
        return True

    def do_EOF(self, argument):
        """ Defines EOF option"""
        print()
        return True

    def emptyline(self):
        """ Defines Empty option"""
        pass

    def do_create(self, argument):
        """Creates an instance of BaseModel"""
        if argument:
            if argument in self.classes:
                # instance = models.base_model.BaseModel()
                get_class = getattr(sys.modules[__name__], argument)
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, argument):
        """string representation based on the class name and id"""
        tokens = shlex.split(argument)
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            # Key has format <className>.id
            keyU = tokens[0] + '.' + str(tokens[1])
            if keyU in dic:
                print(dic[keyU])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, argument):
        """Deletes an instance based on the class name and id"""
        tokensD = shlex.split(argument)
        if len(tokensD) == 0:
            print("** class name missing **")
            return
        elif len(tokensD) == 1:
            print("** instance id missing **")
            return
        elif tokensD[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            dic = models.storage.all()
            # Key has format <className>.id
            key = tokensD[0] + '.' + tokensD[1]
            if key in dic:
                del dic[key]
                models.storage.save()
            else:
                print("** no instance found **")


    def do_all(self, argument):
        """all string representation of all instances"""
        tokensA = shlex.split(argument)
        listI = []
        dic = models.storage.all()
        # show all if no class is passed
        if len(tokensA) == 0:
            for key in dic:
                representation_Class = str(dic[key])
                listI.append(representation_Class)
            # if listI:
            print(listI)
            return

        if tokensA[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            # Representation for a specific class
            representation_Class = ""
            for key in dic:
                className = key.split('.')
                if className[0] == tokensA[0]:
                    # This form doesn't work
                    # listI.append(dic[key])
                    representation_Class = str(dic[key])
                    listI.append(representation_Class)
            # if listI:
            print(listI)

    def do_update(self, arg):
        """Update an instance based on its ID."""
        args = parse(arg)
        obj_dict = models.storage.all()

        if len(args) < 2:
            print(ERROR_CLASS_MISSING)
            return
        if args[0] not in self.classes:
            print(ERROR_CLASS_DOES_NOT_EXIST)
            return
        if len(args) < 3:
            print(ERROR_ID_MISSING)
            return
        if f"{args[0]}.{args[1]}" not in obj_dict:
            print(ERROR_NO_INSTANCE_FOUND)
            return

        obj = obj_dict[f"{args[0]}.{args[1]}"]

        if len(args) == 3 and type(args[2]) == dict:
            # Updating with a dictionary
            updates = args[2]
            for key, value in updates.items():
                if key in obj.__dict__:
                    setattr(obj, key, value)
        elif len(args) == 4:
            # Updating with attribute name and value
            attribute_name = args[2]
            attribute_value = args[3]
            if attribute_name in obj.__dict__:
                setattr(obj, attribute_name, attribute_value)
            else:
                print(f"** no attribute named {attribute_name} **")
        else:
            print(ERROR_VALUE_MISSING)

        models.storage.save()


    def update_dict(self, classname, uid, s_dict):
        """
        Helper method for update() with a dictionary.

        Args:
            classname (str): Class name.
            uid (str): Unique ID.
            s_dict (str): Dictionary string.

        Returns:
            None
        """
        s = s_dict.replace("'", '"')
        d = json.loads(s)

        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


    def do_count(self, argument):
        """  retrieve the number of instances of a class """
        tokensA = shlex.split(argument)
        dic = models.storage.all()
        num_instances = 0
        if tokensA[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in dic:
                className = key.split('.')
                if className[0] == tokensA[0]:
                    num_instances += 1

            print(num_instances)

    def precmd(self, argument):
        """ executed just before the command line line is interpreted """
        args = argument.split('.', 1)
        if len(args) == 2:
            _class = args[0]
            args = args[1].split('(', 1)
            command = args[0]
            if len(args) == 2:
                args = args[1].split(')', 1)
                if len(args) == 2:
                    _id = args[0]
                    other_arguments = args[1]
            line = command + " " + _class + " " + _id + " " + other_arguments
            return line
        else:
            return argument


if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()
