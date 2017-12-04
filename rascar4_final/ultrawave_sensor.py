######################################################################
### Date: 2017/11/13
### file name: ultrawave_sensor.py
### Purpose: this code has generated for the return
###         the distance between the moving object and obstacle
###         ultra sensor
######################################################################


import RPi.GPIO as GPIO # import GPIO librery
import time

GPIO.setmode(GPIO.BOARD)

trig=33
echo=31

#ultrasonic sensor setting
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def getDistance():
    ### 거리를 구하기 위한 함수.
    GPIO.output(trig,False)
    time.sleep(0.5)
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
    while GPIO.input(echo)==0:
        pulse_start=time.time()
    while GPIO.input(echo)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17000
    distance=round(distance,2)
    return distance