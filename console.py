#!/usr/bin/env python3

"""Create a cmd line from python cmd"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        print()
        return True

    def emptyline(self):
        "Empty line command"
        pass

    def help_quit(self):
        """Print help message for quit command"""
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """Print help message for EOF command"""
        print("EOF (Ctrl+D) command to exit the program")
        print()

    def help_all(self):
        """Prints help message for <all> command"""
        print("Prints all string representation of all objects")
        print()

    def help_create(self):
        """Prints help message for <create> command"""
        print("Creates a new instance of a class")
        print()

    def help_show(self):
        """Prints help message for <show> command"""
        print("Prints the string representation of an instance")
        print()

    def help_destroy(self):
        """Prints help message for <destroy> command"""
        print("Deletes an instance based on the class name and ID")
        print()

    def help_update(self):
        """Prints help message for <update> command"""
        print("Updates an instance based on the class name and ID")
        print()

    def precmd(self, line):
        """
        Override the precmd method to modify the user command before execution.
        This method is called before executing each command.
        """
        if '.' in line and 'all()' in line:
            parts = line.split('.')
            class_name = parts[0]
            modified_line = 'all ' + class_name
            print(modified_line)
            return modified_line
        print(line)
        return line

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if args:
            if any(args[0] not in key for key in storage.all().keys()):
                print("** class doesn't exist **")
                return
            objects = {k: v for k, v in storage.all().items() if args[0] in k}
        else:
            objects = storage.all()

        print([str(v) for v in objects.values()])


    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            if attr_type is str:
                attr_value = str(attr_value)
            elif attr_type is int:
                try:
                    attr_value = int(attr_value)
                except ValueError:
                    print("** invalid value type, must be an integer **")
                    return
            elif attr_type is float:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    print("** invalid value type, must be a float **")
                    return
            else:
                print("** invalid value type, must be a string, integer, or float **")
                return

            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            setattr(obj, attr_name, attr_value)
            obj.save()



if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     # Run in non-interactive mode
    #     HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    # else:
    #     # Run in interactive mode
    HBNBCommand().cmdloop()