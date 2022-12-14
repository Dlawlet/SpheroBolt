import random
import sys
import time
from numpy import linalg as LA
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color
from threading import Thread

############################################################################################################
#Functions
############################################################################################################

def collison_detection(droido):
    global speed
    speed.append(tuple((droido.get_velocity()).values()))
    delta = abs(LA.norm(speed[-1])-LA.norm(speed[0]))
    if ( delta> 50):                                          #note: the value of delta is not constant it depends on the speed of the bot
        print(delta)
        droido._collision_detected_notify()
    speed.pop(0)

def trapescape(droid):
    global mainLed_color, bot_orientation, bot_speed, trapsp
    if LA.norm(tuple((droid.get_velocity()).values()))<=0.1:
        trapsp.append(round(LA.norm(tuple((droid.get_velocity()).values()))))
        trapsp.pop(0)
        if trapsp == [0,0,0]:
            bot_orientation = (bot_orientation+180)%360
            droid.set_heading(bot_orientation)
            droid.set_speed(bot_speed)
            trapsp = [1,1,1]

def onCollision(droid):
    global mainLed_color, bot_orientation, bot_speed
    print("collision")
    #droid.stop_roll()
    #droid.strobe(Color(255, 57, 66), (1 / 3) * .5, 3)    
    r = random.randint(0, 255)
    #mainLed_color = Color(r,r,r)
    bot_orientation = (bot_orientation+180)%360
    #bot_speed = (bot_speed+100)%400+100

def mouve(droid):
    global trapsp, bot_orientation, bot_speed
    droid.set_heading(bot_orientation)
    droid.set_speed(bot_speed)
    collison_detection(droid)
    trapescape(droid)
    
    


def main():
    global mainLed_color, bot_orientation, bot_speed
    with SpheroEduAPI(toy) as droid:
        droid.register_event(EventType.on_collision, onCollision)
        droid.set_front_led(frontLed_color)
        #droid.reset_aim()                                  # note the bot save his orientation beetwen two runs
       
        
        while True:
            #droid.start_ir_broadcast(0,1)
            #droid.set_main_led(mainLed_color)

            mouve(droid)
            

############################################################################################################
# constants
############################################################################################################       
toy = scanner.find_toy(toy_name=sys.argv[1])
speed = [(0,0),(0,0)]
trapsp = [1,1,1]

flag = 1
mainLed_color = Color(0, 0, 255)
bot_orientation = 0
bot_speed = 100
frontLed_color = Color(0, 0, 255)


############################################################################################################
# Main
############################################################################################################

if __name__ == '__main__':
    main()
    
        
       