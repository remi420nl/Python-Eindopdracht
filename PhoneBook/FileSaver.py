
#Save a new or rewrite phonebook.txt with the content giving as parameter, and a function to erase everything.
class FileSaver(object):
    def __index__(self):
        pass

    def write_new_file(self,content):
       try:
        f = open("phonebook.txt", "w" )
        f.write(content)

       except IOError:
           print("Er is een fout opgetreden")
       finally:
           f.close()

    def clear_phonebook():
       try:
         f = open("phonebook.txt", "w" )
         f.write("")

       except IOError:
            print("Er is een fout opgetreden met het wissen")
       finally:
           f.close()