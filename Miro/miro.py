import RPi.GPIO as GPIO
import going
import setting
import time

try:
    # 초기 셋팅
    setting.LeftPwm.start(0)
    setting.RightPwm.start(0)
    while True:
        going.finding(30)
        time.sleep(0.1)

except KeyboardInterrupt:
    # the speed of left motor will be set as LOW
    GPIO.output(setting.MotorLeft_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    setting.LeftPwm.ChangeDutyCycle(0)
    # the speed of right motor will be set as LOW
    GPIO.output(setting.MotorRight_PWM, GPIO.LOW)
    # right motor will be stopped with function of ChangeDutyCycle(0)
    setting.RightPwm.ChangeDutyCycle(0)
    # GPIO pin setup has been cleared
    GPIO.cleanup()
# =======================================================================
