#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage
"""Create a cmd line from python cmd"""
import cmd
class HBNBCommand(cmd.Cmd):
    intro = "Welcome to the HBNB Console Type (help) for more information"
    prompt = "(hbnb) "
    def do_help(self, arg):
        """ print the usage information of a command """
        print("Usage: Type help(command) for more information")
    
    def do_quit(self, arg):
        """ Exit the program """
        print("Exitting ... \n Done")
        return True
    
    def do_EOF(self, arg):
        """Exit the program (Ctrl-D)"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            print(arg)
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
            
    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key not in storage.all()[args[0]]:
            print("** no instance found **")
            return
        print(storage.all()[args[0]][instance_key])
        
    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        args = arg.split()
        instances = []
        if not args:
            for key, value in storage.all().items():
                instances.append(str(value))
        elif args[0] not in storage.all():
            print(storage.all())
            print("** class doesn't exist **")
            return
        else:
            for key, value in storage.all()[args[0]].items():
                instances.append(str(value))
        print(instances)
        

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key not in storage.all()[args[0]]:
            print("** no instance found **")
            return
        if len(args) < 4:
            print("** attribute name missing **")
            return
        if len(args) < 5:
            print("** value missing **")
            return

        instance = storage.all()[args[0]][instance_key]
        attribute_name = args[2]
        attribute_value = args[3]
        setattr(instance, attribute_name, eval(attribute_value))
        storage.save()
    
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()