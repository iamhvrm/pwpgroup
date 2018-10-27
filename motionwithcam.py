from gpiozero import MotionSensor
import os

import time
time.sleep(14)
pir=MotionSensor(4)

while(True):
    if pir.motion_detected:
       
        os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/dl3/6.jpg")
        print("pic Taken")    
        
        
        print("motion detected")
    else:
        print("not detectedZ")
    time.sleep(2)
