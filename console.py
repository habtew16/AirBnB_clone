#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {"BaseModel"}

    def do_quit(self, arg):
        """quit command"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """empty line nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
