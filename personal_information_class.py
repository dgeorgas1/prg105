"""Chapter 10 Practice 1 Program - Personal Information Class

Assignment Requirements:
Design a class that holds the following personal data: name, address, age, and phone number. Write
appropriate accessor and mutator methods (get and set). Write a program that creates three instances of
the class. One instance should hold your information and the other two should hold your friends' or family
members' information.  Just add information, don't get it from the user.  Print the data from each object,
make sure to format the output for clarity and ease of reading.

For this assignment, a class diagram is provided for you. In future assignments, you will have to plan your
own project using class diagrams, do this using Word and a single column table. The video also explains what
accessors (getters) and mutators (setters) are."""


class PersonalInformation:
    def __init__(self, name=0, address=0, age=0, phone=0):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone


def main():
    person1 = PersonalInformation()
    person2 = PersonalInformation()
    person3 = PersonalInformation()

    person1.set_name("Dan")
    person1.set_address("Spring Grove, IL")
    person1.set_age(27)
    person1.set_phone("234-567-8901")

    person2.set_name("Heather")
    person2.set_address("Spring Grove, IL")
    person2.set_age(32)
    person2.set_phone("207-302-1029")

    person3.set_name("Allison")
    person3.set_address("Mundelein, IL")
    person3.set_age(29)
    person3.set_phone("987-654-3210")

    print(f'{person1.get_name()}, age {person1.get_age()}\n{person1.get_address()}\n{person1.get_phone()}\n')
    print(f'{person2.get_name()}, age {person2.get_age()}\n{person2.get_address()}\n{person2.get_phone()}\n')
    print(f'{person3.get_name()}, age {person3.get_age()}\n{person3.get_address()}\n{person3.get_phone()}\n')


main()
