def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contact_exists = contacts.get(name) != None
    if contact_exists:
        contacts[name] = phone
        return "Contact updated."
    return "Name not found."

def show_phone(args, contacts):
    name = args[0]
    contact_exists = contacts.get(name) != None
    if contact_exists:
        return f"{contacts[name]}"
    return "Name not found."

def show_all(contacts):
    return "\n".join(map(lambda x: f"{x} {contacts[x]}", contacts))

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        try:
            command, *args = parse_input(user_input)        

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "show":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")

        except:
            print("Invalid command.")

if __name__ == "__main__":
    main()