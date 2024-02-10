# AirBnb Project.
This is the first step towards building a full stack web application : <b>AirBnB colne </b>
This part of the project focuses on building a console application to interact with the various features of the web application.

## The command interpreter:
The [command interpreter](console.py) is a console application that allows the user to interact with the web application. It is built using the [cmd](https://docs.python.org/3/library/cmd.html) module in python.

### How to start the command interpreter
1. Clone the repository
2. install python 2.8^
3. cd into the [AirBnB_clone](.) folder
3. run the command: <code>./console.py</code>

### How to use it
There are various commands integrated into the console.

create: 
    Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel

    If the class name is missing, print ** class name missing ** (ex: $ create)
    If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)

    show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.

    If the class name is missing, print ** class name missing ** (ex: $ show)
    If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
    If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
    If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)




5        examples
