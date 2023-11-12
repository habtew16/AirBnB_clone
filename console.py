#!/usr/bin/python3
"""entry class for
airbnb console cmd
"""
import cmd
import shlex
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {"BaseModel", "Amenity", "City", "Place", "User", "Review", "Review"}

    def do_quit(self, arg):
        return True

    do_EOF = do_quit

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not len(arg):
            print("** class name missing **")
            return
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        newObject = eval(arg)()
        print(newObject.id)
        newObject.save()

    def do_show(self, arg):
        """shows an object"""
        if not len(arg):
            print("** class name missing **")
            return
        strings = split(arg)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[keyValue])

    def do_destroy(self, arg):
        """deletes an object"""
        if not len(arg):
            print("** class name missing **")
            return
        strings = split(arg)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[keyValue]
        storage.save()

    def do_all(self, arg):
        """prints all"""
        if not len(arg):
            print([obj for obj in storage.all().values()])
            return
        strings = split(arg)
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([obj for obj in storage.all().values()
               if strings[0] == type(obj).__name__])

    def do_update(self, arg):
        """updates an object"""
        if not len(arg):
            print("** class name missing **")
            return
        strings = split(arg)
        for string in strings:
            if string.startswith('"') and string.endswith('"'):
                string = string[1:-1]
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(strings) == 1:
            print("** instance id missing **")
            return
        keyValue = strings[0] + '.' + strings[1]
        if keyValue not in storage.all().keys():
            print("** no instance found **")
            return
        if len(strings) == 2:
            print("** attribute name missing **")
            return
        if len(strings) == 3:
            print("** value missing **")
            return
        try:
            setattr(storage.all()[keyValue], strings[2], eval(strings[3]))
        except Exception:
            setattr(storage.all()[keyValue], strings[2], strings[3])

    def stripper(self, st):
        """strips that line"""
        newstring = st[st.find("(")+1:st.rfind(")")]
        newstring = shlex.shlex(newstring, posix=True)
        newstring.whitespace += ','
        newstring.whitespace_split = True
        return list(newstring)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
