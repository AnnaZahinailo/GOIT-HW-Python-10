import re

from classes import AddressBook, Record, Name

users = AddressBook()

def input_error(func):
    def inner(*args):
        try: 
            return func(*args)
        except KeyError:
            return f"Enter user name."
        except ValueError:
            return "Give me name and phone corretly please."
        except IndexError:
            return "Give me name and phone corretly please."
        except TypeError:
            return "Give me name and phone corretly please."
    return inner


def cmd_hello_func(*_): 
    return "How can I help you?"


@input_error
def cmd_add_func(name, *phones):
    if name and not re.match(r"^\w+$", name):
        raise ValueError
    if name in users and not phones:
            return f"The name {name} is already registred in the Address Book."
    user = Record(Name(name))
    if name not in users:
        user.phone_list = []
    else:
        user.phone_list = users.get(name)
    new_phones_list = []
    p = ""
    rp = ""
    if phones:
        for phone in phones:
            if phone and not re.match(r"^\+[\d]{12}$", phone):
                raise ValueError        
            if phone in user.phone_list and len(phones) == 1:
                return f"The phone number {phone} is already registred in the Address Book."    
            elif phone in user.phone_list and len(phones) > 1:
                rp += f"\nThe phone number {phone} is already registred in the Address Book." 
            else:
                user.add_phone(phone)
                new_phones_list.append(phone)
    users.add_record(user)
    p = ", ".join(new_phones_list)
    return f"{name} {p} has been added to the Address Book.{rp}"


@input_error
def cmd_change_phone_func(name, phone, new_phone):
    if name and not re.match(r"^\w+$", name):
        raise ValueError
    if new_phone and not re.match(r"^\+[\d]{12}$", phone):
        raise ValueError
    if name not in users:
        return f"User {name} is not in the Address Book."
    else:
        user = Record(Name(name), phone)
        user.phone_list = users.get(name)
        if name in users and new_phone in user.phone_list:
            return f"The phone number {phone} is already registred in the Address Book."    
        user.change_phone(phone, new_phone)  
        return f"The phone number {phone} for {name} has been changed for {new_phone}."


@input_error
def cmd_delete_phone_func(name, phone):
    if name and not re.match(r"^\w+$", name):
        raise ValueError
    if phone and not re.match(r"^\+[\d]{12}$", phone):
        raise ValueError
    user = Record(Name(name))
    user.phone_list = users.get(name)
    if not name in users:
        return f"No user {name} in the Address Book."
    if phone not in user.phone_list:
        return f"The phone number {phone} is not in the Address Book."
    user.delete_phone(phone)
    return f"The phone number {phone} for {name} has been deleted."



@input_error
def cmd_phone_func(*args):
    name = args[0]
    if name and not re.match(r"^\w+$", name):
        raise ValueError
    phone_list = users.get(name)
    if not name in users:
        return f"No user {name} in the Address Book."
    elif phone_list == []:
        return f"No phones for {name} in the Address Book."
    else:
        return f"{name}: " + ", ".join(phone_list)


def cmd_show_all_func(*_): 
    all = ""
    if len(users) == 0:
        return "No items in the Address Book"
    else:
        for name, phone in users.items():
            all += name + ": " + ", ".join(phone) + "\n"
        return all + "All users are displayed"

 
def help_info(): 
     return """You can manage your Address Book with the commands:
           hello
           add 'Name' ['+380000000000'] ['+380000000001']
           change phone 'Name' '+380000000000' '+380000000001'
           delete phone 'Name' '+380000000000'
           phone 'Name'
           show all
           good bye
           close
           exit"""


def cmd_exit_func(*_):
     return "Good bye!\n"


COMMANDS = {
    'hello': cmd_hello_func,
    'add': cmd_add_func,
    'change phone': cmd_change_phone_func,
    'delete phone': cmd_delete_phone_func,
    'phone': cmd_phone_func,
    'show all': cmd_show_all_func,
    'good bye': cmd_exit_func,
    'close': cmd_exit_func,
    'exit': cmd_exit_func,
}


def cmd_parser(command_line: str):          
    for cmd in COMMANDS:
        space_case = ' ' if cmd in ('add', 'change phone', 'delete phone', 'phone') else '' #to avoid an incorrect commandline that didn't interrupt the program in received version
        if command_line.startswith(cmd + space_case):
            return COMMANDS[cmd], command_line.replace(cmd, '').strip().split()
    return None, []


def main():
    command_line = ""
    print("\nHello!")
    print(help_info())

    while True:
        command_line = input("\nEnter command: ")
        command, data = cmd_parser(command_line)

        if not command:
            print("No command. Try again!")
        else:
            print(command(*data))

            if command == cmd_exit_func:
                break


if __name__ == "__main__":
    main()