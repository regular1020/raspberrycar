######################################################################
### Date: 2017/11/13
### file name: go_any.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to do straight move
######################################################################

# import GPIO library
import RPi.GPIO as GPIO
import time

from Tracking_sensor2 import *

# set GPIO warnings as flase
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

# ======================================================================
# set the forward and backward as True and False
#=======================================================================
forward = True
backward = False

# =======================================================================
# declare the pins of 12, 11, 35 in the Rapberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Rapberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled
# =======================================================================
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# ===========================================================================

# ===========================================================================
def Setleftmotor(direction):
    # Set rightmotor ready to move
    # direction is True if you want to move forward
    # direction is False if you want to move backward
    if direction == True:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif direction == False:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    else:
        print
        'Config Error'


# ===========================================================================

# ===========================================================================
def Setrightmotor(direction):
    # Set rightmotor ready to move
    # direction is True if you want to move forward
    # direction is False if you want to move backward
    if direction == True:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    elif direction == False:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    else:
        print
        'config Error'


# ===========================================================================
# ===========================================================================
# because the connetions between motors (left motor) and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# ===========================================================================

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

# ===========================================================================
# because the connetions between motors (right motor) and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# ===========================================================================

GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
# =======================================================================
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)

# =======================================================================
# create right pwm object to control the speed of right motor
# =======================================================================
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


# =======================================================================
#  go_any method has been generated for the three-wheeled moving
#  objec to move for the direction without any limitation of running_time
#  direction is forward or backward
def go_any(direction, Rspeed, Lspeed):
    # set the left and right motor to go to the selected direction.
    Setleftmotor(direction)
    Setrightmotor(direction)

    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go
    LeftPwm.ChangeDutyCycle(Lspeed)
    # set the speed of the right motor to go
    RightPwm.ChangeDutyCycle(Rspeed)


# =======================================================================

# =======================================================================
# define the forward module
# forward has the parameters of speed and running_time
def go(direction, Rspeed, Lspeed, running_time):
    # set the left motor to go to the selected direction.
    Setleftmotor(direction)
    Setrightmotor(direction)

    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go
    LeftPwm.ChangeDutyCycle(Lspeed)
    # set the speed of the right motor to go
    RightPwm.ChangeDutyCycle(Rspeed)
    # set the running time of the left motor to go
    time.sleep(running_time)


# =======================================================================
# =======================================================================
def PointTurn(direction, speed, running_time):
    if direction == 'left':
        # set the left motor to move backward
        Setleftmotor(False)

        # set the left motor pwm to be ready to go backward
        GPIO.output(MotorLeft_PWM, GPIO.HIGH)

        # set the right motor to move forward
        Setrightmotor(True)

        # set the right motor pwm to be ready to go forward
        GPIO.output(MotorRight_PWM, GPIO.HIGH)

        # set the speed of the left motor to go backward
        LeftPwm.ChangeDutyCycle(speed)
        # set the speed of the right motor to go forward
        RightPwm.ChangeDutyCycle(speed)
        # set the running time of the point turn
        time.sleep(running_time)

    elif direction == 'right':
        # set the left motor to move forward
        Setleftmotor(True)

        # set the left motor pwm to be ready to go forward
        GPIO.output(MotorLeft_PWM, GPIO.HIGH)

        # set the right motor to move backward
        Setrightmotor(False)

        # set the right motor pwm to be ready to go backward
        GPIO.output(MotorRight_PWM, GPIO.HIGH)

        # set the speed of the left motor go to forward
        LeftPwm.ChangeDutyCycle(speed)
        # set the speed of the right motor to go backward
        RightPwm.ChangeDutyCycle(speed)
        # set the running time of the point turn
        time.sleep(running_time)


# =======================================================================
# =======================================================================
def linetrace(direction, track, speed):
    ### 이동방향, 트랙의 상태, 속도를 인자로 받는다.
    ### 현재 자동차의 트랙상의 위치에 따라 자동차가 트랙의 가운데로 올 수 있도록 주행, 보정 해준다.
    if track == 'Center':
        go_any(direction, speed*1.3, speed*1.3)
    elif track == 'Left':
        go_any(direction, speed*0.7, speed)
    elif track == 'Right':
        go_any(direction, speed, speed*0.7)
    elif track == 'MostLeft':
        go_any(direction, speed*0.5, speed*2)
    elif track == 'MostRight':
        go_any(direction, speed*2, speed*0.5)
    elif track == 'Out':
        go_any(direction, speed, speed*0.1)
    elif track == 'Last':
        stop()
# ========================================================================
# =======================================================================
def avoid(direction, fttime, ftspeed, gotime, gospeed, sttime, stspeed):
    ### 회전방항, 첫번째 회전의 시간,속도, 직진의 시간,속도, 두번째 회전의 시간, 속도를 인자로 받는다.
    ### 회전방향대로 첫번째 회전의 조건대로 회전을 받고, 두번째 직진 시간만큼 직진 한 뒤, 두번째 회전의 조건대로 회전을 실행한다.
    if direction == 'right':
        PointTurn('right', ftspeed, fttime)
        go(forward, gospeed, gospeed, gotime)
        stop()
        time.sleep(1)
        PointTurn('left', stspeed, sttime)
    elif direction == 'left':
        PointTurn('left', ftspeed, fttime)
        go(forward, gospeed, gospeed, gotime)
        stop()
        time.sleep(1)
        PointTurn('rigt', stspeed, sttime)
# =======================================================================
# =======================================================================
def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
# =======================================================================
def pwm_setup():
    LeftPwm.start(0)
    RightPwm.start(0)


def pwm_low():
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    LeftPwm.ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()
