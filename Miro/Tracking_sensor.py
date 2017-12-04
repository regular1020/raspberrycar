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

# =======================================================================
def getTracklist():
    '''
    이 함수는 5방향 센서의 값을 리스트로 만들어서 돌려주기만 한다.
    :return: 5방향 센서의 상태의 리스트.
    '''
    L2s = GPIO.input(setting.L2)
    L1s = GPIO.input(setting.L1)
    Cs = GPIO.input(setting.C)
    R1s = GPIO.input(setting.R1)
    R2s = GPIO.input(setting.R2)
    Tracklist = [L2s, L1s, Cs, R1s, R2s]

    return Tracklist
# =======================================================================
# =======================================================================
def getTrack():
    '''
    getTrack은 트렉의 상태를 판단하고 지금의 구동체의 위치를 리턴한다.
    이 함수는 아무 인자도 받지 않는다.
    '''
    L2s = GPIO.input(setting.L2)
    L1s = GPIO.input(setting.L1)
    Cs = GPIO.input(setting.C)
    R1s = GPIO.input(setting.R1)
    R2s = GPIO.input(setting.R2)
    Tracklist = [L2s, L1s, Cs, R1s, R2s]
    listcalc = ''

    if Tracklist == [1, 1, 0, 1, 1]:
        listcalc = 'center'
    elif Tracklist == [1, 0, 0, 0, 1]:
        listcalc = 'center'
    elif Tracklist == [1, 1, 0, 0, 1]:
        listcalc = 'sright'
    elif Tracklist == [1, 1, 1, 0, 1]:
        listcalc = 'sright'
    elif Tracklist == [1, 0, 0, 1, 1]:
        listcalc = 'sleft'
    elif Tracklist == [1, 0, 1, 1, 1]:
        listcalc = 'sleft'
    elif Tracklist == [1, 1, 0, 0, 0]:
        listcalc = 'right'
    elif Tracklist == [1, 1, 1, 0, 0]:
        listcalc = 'right'
    elif Tracklist == [1, 0, 0, 0, 0]:
        listcalc = 'right'
    elif Tracklist == [0, 0, 0, 0, 0]:
        listcalc = 'right'
    elif Tracklist == [0, 0, 0, 1, 1]:
        listcalc = 'left'
    elif Tracklist == [0, 0, 1, 1, 1]:
        listcalc = 'left'
    elif Tracklist == [0, 0, 0, 0, 1]:
        listcalc = 'left'
    elif Tracklist == [1, 1, 1, 1, 1]:
        listcalc = 'out'

    return listcalc

# ==========================================================================
if __name__ == "__main__":
    try:
        while True:
            print(getTrack())
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()

