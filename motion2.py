from gpiozero import MotionSensor
import time
time.sleep(4)
pir=MotionSensor(4)
while(True):
    if pir.motion_detected:
        import os
        os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/dl3/5.jpg")
        print("pic Taken")    
        
        
        print("motion detected")
    else:
        print("not detectedZ")
