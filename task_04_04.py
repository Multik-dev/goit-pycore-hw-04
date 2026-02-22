def parse_input(user_input: str):
    """
    Розбиває введення на команду та аргументи.
    Команда не залежить від регістру.
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add <name> <phone>"

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change <name> <phone>"

    name, phone = args
    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone <name>"

    name = args[0]
    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts saved."

    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            result = add_contact(args, contacts)
            print(result)

        elif command == "change":
            result = change_contact(args, contacts)
            print(result)

        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)

        elif command == "all":
            result = show_all(contacts)
            print(result)

        else:
            # і сюди потрапляємо також, якщо command == "" (порожній ввід)
            print("Invalid command.")


if __name__ == "__main__":
    main()
