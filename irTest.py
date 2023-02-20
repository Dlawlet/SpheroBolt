import random
import sys
import time
import numpy as np
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color
from threading import Thread, Lock

############################################################################################################
#Functions
############################################################################################################
def move(droid):
    global bot_speed,curDirection,block_movement,offset,lock

    direction_counter = random.random()*2
    print(int(droid.get_luminosity()['ambient_light']))
    try:
        if not block_movement and int(droid.get_luminosity()['ambient_light']) <= 500:
            droid.roll(curDirection, bot_speed, direction_counter)
        elif int(droid.get_luminosity()['ambient_light']) > 500 :
            if block_movement:      #if the light is already detected, then
                return      
            block_movement = True
            try:
                droid.stop_roll()
                droid.strobe(Color(255, 57, 66), (3 / 15) * .5, 15)
                while int(droid.get_luminosity()['ambient_light']) > 500:
                    droid.stop_roll()
            finally:
                block_movement = False
                
        offset = 50
        offset = 90


        move(droid)

       
    
            
    except KeyboardInterrupt:
        print("Thread interrupted by user")
        block_movement = True
    
    
def connection():
    if len(sys.argv) > 1:
        toy = scanner.find_toy(toy_name=serial_numbers[int(sys.argv[1])-1])
    else:
        toy = scanner.find_toy()
    return toy


def main():
    global mainLed_color,  bot_speed, lock, curDirection, block_movement
    with SpheroEduAPI(toy) as droid:
        #droid.start_ir_broadcast(4,5)
        
        while True:
            try: 
                droid.set_front_led(frontLed_color)
                #droid.send_ir_message(1,32)
                pass
            except KeyboardInterrupt:
                print("Thread interrupted by user")
                break
            
       
    
            
############################################################################################################
# constants
############################################################################################################       
#toy = scanner.find_toy(toy_name="SB-719D")
serial_numbers = [    "SB-31F6",    "SB-645E",    "SB-89C3",    "SB-9D95",    "SB-6D85",    "SB-3CE4",    "SB-CB70",    "SB-719D",    "SB-C7C7",    "SB-7F73",    "SB-1D85",    "SB-80F2",    "SB-AA77",    "SB-D760",    "SB-AEB1"]

toy = None
while toy == None:
    try :
        toy = connection()
    except Exception as e:
        toy = None  

r=0
speed = [(0,0),(0,0)]
trap_speed_list = [1,1,1]

curDirection = 0

flag = False
block_movement = False
# set mainLed_color to purple
mainLed_color = Color(255, 0, 255)
frontLed_color = Color(0, 0, 255)

bot_speed = 50 # 0-255 

lock = Lock()

offset = 90

############################################################################################################
# Main
############################################################################################################
if __name__ == '__main__':
    main()
    
        
       