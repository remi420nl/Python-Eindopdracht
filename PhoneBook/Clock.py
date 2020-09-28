import time,threading,tkinter as tk

#Class for the clock instance at tkinter app which runs in a thread. Using time module we set a variable for the text in correct european format
#The while loop runs every second continuously 
class Clock():

    #Global variable so i let the while loop stop using a seperate function
    switch = True
    def __init__(self):
        pass

    def turn_off(self):  
      Clock.switch = False 

    def startclock(self, label):
       
        while Clock.switch:
            clock_time = time.strftime('Datum %d-%m-%Y Tijd %H:%M:%S', time.localtime())
            label.config(text=clock_time)
            time.sleep(1)





