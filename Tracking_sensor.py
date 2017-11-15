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
    
    L2s = GPIO.input(L2)
    L1s = GPIO.input(L1)
    Cs = GPIO.input(C)
    R1s = GPIO.input(R1)
    R2s = GPIO.input(R2)

    ### getTrack sensor the track and return each number to the circumstance
    ### return 0 : C off L2,L1,R1,R2 on
    ### return 1 : C,R1,L1 off L2,R2 on
    ### 0,1 means the car is on the correct direction
    ### return 2 : C,L1 off R1,R2,L2 on
    ### 2 means the car is slightly moved to the left
    ### return 3 : C,R1 off R2,L1,L2 on
    ### 3 means the car is slightly moved to the right
    ### return 4 : L2 off C on
    ### 4 means the car is completely moved to left
    ### return 5 : R2 off C on
    ### 5 means the car is completely moved to right
    ### return 6 : all on
    ### 6 means the car is completely out of track
    x = 0
    if Cs == 0:
        if L1s == 0:
            if R1s == 0:
                x = 1
            elif R1s == 1:
                x = 2
        elif L1s == 1:
            if R1s == 0:
                x = 3
        else:
            x = 0
    elif L1s == 0:
        x = 2
    elif R1s == 0:
        x = 3
    elif L2s == 0:
        x = 4
    elif R2s == 0:
        x = 5
    else:
        x = 6
    return x
# ==========================================================================
if __name__ == "__main__":
    try:
        while True:
            print(getTrack())
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()

