from Person import *
from Printer import *

#Class for setting the correct novi emailadress. In uses multiple inherantace to store the fname and lname in Person class and to use Printer functions
#Hashcode is calculated using first and lastname so the Dictionary key can be compared using this to see if a value already exists
class Email(Person, Printer):
   def __init__(self, fname, lname):
      Person.__init__(self,fname, lname)

   def get_email(self):
       if len(self.get_fname()) > 1 and len(self.get_lname()) > 1:
            return self.get_fname().strip() + "." + self.get_lname().strip() + "@novi.nl"
       else:
            return None

   def check_info(self):
       if  self.get_email():
             return True
       else:
             return False

   def return_info(self):
       return self.get_email()

   def get_title(self):
        return "Email:\n"

   def __repr__(self):
       return  Person.__repr__(self)

   def __hash__(self):
        return hash(self.get_fullname())

   def __eq__(self, other):
        return self.get_fullname() == other.get_fullname()