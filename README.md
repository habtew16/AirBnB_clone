An AirBnB clone.

0x00. AirBnB clone - The console
0x00.Table of Contents
0x01 Summary
0x02 Environment
0x03 Installation
0x04 Testing
0x05 Usage
0x06 Authors
0x01 Summary
This is a team project to build a minimum viable product for AirBnB.

The console serves as a command interpreter that facilitates the interaction with objects, providing an abstraction layer between these objects and their underlying storage mechanisms.

For a background review of the project visit: Wiki.

The console is expected to perform the following:

create a new object
retrive an object from a file
perform operations on objects
destroy an object
Storage
All the classes are handled by the Storage engine in the FileStorage Class.

0x02 Environment
Suite CRM python Suite CRM git distributed version control system GitHub

Proper Documentation and Coding Style Guidelines:
pycodestyle (version 2.7.*)
PEP8
All the development and testing was done on the Ubuntu 20.04 LTS operating system with the Python 3.8.3. The editor used was VIM 8.1.2269 and for version control, Git 2.25.1 and Github were used.

0x03 Installation
Clone project repository as:

git clone https://github.com/habtew16/AirBnB_clone.git
Once the repository is cloned locate the "console.py" file and run it as follows:

/AirBnB_clone$ ./console.py When this command is run, the following prompt should appear: (hbnb) This prompt designates you are in the "HBnB" console.

Execution
In interactive mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
in Non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
0x04 Testing
Find relevant tests for this project in the tests folder.

Documentation
Modules:
python3 -c 'print(__import__("my_module").__doc__)'
Classes:
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
Functions (inside and outside a class):
python3 -c 'print(__import__("my_module").my_function.__doc__)'
and

python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
Python Unit Tests
unittest module
File extension .py
Files and folders star with test_
Organization:for models/base.py, unit tests in: tests/test_models/test_base.py
Execution command: python3 -m unittest discover tests
or: python3 -m unittest tests/test_models/test_base.py
run test in interactive mode
echo "python3 -m unittest discover tests" | bash
run test in non-interactive mode
To run the tests in non-interactive mode, and discover all the test, you can use the command:

python3 -m unittest discover tests
0x05 Usage
Start the console in interactive mode:
$ ./console.py
(hbnb)
Use help to see the available commands:
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
Quit the console:
(hbnb) quit
$
Commands, its Usage & Descriptions
Some basic commands recognized by the interpreter are:

Command	Description
quit or EOF	Exits the program
Usage	By itself
-----	-----
help	Provides a text describing how to use a command.
Usage	By itself --or-- help <command>
-----	-----
create	Creates a new instance of a valid Class, saves it (to the JSON file), and prints the id. Valid classes are BaseModel, User, State, City, Place, Amenity, and Review.
Usage	create <class name>
-----	-----
show	Prints the string representation of an instance based on the class name and id
Usage	show <class name> <id> --or-- <class name>.show(<id>)
-----	-----
destroy	Deletes an instance based on the class name and id (saves the change into a JSON file).
Usage	destroy <class name> <id> --or-- .destroy()
-----	-----
all	Prints all string representation of all instances based or not on the class name.
Usage	By itself or all <class name> --or-- <class name>.all()
-----	-----
-----	-----
Update updates an instance based on the class name and id by adding or updating an attribute (saves the changes into a JSON file).
Usage	update <class name> <id> <attribute name> "<attribute value>" ---or--- <class name>.update(<id>, <attribute name>, <attribute value>) --or-- <class name>.update(<id>, <dictionary representation>)
-----	-----
count	Retrieve the number of instances of a class.
Usage	<class name>.count()

Authors

Habtamu Gebre

Josephine Dassah
