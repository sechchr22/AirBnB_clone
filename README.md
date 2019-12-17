# AirBnB clone - The console
The global approach of this project is about making an AirBnb clone, but on this one we will focus on only making our console (command interpreter).

### Whats a command interpreter?
A command interpreter is the part of a computer [operating system](https://whatis.techtarget.com/definition/operating-system-OS) that understands and executes commands that are entered interactively by a human being or from a program. In some operating systems, the command interpreter is called the [shell](https://searchdatacenter.techtarget.com/definition/shell).

 ### Our command interpreter
In our case, we want to be able to manage objects:
-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc
-   Do operations on objects (count, compute stats, etc)
-   Update attributes of an object
-   Destroy an object

#### interactive mode
 ````
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
````

#### non-interactive mode
```
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
```

### Set up
```
git clone https://github.com/gefranco/AirBnB_clone.git
```

### Starting the console
```
./console.py
(hbnb)
```
### Commands
| Command | Description |
| ------ | ------ |
| all | Prints all string representation of all instances|
| create | Creates a new instance of BaseModel |
| destroy | Deletes an instance based on the class name and id |
| show |  Prints the string representation of an instance based on the class name and id |
| update | Update the instance |
| help | List available commands with "help" or detailed help with "help cmd" |
| quit | Quit command to exit the program |
| EOF | Quit command to exit the program when hitting CTRL + D |

### Examples

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

Undocumented commands:
======================
count

(hbnb)
```
```
(hbnb) create BaseModel
79916999-ae52-42f0-9a32-d344152cb73b
(hbnb) show BaseModel 79916999-ae52-42f0-9a32-d344152cb73b
[BaseModel] (79916999-ae52-42f0-9a32-d344152cb73b) {'created_at': datetime.datetime(2019, 11, 14, 4, 45, 10, 593924), 'updated_at': datetime.datetime(2019, 11, 14, 4, 45, 10, 593948), 'id': '79916999-ae52-42f0-9a32-d344152cb73b'}
```

