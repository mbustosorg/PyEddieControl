'''
This is a script to 'drive' Eddie via keyboard input

Usage:
> python EddieDrive.py

*** NOTE ***
This script does not work within the Enthought Canopy environment.
It must be run from the command line via: python EddieDrive.py

It is also currently only works on Windows too, sorry.
'''

# WARNING # - Getch is a Windows only function.  Similar functionality
# is available on Linux/MacOS.
from getch import getch

import sys
from time import sleep

# This is the IP address for my Eddie, yours will probably be different
# OLD USAGE --> MyEddie = PyEddiePlus.EddiePlus("Edward","192.168.1.111")
import PyEddiePlus
MyEddie = PyEddiePlus.EddiePlus("Rafael")
MyEddie.FindEddie()
MyEddie.InitializeEddie()

print "Use a,d,w & x to drive Eddie"
print "Press q to Quit"
print 
sys.stdout.flush()

MaxSpeed = 10
MaxTurn = 6

SpeedVal = 0
TurnVal = 0
KeyPress = 's'

while KeyPress is not 'q':
    # Take keyboard input and issue appropriate commands to Eddie
    KeyPress = getch()

    if KeyPress == 'a':
        TurnVal -= 1
    elif KeyPress == 'd':
        TurnVal += 1
    elif KeyPress == 'w':
        SpeedVal += 1
    elif KeyPress == 'x':
        SpeedVal -= 1
    elif KeyPress == 's':
        SpeedVal = 0
        TurnVal = 0
    else:
        # Do nothing
        # Received a character other than an Eddie command
        print "Key Received: {0}".format(KeyPress)
        #pass
        
    # Limit the maximum speed
    if SpeedVal > MaxSpeed:
        SpeedVal = MaxSpeed
    
    if TurnVal > MaxTurn:
        TurnVal = MaxTurn
        
    print "Turn  = {0}".format(TurnVal)
    print "Speed = {0}".format(SpeedVal)

    MyEddie.Turn(TurnVal)
    MyEddie.Drive(SpeedVal)
    
    # Go through the loop at about 10Hz
    sleep(.05)

MyEddie.Disconnect()
        
print "Eddie is tired, he needs to rest now."
    


