#!/usr/bin/python3
"""
The conole v: 0.0.1
contains entry point of cmd
"""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {"BaseModel"}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    do_EOF = do_quit

    def emptyline(self):
        """empty line nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
