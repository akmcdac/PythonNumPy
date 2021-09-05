# This is a week2 assignment Python script.
class Contact:
    def __init__(self, name, number, age):
        self.name = name
        self._number = number
        self.__age = age

    @property
    def get_number(self):
        return self._number

    @property
    def get_age(self):
        return self.__age


class PhoneBook:
    def __init__(self):
        self._contacts = []

    def add_contact(self, contact):
        for i, aContact in enumerate(self._contacts):
            if aContact.name == contact.name:
                self._contacts[i] = contact
                break
        else:
            self._contacts.append(contact)

    def get_contact(self, name):
        for contact in self._contacts:
            if contact.name == name:
                return contact


phoneBook = PhoneBook()

contact1 = Contact("Ajay", "8826688108", 36)
contact2 = Contact("Maurya", "9723546366", 26)
contact3 = Contact("Maurya", "9723546366", 22)

phoneBook.add_contact(contact1)
phoneBook.add_contact(contact2)
phoneBook.add_contact(contact3)

contactMaurya = phoneBook.get_contact("Ajay")

if isinstance(contactMaurya, Contact):
    print(contactMaurya.name + " " + str(contactMaurya.get_age) + " " + str(contactMaurya.get_number))
else:
    print("No user by that name")
