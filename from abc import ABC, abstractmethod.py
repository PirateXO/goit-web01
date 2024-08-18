from abc import ABC, abstractmethod

class UserView(ABC):
    @abstractmethod
    def display_message(self, message: str):
        pass

    @abstractmethod
    def display_contact(self, contact: str):
        pass

    @abstractmethod
    def display_all_contacts(self, contacts: str):
        pass

    @abstractmethod
    def display_upcoming_birthdays(self, birthdays: str):
        pass

    @abstractmethod
    def display_help(self, help_message: str):
        pass
