from Printer import *


#To store adress using 3 atributs. The hashcode calculates the hash based on string of 3 atributes
class Adress(Printer): 

    def __init__(self, street, postcode, city):
        self.__street = street
        self.__postcode = postcode
        self.__city = city

    def get_street(self):
        return self.__street

    def get_postcode(self):
        return self.__postcode

    def get_city(self):
        return self.__city

    def check_info(self):
        if self.get_street() == "" and self.get_postcode() == "" and self.get_city() == "":
            return False
        else:
            return True
    
    def return_info(self):
        return self.get_street() +"\n" + self.get_postcode() +"\n" + self.get_city()

    def print_adress(self):
        return self.check_adress()

    def get_title(self):
        return "Adres:\n"

    def __repr__(self):
        return self.print_adress()

    def __str__(self):
        return self.print_adress()

    def __hash__(self):
        return hash(self.return_info())

    def __eq__(self, other):
        return self.return_info() == other.return_info()
