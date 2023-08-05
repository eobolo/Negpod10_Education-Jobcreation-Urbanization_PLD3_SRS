#!/usr/bin/python3
class Employers():
    __counter = 0

    def __init__(self, counter, name, email, password,
                 dob, phnum, age, status):
        type(self).__counter += counter + 1
        self.counter = Employers.__counter
        self.name = name
        self.__email = email
        self.__password = password
        self.dob = dob
        self.phnum = phnum
        self.age = age
        self.status = status

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @staticmethod
    def counter_return():
        return Employers.__counter

    def employers_forget_details(self):
        print("This is your password {}".format(self.password))
        print("yes for employer no for employer: status is {}"
              .format(self.status))
        print("employee or employer number is {}".format(self.counter))
