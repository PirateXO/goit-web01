def main():
    book = load_data()
    view = ConsoleView()

    view.display_message("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            view.display_message("Data saved. Good bye!")
            break

        elif command == "hello":
            view.display_message("How can I help you?")

        elif command == "add":
            view.display_message(add_contact(args, book))

        elif command == "change":
            view.display_message(change_phone(args, book))

        elif command == "phone":
            contact = show_phone(args, book)
            view.display_contact(contact)

        elif command == "all":
            all_contacts = show_all_contacts(args, book)
            view.display_all_contacts(all_contacts)

        elif command == "add-birthday":
            view.display_message(add_birthday(args, book))

        elif command == "show-birthday":
            birthday_message = show_birthday(args, book)
            view.display_message(birthday_message)

        elif command == "birthdays":
            upcoming_birthdays = show_upcoming_birthdays(args, book)
            view.display_upcoming_birthdays(upcoming_birthdays)

        else:
            view.display_message("Invalid command.")
