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
        self._contacts = {}

    def add_contact(self, contact):
        self._contacts[contact.name] = contact

    def get_contact(self, name):
        if name in self._contacts:
            return self._contacts[name]


phoneBook = PhoneBook()

contact1 = Contact("Ajay", "8826688108", 36)
contact2 = Contact("Maurya", "9833447722", 26)
contact3 = Contact("Maurya", "9833447722", 22)

phoneBook.add_contact(contact1)
phoneBook.add_contact(contact2)
phoneBook.add_contact(contact3)

phoneContactMaurya = phoneBook.get_contact("Maurya")

if isinstance(phoneContactMaurya, Contact):
    print(phoneContactMaurya.name + " " + str(phoneContactMaurya.get_age) + " " + str(phoneContactMaurya.get_number))
else:
    print("No Phone contact found")
