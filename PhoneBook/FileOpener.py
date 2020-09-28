
#Open the written txt file 
class FileOpener(object):

    def open_file(self):
       try:
        f = open("phonebook.txt", "r")
        return f
       except IOError:
           print("Er is een fout opgetreden")


