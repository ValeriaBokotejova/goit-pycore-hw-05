def input_error(func): # Decorator for handling user input errors
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
        except:
            return "Invalid command."
    return inner


def parse_input(user_input): # Command parser
    parts = user_input.split()
    cmd = parts[0].strip().lower() 
    args = parts[1:] 
    return cmd, args

@input_error
def add_contact(args, contacts): # Add contact
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts): # Edit contact
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    elif name not in contacts:
        return f"Contact '{name}' not found."

@input_error
def show_phone(args, contacts): # Show phone number
    if len(args) != 1:
        return "Please provide the name of the contact."
    name, = args
    if name in contacts:
        return f"The phone number for contact '{name}' is {contacts[name]}."
    elif name not in contacts:
        return f"Contact '{name}' not found."

@input_error
def show_all_contacts(contacts): # Show all contacts
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

@input_error
def process_input(command, args, contacts): # Commands
    if command == "hello":
        return "How can I help you?"
    elif command == "add":
        return add_contact(args, contacts)
    elif command == "change":
        return change_contact(args, contacts)
    elif command == "phone":
        return show_phone(args, contacts)
    elif command == "all":
        return show_all_contacts(contacts)
    else:
        return "Invalid command."

@input_error
def main(): # Function managing the main command processing loop
    contacts = {}
    print("Welcome to the assistant bot!")

    while True: 
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print(process_input(command, args, contacts))

if __name__ == "__main__":
    main()