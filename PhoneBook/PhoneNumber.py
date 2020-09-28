from Printer import *

#For storing phonenumber
class PhoneNumber(Printer):
    def __init__(self, fnumber):
        self.__fnumber = fnumber

    def get_number(self):
        return self.__fnumber

    def check_info(self):
        if self.get_number() == "":
            return False
        else:
             return True

    def get_title(self):
        return "Telefoonnummer:\n"

    def return_info(self):
        return self.get_number()

    def __repr__(self):
        return self.__fnumber


