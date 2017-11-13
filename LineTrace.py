from go_any import *
from Tracking_sensor import *
from ultrawave_sensor import *

try:
    LeftPwm.start(0)
    RightPwm.start(0)
    d = getDistance()
    while (d > 15):
        d = getDistance()
        print (d)
        s = getTrack()
        print (s)
        linetrace(forward,s)
    stop()
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
