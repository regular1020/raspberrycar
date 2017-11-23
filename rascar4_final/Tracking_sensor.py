#########################################################################
### Date: 2017/11/13
### file name: Tracking_sensor.py
### Purpose: this code has been generated for the five-way tracking sensor
###         to perform the decision of direction
###
#########################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import time

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)

# =======================================================================
# declare the pins of 16, 18, 22, 40, 32 in the Rapberry Pi
# as the control pins of 5-way trackinmg sensor in order to
# control direction
#
#  L2    L1     C     R1     R2
#  16    18     22    40     32
#
# led turns on (1) : trackinmg sensor led detects white playground
# led turns off(0) : trackinmg sensor led detects black line

# L2 off : it means that moving object finds black line
#                   at the position of L2
#                   black line locates below the L2 of the moving object
#
# L1 off : it means that moving object finds black line
#                   at the position of L1
#                   black line locates below the L1 of the moving object
#
# C off : it means that moving object finds black line
#                   at the position of C
#                   black line locates below the C of the moving object
#
# R1 off : it means that moving object finds black line
#                   at the position of R1
#                   black line locates below the R1  of the moving object
#
# R2 off : it means that moving object finds black line
#                   at the position of R2
#                   black line locates below the R2 of the moving object
# =======================================================================

L2 = 16
L1 = 18
C = 22
R1 = 40
R2 = 32

# =======================================================================
# because the connetions between 5-way tracking sensor and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared whether their roles of pins
# are output pin or input pin
# since the 5-way tracking sensor data has been detected and
# used as the input data, leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared as input
#
# =======================================================================

GPIO.setup(L2, GPIO.IN)
GPIO.setup(L1, GPIO.IN)
GPIO.setup(C, GPIO.IN)
GPIO.setup(R1, GPIO.IN)
GPIO.setup(R2, GPIO.IN)


# =======================================================================
# GPIO.input(leftmostled) method gives the data obtained from leftmostled
# leftmostled returns (1) : leftmostled detects white playground
# leftmostled returns (0) : leftmostled detects black line
#
#
# GPIO.input(leftlessled) method gives the data obtained from leftlessled
# leftlessled returns (1) : leftlessled detects white playground
# leftlessled returns (0) : leftlessled detects black line
#
# GPIO.input(centerled) method gives the data obtained from centerled
# centerled returns (1) : centerled detects white playground
# centerled returns (0) : centerled detects black line
#
# GPIO.input(rightlessled) method gives the data obtained from rightlessled
# rightlessled returns (1) : rightlessled detects white playground
# rightlessled returns (0) : rightlessled detects black line
#
# GPIO.input(rightmostled) method gives the data obtained from rightmostled
# rightmostled returns (1) : rightmostled detects white playground
# rightmostled returns (0) : rightmostled detects black line
#
# =======================================================================

# =======================================================================
def getTrack():
    ### 아무 인자도 받지 않는 함수이다.
    ### 자동차의 5방향 추적센서의 상태를 리스트로 받고, 자동차의 위치 정보를 알려준다.
    L2s = GPIO.input(L2)
    L1s = GPIO.input(L1)
    Cs = GPIO.input(C)
    R1s = GPIO.input(R1)
    R2s = GPIO.input(R2)
    Tracklist = [L2s, L1s, Cs, R1s, R2s]
    listcalc = ''

    if Tracklist == [0, 0, 0, 0, 0]:
        listcalc = 'Last'
    elif Tracklist == [1, 1, 0, 1, 1]:
        listcalc = 'Center'
    elif Tracklist == [1, 0, 0, 0, 1]:
        listcalc = 'Center'
    elif Tracklist == [1, 0, 0, 1, 1]:
        listcalc = 'Left'
    elif Tracklist == [1, 1, 0, 0, 1]:
        listcalc = 'Right'
    elif Tracklist == [1, 0, 1, 1, 1]:
        listcalc = 'Left'
    elif Tracklist == [1, 1, 1, 0, 1]:
        listcalc = 'Right'
    elif Tracklist[0] == 0:
        listcalc = 'MostLeft'
    elif Tracklist[4] == 0:
        listcalc = 'MostRight'
    elif Tracklist == [1, 1, 1, 1, 1]:
        listcalc = 'Out'

    return listcalc
# ==========================================================================
if __name__ == "__main__":
    try:
        while True:
            print(getTrack())
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()

