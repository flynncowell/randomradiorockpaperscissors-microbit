# Radio rock paper scissors
from microbit import *
import radio
import random 

choices = ["rock","paper","scisssors"]

radio.on() #turn radio on 

while True:
    mychoice = radio.reciveve()
        display.scroll(mychoice)
        
        
