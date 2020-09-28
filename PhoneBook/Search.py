
#Class to search if a given name already exists as a key in the Dictionary, it can search a complete or partial name
class Search(object):
   def __init__(self, book):
       self.book = book

   def start(self, name):
     temp = self.book.get_book()
     found = False
     output = ""
     for key in temp:
         keyname = key.get_fullname()
         if keyname.lower().find(name.lower()) != -1:
           found = True
           output += self.book.print_contact(key)
     if found == False:
         output = "Niets gevonden"
     return output
        
              
          




