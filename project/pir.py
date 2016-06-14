
import RPi.GPIO as GPIO
import time
import os
import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(21,GPIO.IN)

now = datetime.today()
while True:
    input_state = GPIO.input(21)
    if input_state == True:
        GPIO.output(10,1)
        print('Motion Detected')
        # os.system('/home/pi/program/pushbullet.sh "Alert Motion Detected."') #notification sent to phone and lappy about activity
        time.sleep(2)
        GPIO.output(10,0)
        time.sleep(2)
    else
        if(now.hour>18 and now.hour<5)
            GPIO.output(10,0)
            """GPIO.output(,0) for fan, and other appliances"""

"""
#living room modes and activity detection near door
while steve_computer_vision.input != null :
    input_mode=steve_computer_vision.input()
    if input_mode.lower()=="sleep": #sleep mode
        GPIO.output(10,0) #lights off
        GPIO.output(,0) #all other appliances off
    elif input_mode.lower()=="study":
        GPIO.output(10,1)
        GPIO.output(,0)
    elif input_mode.lower()=="party":
        GPIO.output(10,0)
        GPIO.output(,1)
    elif input_mode.lower()=='music':
        GPIO.output(,1) #speaker turned on
    elif input_mode.lower()=='dnd' or 'do not disturb':
        GPIO.output(,0) #doorbell turned off
    elif input_mode.lower()=='empty':
        GPIO.output(,0) #turn off everything    


while True:
    input_unknown= GPIO.input(21)
    if(now.hour>12 and now.hour<5):
        GPIO.output(,1) #camera on
        os.system('/home/pi/program/pushbullet.sh "Alert Motion Detected."') #notification sent to phone and lappy about activity
    if(manual_override[cam]==1)
        input_unknown=False
"""
