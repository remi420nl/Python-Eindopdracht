from Adress import *
from Person import *
from PhoneNumber import *
from Email import *

class PhoneBook:
  #Constructor with Dictionary
  def __init__(self):
    self.book = {}

  #Checks if first and lastname (hashcode) to be added already exists in Dict
  def add_to_book(self, fname,lname):
     found = False
     self.key = Email(fname,lname)
   
     for temp in self.book:
        if temp == self.key:
               found = True

     return found

  #returns Dict
  def get_book(self):
     return self.book

  #Sets Email instance as key and makes List of Adress and Phonenumber instances to set them as value
  def add_new_contact(self,  street,postcode,city, fnumber):
     
     Adress_list = Adress(street,postcode,city)
     Phonenumber = PhoneNumber(fnumber)
     self.contact_info = [Adress_list,Phonenumber]
     self.book[self.key] = self.contact_info

 #Chekcs check if adress and/or tel is changed
  def replace_contact(self, street,postcode,city, fnumber):
      adresstochange = Adress( street,postcode,city)
      temp_adress = self.book[self.key][0]
      tempnumber = self.book[self.key][1].get_number()
      if (tempnumber == fnumber):
          self.replace_adress(street,postcode,city)
      elif(tempnumber != fnumber and temp_adress != adresstochange):
          self.replace_adress(street,postcode,city)
          self.replace_number(fnumber)
      else:
          self.replace_number(fnumber)


  #Stores old number and rewrites List, after deleing the original key it assigns a new key with adjusted List (value)
  def replace_adress(self, street, postcode, city):
      temp_number = self.book[self.key][1]
      r = dict(self.book)
      del r[self.key]
      self.book = r
      Adress_list2 = Adress(street, postcode, city)
      Phonenumber2 = temp_number
      self.new_contact_info = [Adress_list2,Phonenumber2 ]

      self.book[self.key] = self.new_contact_info

 #Stores old adress and rewrites List, after deleing the original key it assigns a new key with adjusted List (value)
  def replace_number(self, fnumber):
      temp_adress = self.book[self.key][0]
      r = dict(self.book)
      del r[self.key]
      self.book = r
      Adress_list2 = temp_adress
      Phonenumber2 = PhoneNumber(fnumber)
      self.new_contact_info = [Adress_list2, Phonenumber2]

      self.book[self.key] = self.new_contact_info


 #Prints complete book using superclass using several function and returns it in correct format
  def print_book(self):
        content = ""
        for naam, contactinfo in self.book.items():
            content += naam.get_fullname() + "\n"
            content += contactinfo[0].check_contactinfo()
            content += contactinfo[1].check_contactinfo()
            content += naam.check_contactinfo()
            content += self.print_line()
        return content

  #Prints only one contact that mathces the Dict key
  def print_contact(self, key):
        content = ""
        contactinfo = self.book.get(key)

        content +=  key.get_fullname() + "\n"
        content += contactinfo[0].check_contactinfo()
        content += contactinfo[1].check_contactinfo()
        content += key.check_contactinfo()
        content += self.print_line()
        
        return content


  def print_line(self):
      return "----------\n\n" 

  #Clear Dictionary
  def clear_phonebook(self):
     self.book.clear()

 #Returns length of Dictionary in string format, for dialog box
  def get_total(self):
      return str(len(self.book))






