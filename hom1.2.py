class ConsoleView(UserView):
    def display_message(self, message: str):
        print(message)

    def display_contact(self, contact: str):
        print(contact)

    def display_all_contacts(self, contacts: str):
        print(contacts)

    def display_upcoming_birthdays(self, birthdays: str):
        print(birthdays)

    def display_help(self, help_message: str):
        print(help_message)
