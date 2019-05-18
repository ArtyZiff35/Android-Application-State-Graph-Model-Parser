import re
import sys
import time
import os
import subprocess
from com.dtmilano.android.viewclient import ViewClient, View, ViewClientOptions
from com.dtmilano.android.adb import adbclient
from com.dtmilano.android.common import debugArgsToDict
from stateNode import stateNode
import graphPlotter as gp
from matplotlib.image import imread




########## IMPORTANT VARIABLES
topScreenLimit = 384    # 20% from top (considering 1920 pixels in height)
middleScreenLimit = 1536    # 60% center of screen


# Setting the ViewClient's options
kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': True}
kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': False}
# Connecting to the Device
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)
# Instatiation of the ViewClient for the selected Device: this is an interface for the device's views
vc = ViewClient(device, serialno, **kwargs2)
if vc.useUiAutomator:
    print "ViewClient: using UiAutomator backend"
    #device.dumpsys()



# Getting the screen size via adb shell command
output = subprocess.check_output("adb shell dumpsys window | find \"width\"", shell=True)
# Parsing the result in order to find the width
matchResult = re.search("width=[0-9]+,", output)
screenWidth = output[matchResult.start()+6 : matchResult.end()-1]
screenWidth = int(screenWidth)
# Parsing the result in order to find the height
matchResult = re.search("height=[0-9]+,", output)
screenHeight = output[matchResult.start()+7 : matchResult.end()-1]
screenHeight = int(screenHeight)

# Dumping the current view elements of the application
print "Dumping current application screen"
vc.dump(window='-1')
elementToAttributesDictionary = {}
for element in vc.viewsById:    # element is a string (uniqueID)
    # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
    elementAttributes = vc.viewsById[element].map
    # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
    elementToAttributesDictionary[elementAttributes['uniqueId']] = elementAttributes
    # Bounds are (startWidth, startHeight), (endWidth, endHeight)
    topHeight = elementAttributes['bounds'][0][1]
    bottomHeight = elementAttributes['bounds'][1][1]

# Taking a screenshot
device.takeSnapshot().save("./screenshots/screenshot.PNG", 'PNG')
loadedScreenshot = imread("./screenshots/screenshot.PNG")
