
#Class for setting the first and lastname
class Person(object):
    def __init__(self, fname, lname):
      self.__fname = fname
      self.__lname = lname

    def get_fullname(self):
        return self.__fname + " " + self.__lname

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def return_info(self):
        return get_fullname()

    def get_title(self):
        return "Naam:\n"

    def __repr__(self):
        return self.get_fullname()

