import socket
    
#Start a socket and waits for incoming client, then it reads bytes of the phonebook.txt file and sends it data
class Server():

   def startserver():
      hostname = socket.gethostname()
      port = 1234
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.bind((hostname, port))
      s.listen(1)
      print("Wachten op inkomende verbinding")
      connection, adr = s.accept()
      print(adr, " is verbonden")

      file = open("phonebook.txt", "rb")
      file_data = file.read(1024)
      connection.send(file_data)



