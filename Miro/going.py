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
def finding(speed):
    '''
    finding 함수는 라인트레이싱 하는 중에 만나는 교차로를 찾고 판단한다.
    :param track: getTrack을 통해 받은 값, Center, left, right, sleft, sright out이 있다.
    :param speed: 구동체의 속도 0~100의 값.
    '''
    s = Tracking_sensor.getTrack()
    if s == 'center':
        print(s)
        go_any(forward, speed, speed)
    elif s == 'sright':
        print(s)
        go_any(forward, speed*1.5, speed*0.8)
    elif s == 'sleft':
        print(s)
        go_any(forward, speed*0.8, speed*1.5)
    elif s == 'right':
        print(s)
        go_any(forward, speed, speed)
        time.sleep(0.3)
        PointTurn('right', speed)
        time.sleep(0.2)
        l = Tracking_sensor.getTracklist()
        while l[3] == 1:
            l = Tracking_sensor.getTracklist()
            PointTurn('right', speed*0.5)
        stop()
    elif s == 'left':
        print(s)
        go_any(forward, speed, speed)
        s = Tracking_sensor.getTrack()
        if s == 'out':
            PointTurn('left', speed)
            time.sleep(0.2)
            l = Tracking_sensor.getTracklist()
            while l[1] == 1:
                PointTurn('left', speed*0.5)
    elif s == 'out':
        print(s)
        l = Tracking_sensor.getTracklist()
        while l[3] == 1:
            l = Tracking_sensor.getTracklist()
            PointTurn('right', speed*0.5)



# =======================================================================

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
