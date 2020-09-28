import tkinter as tk
from tkinter import messagebox
from PhoneBook import *
from Search import *
from FileSaver import *
from FileOpener import *
import threading
import time
from Clock import *
from Pickler import Pickler
from Client import *
from Server import *

'''''
Eindopdracht Python
Remi Peerlings
Novi Maastricht
5-3-2020
'''''


#Sets variable equal to new loaded pickle (PhoneBook instance), so it always starts in the latest saved state
Phone_book = Pickler.load_pickle()

class MainProgramma(tk.Tk):
    def __init__(self):
      tk.Tk.__init__(self)


      #Settin Layout and using self because superclass is tk
      self.geometry("600x600")
      self.title("Python eindopdracht")
      menu = tk.Menu(self)
      self.config(menu=menu)
      # Menu with commands
      file_menu = tk.Menu(menu)
      menu.add_cascade(label="Bestand", menu=file_menu)
      file_menu.add_command(label="Print tekstbestand", command= lambda: display_output())
      file_menu.add_command(label="Opslaan in tekstbestand", command= lambda: save_book())
      file_menu.add_separator()
      file_menu.add_command(label="Start Server", command= lambda: start_server())
      file_menu.add_command(label="Download tekstbestand", command= lambda: start_client())
      file_menu.add_command(label="Totaal contacten", command= lambda: show_total())
      file_menu.add_separator()
      file_menu.add_command(label="Afsluiten", command= lambda : exit())

      heading = tk.Label(text="Telefoonboek Novi Medewerkers", bg="grey", fg="white", width="500")
      heading.pack()
      
      #Labels and placing
      first_name_label = tk.Label(text="Voornaam")
      last_name_label = tk.Label(text="Achternaam")
      street_label = tk.Label(text="Straat")
      postcode_label = tk.Label(text="Postcode")
      city_label = tk.Label(text="Woonplaats")
      tel_label = tk.Label(text="Telefoonnummer")
      first_name_label.place(x=20, y=50)
      last_name_label.place(x=20, y=80)
      street_label.place(x=20, y=110)
      postcode_label.place(x=20, y=140)
      city_label.place(x=20, y=170)
      tel_label.place(x=20, y=200)
      self.output = tk.Text(self, height=15, width=68)
      self.output.pack()
      self.output.place(x=20, y=300)

      #A Status bar at the bottom of the screen to show to clock using a Thread and Whili loop
      time_label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
      time_label.pack(side=tk.BOTTOM, fill=tk.X)

      fname = tk.StringVar()
      lname = tk.StringVar()
      street = tk.StringVar()
      postcode = tk.StringVar()
      city = tk.StringVar()
      telnr = tk.StringVar()
      search = tk.StringVar()
      display = tk.StringVar()

      self.display_label = tk.Label(self, textvariable=display)
      fname_input = tk.Entry(textvariable=fname)
      lname_input = tk.Entry(textvariable=lname)
      street_input = tk.Entry(textvariable=street)
      postcode__input = tk.Entry(textvariable=postcode)
      city_input = tk.Entry(textvariable=city)
      telnr_input = tk.Entry(textvariable=telnr)
      search_input = tk.Entry(textvariable=search)

      fname_input.place(x=120, y=50)
      lname_input.place(x=120, y=80)
      street_input.place(x=120, y=110)
      postcode__input.place(x=120, y=140)
      city_input.place(x=120, y=170)
      telnr_input.place(x=120, y=200)
      search_input.place(x=280, y=50)
      self.display_label.place(x=20, y=25)

      submit_button = tk.Button(text="Toevoegen", command= lambda: submit_contact())
      submit_button.place(x=20, y=240)
      clear_button = tk.Button(text="Wis Velden", command= lambda: erase_fields())
      clear_button.place(x=100, y=240)
      search_button = tk.Button(text="Zoek op naam", command= lambda: start_search(search.get()))
      search_button.place(x=280, y=80)
      save_button = tk.Button(text="Opslaan in Geheugen", command= lambda:  pickle_book())
      save_button.place(x=350, y=240)
      clearall_button = tk.Button(text="Wis geheugen", command= lambda: clear_phonebook())
      clearall_button.place(x=480, y=240)

      #Stops While loop before destroying mainloop to exit the app
      def exit():
         klok.turn_off()
         self.destroy() 

      #Search by name using a Search instance
      def start_search(name):
        start_search = Search(Phone_book)
        output = start_search.start(name)
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.INSERT, 'u zocht op %s \n\n' % name)
        self.output.insert(tk.INSERT, output)

      #Delete txt file, PhoneBook Dictionary and repickle it
      def clear_phonebook():
        Phone_book.clear_phonebook()
        FileSaver.clear_phonebook()
        pickle_book()
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.INSERT, "Alles gewist")

     #Pickle PhoneBook instance
      def pickle_book():
         Pickler.start_pickle(Phone_book)
         self.output.delete('1.0', tk.END)
         self.output.insert(tk.INSERT, "Object opgeslagen")

      #Start a client socket, for downloading the txt file
      def start_client():
          Client.startclient()
     
     #Start server using Thread otherwise the program freezes
      def start_server():
          t2 = threading.Thread(target= Server.startserver, args=())
          t2.setDaemon(True) 
          t2.start()
          
     #Erase all input fields
      def erase_fields():
        fname.set("")
        lname.set("")
        street.set("")
        postcode.set("")
        city.set("")
        telnr.set("")
        search.set("")

     #Open the saved txt file and display it in output textfield
      def display_output():
        OpenFile = FileOpener()
        file = OpenFile.open_file()
        self.output.delete('1.0', tk.END)
    
        self.output.insert(tk.INSERT, file.read())

      #Save the print_book() output to phonebook.txt
      def save_book():
        SaveFile = FileSaver()
        SaveFile.write_new_file(Phone_book.print_book())

      #Dialog for total Dictionary keys
      def show_total():
        messagebox.showinfo("Totaal aantal contacten", Phone_book.get_total())

      #Gets called after users presses "toevoegen", depending on if key exists it adds a new key or updates the existing value and displays output
      def submit_contact():
         if fname.get() != "" and lname.get() != "":
           if (Phone_book.add_to_book(fname.get(), lname.get())) is True:
              display.set("Bestaand contact bijgewerkt")
              Phone_book.replace_contact(street.get(), postcode.get(), city.get(), telnr.get())
           else:
             Phone_book.add_new_contact(street.get(), postcode.get(), city.get(), telnr.get())
             display.set("Nieuw contact aangemaakt")
         else:
             display.set("Geen volledige naam ingevuld")
      
      #Protocol rule for closing the tkinter window, so it calls the exit function the stop the loop otherwise it generates an error
      self.protocol("WM_DELETE_WINDOW", lambda: exit())

      #Start new thread for clock instance and give the tkinter time_label as parameter
      klok = Clock()
      t = threading.Thread(target= klok.startclock, name="Klok", args=(time_label,))
      t.setDaemon(True)
      t.start() 
      


b = MainProgramma()
b.mainloop()
