'''
name: going.py
made by 박정규.
edited by 박정규, 남경태, 박태범.
Date : 2017/11/29

이 모듈은 구동체의 움직임에 관한 함수들을 모아놓은 모듈이다.
'''

# import GPIO library
import RPi.GPIO as GPIO
import time
import setting
import Tracking_sensor

# ======================================================================
# set the forward and backward as True and False
#=======================================================================
forward = True
backward = False

# ===========================================================================
def Setleftmotor(direction):
    '''
    Setleftmotor 함수는 왼쪽 모터의 회전방향을 정해준다.
    :param direction: forward or backward.
    '''
    if direction == True:
        GPIO.output(setting.MotorLeft_A, GPIO.HIGH)
        GPIO.output(setting.MotorLeft_B, GPIO.LOW)
    elif direction == False:
        GPIO.output(setting.MotorLeft_A, GPIO.LOW)
        GPIO.output(setting.MotorLeft_B, GPIO.HIGH)
    else:
        print
        'Config Error'
# ===========================================================================

# ===========================================================================
def Setrightmotor(direction):
    '''
    SetRightmotor 함수는 오른쪽 모터의 회전방향을 정해준다.
    :param direction: forward or backward.
    '''
    if direction == True:
        GPIO.output(setting.MotorRight_A, GPIO.LOW)
        GPIO.output(setting.MotorRight_B, GPIO.HIGH)
    elif direction == False:
        GPIO.output(setting.MotorRight_A, GPIO.HIGH)
        GPIO.output(setting.MotorRight_B, GPIO.LOW)
    else:
        print
        'config Error'
# ===========================================================================

# =======================================================================
def go_any(direction, Rspeed, Lspeed):
    '''
    go_any 함수는 주어진 방향과 속도로 구동체를 이동시키는 역할을 한다.
    :param direction: forward or backward
    :param Rspeed: 0~100, rightmotorspeed
    :param Lspeed: 0~100, leftmotorspeed
    '''
    Setleftmotor(direction)
    Setrightmotor(direction)

    GPIO.output(setting.MotorLeft_PWM, GPIO.HIGH)
    GPIO.output(setting.MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go
    setting.LeftPwm.ChangeDutyCycle(Lspeed)
    # set the speed of the right motor to go
    setting.RightPwm.ChangeDutyCycle(Rspeed)
# =======================================================================

# =======================================================================
def PointTurn(direction, speed):
    '''
    PointTurn함수는 주어진 방향, 속도로 회전을 시키는 역할을 한다.
    :param direction: 'left' or 'right'
    :param speed: 0~100
    '''
    if direction == 'left':
        # set the left motor to move backward
        Setleftmotor(False)

        # set the left motor pwm to be ready to go backward
        GPIO.output(setting.MotorLeft_PWM, GPIO.HIGH)

        # set the right motor to move forward
        Setrightmotor(True)

        # set the right motor pwm to be ready to go forward
        GPIO.output(setting.MotorRight_PWM, GPIO.HIGH)

        # set the speed of the left motor to go backward
        setting.LeftPwm.ChangeDutyCycle(speed)
        # set the speed of the right motor to go forward
        setting.RightPwm.ChangeDutyCycle(speed)


    elif direction == 'right':
        # set the left motor to move forward
        Setleftmotor(True)

        # set the left motor pwm to be ready to go forward
        GPIO.output(setting.MotorLeft_PWM, GPIO.HIGH)

        # set the right motor to move backward
        Setrightmotor(False)

        # set the right motor pwm to be ready to go backward
        GPIO.output(setting.MotorRight_PWM, GPIO.HIGH)

        # set the speed of the left motor go to forward
        setting.LeftPwm.ChangeDutyCycle(speed)
        # set the speed of the right motor to go backward
        setting.RightPwm.ChangeDutyCycle(speed)
# =======================================================================
# =======================================================================
def lineTrace(speed):
    t = Tracking_sensor.goingtrack()
    print (t)
    if not t[2] and not t[4]:
        stop()
        go_any(forward,speed,speed)
        time.sleep(0.4)
        PointTurn('right', speed)
        time.sleep(0.5)
        while Tracking_sensor.goingtrack()[3]:
            continue
        stop()
    elif t[1] and not t[2] and t[3]:
        go_any(forward,speed,speed)
    elif not t[1]:
        go_any(forward,speed,speed/3)
    elif not t[3]:
        go_any(forward,speed/3,speed)
    elif t == [1,1,1,1,1]:
        stop()
        time.sleep(0.5)
        PointTurn('left', speed)
        while Tracking_sensor.goingtrack()[3]:
            continue
        stop()
    time.sleep(0.1)

# =======================================================================
def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(setting.MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(setting.MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    setting.LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    setting.RightPwm.ChangeDutyCycle(0)
# =======================================================================
def pwm_setup():
    setting.LeftPwm.start(0)
    setting.RightPwm.start(0)


def pwm_low():
    GPIO.output(setting.MotorLeft_PWM, GPIO.LOW)
    GPIO.output(setting.MotorRight_PWM, GPIO.LOW)
    setting.LeftPwm.ChangeDutyCycle(0)
    setting.RightPwm.ChangeDutyCycle(0)
    GPIO.cleanup()
