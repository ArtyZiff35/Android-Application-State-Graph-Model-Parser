from com.dtmilano.android.viewclient import ViewClient, View, ViewClientOptions
from com.dtmilano.android.adb import adbclient
from com.dtmilano.android.common import debugArgsToDict
import subprocess
from subprocess import check_output
import psutil
import os
import time
import sys


# Method to kill a process
def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

def getTimestamp(line):
    return float(line.split()[1][:-1])

# Instantiating the output file
shellFileName = "./outputFiles/out.txt"

# outFile = open(shellFileName, 'w')
# # Calling ADB shell
# proc = subprocess.Popen(["adb", "shell"],stdin=subprocess.PIPE, stdout=outFile, stderr=outFile)
# # Asking for the getevent util
# proc.stdin.write("getevent -l /dev/input/event1")
# proc.stdin.write("\n")
# proc.stdin.flush()
# print "\nRecording..."
# # Managing main loop
# while True:
#     userInput = str(raw_input("To stop recording, type 'q': "))
#     print userInput
#     if userInput=='q' or userInput=='Q':
#         break
# # Stopping the recording subprocess
# print "Stopped Recording!"
# kill(proc.pid)
# outFile.flush()
# outFile.close()


# Preparing the output script
outputScriptName = "./outputFiles/outputScript.txt"
outputScriptFile = open(outputScriptName, "w")

# Writing headers
outputScriptFile.write("When VIDEO app:\nIN PORTAL check for SAME state:\n")


# Now reading the output of the shell
line = "XXX"
status = "XXX"
initialTime = 0
finalTime = 0
initialX = 0
initialY = 0
currentX = 0
currentY = 0
with open(shellFileName) as fp:
    while line:
        # Reading a line
        line = fp.readline()
        # Entering a new input event
        if "ABS_MT_TRACKING_ID" in line:
            if "00000000" in line:
                # Pressing down
                initialTime = getTimestamp(line)
                status = "DOWN"
                initialX = 0
                initialY = 0
                # Understanding whether we need to introduce a sleep
                if finalTime!=0:
                    delta = (initialTime - finalTime)
                    finalTime = 0
                    # Writing command to file
                    outputScriptFile.write("\tCUSTOM SLEEP " + str(delta*1000) + " ;\n")
                    print "INTRODUCED PAUSE OF " + str(delta) + " secs"
                print "PRESSING"
            elif "ffffffff" in line:
                # Releasing press
                finalTime = getTimestamp(line)
                delta = (finalTime - initialTime)
                status = "UP"
                # Writing command to file
                outputScriptFile.write("\tCUSTOM DRAG FROM " + str(initialX) + " " + str(initialY) + " TO " + str(currentX) + " " + str(currentY) + " DURATION " + str(delta*1000) + " ;\n")
                print "RELEASING after " + str(delta) + " secs"
        # Entering a coordinates change
        elif "ABS_MT_POSITION_X" in line:
            # Converting from hex to decimal
            hex = line.split()[-1]
            currentX = int(hex, 16)
            currentX = currentX/30.34
            if initialX == 0:
                initialX = currentX
            print "X: " + str(currentX)
        elif "ABS_MT_POSITION_Y" in line:
            hex = line.split()[-1]
            currentY = int(hex, 16)
            currentY = currentY/17.07
            if initialY == 0:
                initialY = currentY
            print "Y: " + str(currentY)


outputScriptFile.flush()
outputScriptFile.close()

