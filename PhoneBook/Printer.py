
#Superclass for Adress,PhoneNumber and Email class, if returns the right format to be printed by  the phonebook
class Printer(object):

    def __init__(self):
        pass

    def not_found(self):
        content = self.get_title()
        content += "niet bekend \n"
        return content

    def check_contactinfo(self):

        if self.check_info():
            content = self.get_title()
            content += self.return_info()
            content += "\n"
            return content
        else:
            return self.not_found()



