import random
import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI, EventType
from spherov2.types import Color
from threading import Thread, Lock

############################################################################################################
#Functions
############################################################################################################

def trap_escape(droid):
    # Define global variables
    global mainLed_color, bot_orientation, bot_speed, trap_speed_list, lock, curDirection
    
    # Use a try-except block to handle keyboard interrupt
    try:
        while True:
            velocity = droid.get_velocity()
            velocity_norm = np.linalg.norm(list(velocity.values()))
            # Check if the velocity norm is less than or equal to 0.1
            if velocity_norm <= 0.1:
                droid.strobe(Color(255, 57, 66), (1 / 3) * .5, 3)    #strobe red to indicate trap
                trap_speed_list.append(round(velocity_norm))
                trap_speed_list.pop(0)
                # Check if the last three velocity norms are all 0
                if trap_speed_list == [0, 0, 0]:
                    # Acquire lock to change direction
                    with lock:
                        # Change direction randomly by 180 degrees
                        curDirection = int(curDirection + 180)%360
                        droid.roll(curDirection, 60, 10)
                        time.sleep(1)
                    trap_speed_list = [1, 1, 1]
    except KeyboardInterrupt:
        print("Thread interrupted by user")


    

def onCollision(droid):
    global mainLed_color, bot_orientation, bot_speed, lock, curDirection,r,lock, flag
    if flag:      #if the collision is already detected, then
        return      
    flag = True
    try:
        print("in collision")
        #droid.stop_roll()
        #droid.strobe(Color(255, 57, 66), (1 / 3) * .5, 3)    
        colors=[Color(255, 57, 66),Color(255, 255, 255),Color(0, 255, 0),Color(0, 0, 255)]
        mainLed_color = colors[r]
        droid.set_main_led(mainLed_color)  
        r= (r+1)%4

        #curDirection = int(curDirection + 180)%360
        bot_speed = -bot_speed
        print("curDirection=", curDirection)
        # Change direction randomly by 180 degrees
        #curDirection = int(curDirection + 180*random.random())%360
        #droid.roll(curDirection, 1, 1)
        print("out collision")
    finally:
        flag = False
        mouve(droid)
        


def mouve(droid):
    global trapsp, bot_orientation, bot_speed,curDirection
    try:
        while True:
            droid.roll(curDirection, bot_speed, 10)
    except KeyboardInterrupt:
        print("Thread interrupted by user")
    
    
def connection():
    toy = scanner.find_toy(toy_name="SB-719D")
    return toy

def main():
    global mainLed_color, bot_orientation, bot_speed, lock, curDirection
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
            thread2 = Thread(target=trap_escape, args=((droid,)))
            thread2.start()
            mouve(droid)
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
mainLed_color = Color(0, 0, 255)
bot_orientation = 0
bot_speed = 100
frontLed_color = Color(0, 0, 255)

lock = Lock()

############################################################################################################
# Main
############################################################################################################

if __name__ == '__main__':
    main()
    
        
       