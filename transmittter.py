# random Radio rock paper scissors
from microbit import *
import radio
import random 

choices = ["rock","paper","scissors"]

radio.on() #turn radio on 

while True:
    if button_a.was_pressed():
       mychoice = display.scroll(random.choice(choices))
       yourchoice = radio.send(random.choice(choices))
        sleep(5000)
            if mychoice == rock and yourchoice == scissors:
                display.scroll("you won!")
                elif mychoice == scissors and yourchoice == rock:
                    display.scroll("you lost!")
                        elif mychoice == scissors and yourchoice == paper:
                            display.scroll("you won!")
                             elif mychoice == paper and yourchoice == scissors:
                                 display.scroll("you lost!")
                                    elif mychoice == paper and yourchoice == rock:
                                        display.scroll("you won!")
                                            elif mychoice == rock and yourchoice == paper:
                                                display.scroll("you lost!")
                                                    elif mychoice == rock and yourchoice == rock:
                                                        display.scroll("it's a draw!")
                                                            elif mychoice == paper and yourchoice == paper:
                                                                display.scroll("it's a draw!")
                                                                    elif mychoice == scissors and yourchoice == scissors:    
                                                                        display.scroll("it's a draw!")
                                                                        
