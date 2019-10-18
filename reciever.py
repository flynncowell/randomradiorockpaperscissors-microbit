# random Radio rock paper scissors
from microbit import *
import radio
import random 

choices = ["rock","paper","scissors"]

radio.on() #turn radio on 

while True:
    if button_a.was_pressed():
       choice1= random.choice(choices)
       choice2 = radio.recieve()
       sleep(2000)
       display.scroll(choice1)
       radio.send(choice1)2
       
        sleep(5000)
            if choice1 == rock and choice2 == scissors:
                display.scroll("you won!")
                elif choice1 == scissors and choice2 == rock:
                    display.scroll("you lost!")
                        elif choice1 == scissors and choice2 == paper:
                            display.scroll("you won!")
                             elif choice1 == paper and choice2 == scissors:
                                 display.scroll("you lost!")
                                    elif choice1 == paper and choice2 == rock:
                                        display.scroll("you won!")
                                            elif choice1 == rock and choice2 == paper:
                                                display.scroll("you lost!")
                                                    elif choice1 == rock and choice2 == rock:
                                                        display.scroll("it's a draw!")
                                                            elif choice1 == paper and choice2 == paper:
                                                                display.scroll("it's a draw!")
                                                                    elif choice1 == scissors and choice2 == scissors:    
                                                                        display.scroll("it's a draw!")
        
        
