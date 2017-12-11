'''
name : Tracking_sensor.py
made by : 박정규
date : 2017/11/27
이 모듈은 5 방향 센서를 이용해 트렉에서 구동체의 위치를 인식하는 펑션 getTrack을 포함한다.
'''
# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import time
import setting

L2s = GPIO.input(setting.L2)
L1s = GPIO.input(setting.L1)
Cs = GPIO.input(setting.C)
R1s = GPIO.input(setting.R1)
R2s = GPIO.input(setting.R2)
Tracklist = [L2s, L1s, Cs, R1s, R2s]
# =======================================================================

# =======================================================================
def goingtrack():
    '''
    이 함수는 5 방향 센서중, 직진에 관한 센서 가운데 3개의 값을 리스트로 반들어서 돌려준다.
    :return: 5방향 센서의 상태에 관한 문자열.
    '''
    L2s = GPIO.input(setting.L2)
    L1s = GPIO.input(setting.L1)
    Cs = GPIO.input(setting.C)
    R1s = GPIO.input(setting.R1)
    R2s = GPIO.input(setting.R2)

    Tracklist = [L2s, L1s, Cs, R1s, R2s]
    return Tracklist
# ==========================================================================
if __name__ == "__main__":
    try:
        while True:
            print(getTrack())
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()

