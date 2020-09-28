import pickle
from PhoneBook import *

#Writes a pickle file of the PhoneBook instance, and read the saved pickle, if there is no pickle (launching first time) 
#it creates a new Phonebook instance so it can be saved the next time
class Pickler(object):
      
    def start_pickle(obj):
        pickle_file = open("phonebook.pickle", "wb")
        pickle.dump(obj, pickle_file)
        pickle_file.close()

    
    def load_pickle():
        try:
           pickle_load = open("phonebook.pickle", "rb")
           obj = pickle.load(pickle_load)
           return obj
        except:
           print("geen pickle gevonden, nieuw object aangemaakt")
           new_book = PhoneBook()
           return new_book









