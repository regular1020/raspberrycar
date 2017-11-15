from go_any import *
from Tracking_sensor import *
from ultrawave_sensor import *

try:
    LeftPwm.start(0)
    RightPwm.start(0)
    d = getDistance()
    print (d)
    s = getTrack()
    print (s)
    while (d > 18):
        d = getDistance()
        print (d)
        s = getTrack()
        print (s)
        linetrace(forward,s,43)
        time.sleep(0.001)
    time.sleep(1)
    PointTurn('right', 40, 0.7)
    time.sleep(1)
    go(forward, 40, 40, 1)
    time.sleep(1)
    PointTurn('left', 25, 1.5)
    time.sleep(1)
    s = getTrack()
    while (s == 6):
        go_any(forward,40,40)
        s = getTrack()
    time.sleep(1)
    go(forward, 30,40,0.5)
    PointTurn('right', 35, 1)
    d = getDistance()
    s = getTrack()
    while (d > 170):
        d = getDistance()
        print (d)
        s = getTrack()
        print (s)
        linetrace(forward,s,43)
        time.sleep(0.001)
    time.sleep(1)
    PointTurn('right', 40, 0.7)
    time.sleep(1)
    go(forward, 40, 40, 0.7)
    time.sleep(1)
    #PointTurn('left', 45, 1)
    go(forward, 40, 0, 1)
    s = getTrack()
    while (s == 6):
        go_any(forward, 30, 30)
        s = getTrack()
    time.sleep(1)
    PointTurn('right', 35, 1)
    while (d > 150):
        d = getDistance()
        print (d)
        s = getTrack()
        print (s)
        linetrace(forward,s,40)
        time.sleep(0.001)
except KeyboardInterrupt:
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # right motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    # GPIO pin setup has been cleared
    GPIO.cleanup()
# =======================================================================
