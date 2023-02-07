import random
import time
import numpy as np
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color
from threading import Thread, Lock

############################################################################################################
#Functions
############################################################################################################

def randomReflect(curDirection,offset):
    
    left_bound = curDirection - 90 - offset     
    right_bound = curDirection + 90 + offset    

    if left_bound < 0:
        left_bound += 360
        right_bound += 360
        new_direction = random.randint(min(left_bound%360, right_bound%360),max(left_bound%360, right_bound%360))
    else:
        new_direction = random.randint(min(left_bound%360, right_bound%360),max(left_bound%360, right_bound%360))

    return new_direction

def trap_escape(droid):
    # Define global variables
    global mainLed_color,  bot_speed, trap_speed_list, lock, curDirection
    
    # Use a try-except block to handle keyboard interrupt
    try:
        while True:
            velocity = droid.get_velocity()
            velocity_norm = np.linalg.norm(list(velocity.values()))
            # Check if the velocity norm is less than or equal to 0.1
            if velocity_norm <= 0.1:
                droid.strobe(Color(255, 57, 66), (1 / 3) * .5, 3)    #strobe red to indicate trap
                print("trap detected")
                trap_speed_list.append(round(velocity_norm))
                trap_speed_list.pop(0)
                # Check if the last three velocity norms are all 0
                if trap_speed_list == [0, 0, 0]:
                    # Acquire lock to change direction
                    with lock:
                        # Change direction randomly by 180 degrees
                        curDirection = int(curDirection + 180)%360
                        droid.roll(curDirection, bot_speed, 10)
                        time.sleep(1)
                    trap_speed_list = [1, 1, 1]
    except KeyboardInterrupt:
        print("Thread interrupted by user")


def onCollision(droid):
    global mainLed_color,  bot_speed, lock, curDirection,r,lock, flag, block_movement
    if flag:      #if the collision is already detected, then
        return      
    flag = True
    try:
        #block_movement = True
        print("in collision")
        #colorlist containinfg the following colors: red, green, blue, white
        colors=[Color(255, 0, 0),Color(0, 255, 0),Color(0, 0, 255),Color(255, 255, 255)]
        mainLed_color = colors[r]
        droid.set_main_led(mainLed_color) 
        r= (r+1)%4
        print("curDirection=", curDirection)
        #Change direction randomly by random degrees
        curDirection = randomReflect(curDirection, 50)
        droid.roll(curDirection, bot_speed, 1)
        #droid.roll(curDirection, 255, 1)
        #time.sleep(0.1)
        print("out collision")
    finally:
        block_movement = False
        flag = False
        move(droid)
        

def move(droid):
    global bot_speed,curDirection,block_movement
    try:
        while True:
            if not block_movement:
                droid.roll(curDirection, bot_speed, 20)
    except KeyboardInterrupt:
        print("Thread interrupted by user")
    
    
def connection():
    toy = scanner.find_toy(toy_name="SB-7F73")
    return toy


def main():
    global mainLed_color,  bot_speed, lock, curDirection
    with SpheroEduAPI(toy) as droid:
        droid.register_event(EventType.on_collision, onCollision)
        droid.set_front_led(frontLed_color)
        #droid.reset_aim()                                  # note the bot save his orientation beetwen two runs
        #droid.start_ir_broadcast(0,7)
        lock = Lock()
        try:
            #droid.start_ir_follow(0,1)
            #droid.start_ir_broadcast(0,1)
            droid.set_main_led(mainLed_color)
            #thread2 = Thread(target=trap_escape, args=((droid,)))
            #thread2.start()
            move(droid)
        except KeyboardInterrupt:
             print("Thread interrupted by user")
    
            
############################################################################################################
# constants
############################################################################################################       
#toy = scanner.find_toy(toy_name="SB-719D")
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

bot_speed = 80 # 0-255 

lock = Lock()


############################################################################################################
# Main
############################################################################################################
if __name__ == '__main__':
    main()
    
        
       