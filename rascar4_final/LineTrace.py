from go_any import *
from Tracking_sensor import *
from ultrawave_sensor import *

try:
    # 초기 셋팅
    LeftPwm.start(0)
    RightPwm.start(0)
    d = getDistance()
    s = getTrack()

    # 주행 시작
    while (d > 18):
        d = getDistance()
        print (d)
        s = getTrack()
        print (s)
        linetrace(forward,s,50)
        time.sleep(0.001)

    # 장애물 감지.
    avoid('left', 0.7, 40, 0.7, 40, 0.7, 40)
    s = getTrack()
    # 장애물 회피.
    while (s == 'out'):
        go_any(forward,40,40)
        s = getTrack()
    time.sleep(1)
    # 트랙으로 복귀

    d = getDistance()
    s = getTrack()
    while (d > 23):
        d = getDistance()
        print (d)
        s = getTrack()
        print (s)
        linetrace(forward,s,40)
        time.sleep(0.001)

    #장애물 감지.
    avoid('left', 0.7, 40, 0.7, 40, 0.7, 40)
    s = getTrack()
    #장애물 회피.
    while (s == 'out'):
        go_any(forward, 40, 40)
        s = getTrack()
    time.sleep(1)
    # 트랙으로 복귀
    s = getTrack()
    while (True):
        s = getTrack()
        linetrace(forward,s,40)
        time.sleep(0.001)
        if (s == 'Last'):
            break
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
