#!/usr/bin/python3
"""Command interpreter module"""
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
cl = ['User', 'State', 'City', 'Amenity', 'Place', 'Review', 'BaseModel']


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
        """Prints the string representation of an instance"""
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
        """Prints string representations of all instances"""

        # Split the input into individual arguments
        args = arg.split()

        if len(args) == 0:
            # If no arguments provided.
            objects = storage.all().values()
            print([str(v) for v in objects])
            return

        if len(args) == 1:
            # If only one argument provided
            if args[0].endswith('.all()'):
                cls_name = args[0][:-6]
                if cls_name not in cl:
                    print("** class doesn't exist **")
                    return
                y = [x for x in storage.all().values() if isinstance(x, eval(cls_name))]
                print([str(x) for x in y])
                return

            # If argument is a class name
            class_name = args[0]
            if class_name not in cl:
                print("** class doesn't exist **")
                return
            y = [x for x in storage.all().values() if isinstance(x, eval(class_name))]
            print([str(x) for x in y])
            return

        if len(args) == 2:
            # If two arguments provided.
            if args[0] == 'all':
                cls_name = args[1]
                if cls_name not in cl:
                    print("** class doesn't exist **")
                    return
                y = [x for x in storage.all().values() if isinstance(x, eval(cls_name))]
                print([str(x) for x in y])
                return

        # Invalid arguments
        print("** invalid command format **")

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

    def do_count(self, arg):
        """Prints the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        classes = storage.all().keys()
        class_counts = [key.split('.')[0] for key in classes]

        if class_name not in class_counts:
            print("** class doesn't exist **")
            return

        count = sum(1 for key in classes if key.split('.')[0] == class_name)
        print(count)

    def default(self, line):
        """Excecutes for any other command"""
        if line.endswith('all()'):
            class_name = line.split('.')[0]
            self.do_all(class_name)

        elif line.endswith('count()'):
            class_name = line.split('.')[0]
            self.do_count(class_name)

        elif 'show(' in line:
            args = line.split('.')
            if len(args) != 2 or 'show(' not in args[1]:
                print("** invalid command format **")
                return
            class_name, rest = args
            instance_id = rest.split('(')[1].strip(')\"\'')
            self.do_show(f"{class_name.strip()} {instance_id}")

        elif 'destroy(' in line:
            args = line.split('.')
            if len(args) != 2 or 'destroy(' not in args[1]:
                print("** invalid command format **")
                return
            class_name, rest = args
            instance_id = rest.split('(')[1].strip(')\"\'')
            self.do_destroy(f"{class_name.strip()} {instance_id}")

        elif 'update(' in line:
            args = line.split('.')
            if len(args) != 2 or 'update(' not in args[1]:
                print("** invalid command format **")
                return
            cls, rest = args
            d, name, value = rest.split('(')[1].strip(')\"\'').split(',')
            self.do_update(f"{cls.strip()} {d.strip()} {name.strip()} {value.strip()}")

        elif 'update(' in line:
            args = line.split('.')
            if len(args) != 2 or 'update(' not in args[1]:
                print("** invalid command format **")
                return
            class_name, rest = args
            instance_id, attr_dict_str = rest.split('(')[1].strip(')\"\'').split(',', 1)
            attr_dict = eval(attr_dict_str.strip())
            self.do_update(f"{class_name.strip()} {instance_id.strip()} {attr_dict}")

        else:
            print("Invalid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
