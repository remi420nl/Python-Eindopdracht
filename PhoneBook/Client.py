import socket
import time
import os

#Client using default hostname for receiving the sent txt by the server and store it at users Desktop in txt format
class Client():

  def startclient():
      hostname = socket.gethostname()
      port = 1234
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((hostname, port))
      print("Connected(client)")

      time.sleep(1)
      print("geef een naam op:")
      filenametemp = input(str(">>")) + ".txt"
      filename = os.path.join(os.environ["HOMEPATH"], "Desktop" + "\\" +  filenametemp)
      file = open(filename, "wb")
      file_data = s.recv(1024)
      file.write(file_data)
      file.close()
      print("bestand op bureaublad geplaatst")

     

