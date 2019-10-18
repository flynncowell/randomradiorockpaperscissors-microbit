# Radio rock paper scissors
from microbit import *
import radio
import random 

choices = ["rock","paper","scisssors"]

radio.on() #turn radio on 
 

while True:
    if radio.recieve() == choices:
    choice1 = radio.recieve()
    choice2 = random.choice(choices)
        radio.send(choice2)
    
