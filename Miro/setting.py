'''
name : setting.py
made by : 박정규
date : 2017/11/27
이 모듈은 구동체의 세팅을 한번에 모아서 실행하는 모듈이다.
'''

# import GPIO library
import RPi.GPIO as GPIO

# set GPIO warnings as flase
GPIO.setwarnings(False)
# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)
GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

L2 = 16
L1 = 18
C = 22
R1 = 40
R2 = 32

GPIO.setup(L2, GPIO.IN)
GPIO.setup(L1, GPIO.IN)
GPIO.setup(C, GPIO.IN)
GPIO.setup(R1, GPIO.IN)
GPIO.setup(R2, GPIO.IN)

trig = 33
echo = 31

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)
RightPwm = GPIO.PWM(MotorRight_PWM, 100)
