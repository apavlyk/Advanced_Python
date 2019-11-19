#!/usr/bin/python


class Person(object):

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    def test_metH(self, block=True, *args):
        pass


if __name__ == '__main__':
    person = Person("John", "Smith", "31")
    print("Hello {} {}! How are you?".format(person.name, person.surname))
    print(person.age)
