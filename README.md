# AirBNB Clone 
***
to project AirBNB clone, to Holberton School.
## Description
---
![Phase 1](https://imgur.com/a/bp3kiNa "Phase 1")

This is a C.L.I. (Command Line Interpreter) prepare to manage and store your AirBNB objects, in a JSON database.
 #### Environment 
* OS: Ubuntu 14.04 LTS
* Language: Python 3.4.3
* Style
* Python PEP 8 (v.1.7.0)

## Storage
All data will be stored and modified in the filename <data.json>
## Console
The console  can be runned  in interactive and non-interactive mode. 

### Interactive Mode
Init the console in interactive mode with te command:
```
 % ./console.py
(hbnb)
```
To get help type the command ***help***  or ***help command***, also you can finish the execution with ***quit*** command
```
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)help all

             Prints the string representation of
             all instances based or not on the class name.
        
(hbnb)quit
```

### Non - Interactive Mode
Also it can be used in non-interactive mode as follows:
```
 % echo "help" | ./console.py 
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)%  
```
 # Capabilities of CLI
~~~
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Update attributes of an object
* Destroy an object
* Show an object attributes
~~~
## Testing
---
 ###  Unittest Module
This project uses python library, unittest to run tests on all python files. All unittests are in the ./tests directory with the command:
-  python3 -m unittest discover -v ./tests/


## Authors
---
 - Luis Mejia [@Lemmishmaniasis](https://www.twitter.com) [GitHub](https://github.com/lemejiamo)
 

