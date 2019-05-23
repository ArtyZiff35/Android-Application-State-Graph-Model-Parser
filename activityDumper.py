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
import enum
from activityDataClass import activityDataClass
import cv2
import time
import pickle



########## IMPORTANT VARIABLES ################
topScreenLimitPercentage = 0.2    # 20% from top (considering 1920 pixels in height)
middleScreenLimitPercentage = 0.6    # 60% center of screen
topScreenCropping = 65               # Pixels to crop on top of the screenshot
bottomScreenCropping = 127           # Pixels to crop on bottom of the screenshot
storePath = "./storedData/labeledActivities.dat"

class ActivityTypes(enum.Enum):     # Enumeration for screen section
    ToDo = 1
    Ad = 2
    Login = 3
    ListScreen = 4
    Portal = 5
    Browser = 6
    Map = 7
    Messages = 8

numCategories = 8
activityTypeDictionary = {
    1 : "Todo",
    2 : "Ad",
    3 : "Login",
    4 : "ListScreen",
    5 : "Portal",
    6 : "Browser",
    7 : "Map",
    8 : "Messages"
}

###############################################


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


# First of all, check if the stored file
labeledList = []
exists = os.path.isfile(storePath)
if exists:
    # If the file already exists, then load it
    with open(storePath, "rb") as fp:  # Unpickling
         labeledList = pickle.load(fp)
    print "[[ Loaded list with " + str(len(labeledList)) + " elements ]]"
else:
    # If the file does not exist yet, create the empty list
    labeledList = []
    print "[[ New list created ]]"

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


# Calculating the percentage of screen sections
topScreenSection = int(topScreenLimitPercentage * screenHeight)
middleScreenSection = int(topScreenSection + (middleScreenLimitPercentage * screenHeight))


# Instantiation of the activityDataClass object and getting the activity name
activityObject = activityDataClass( device.getTopActivityName() )

# Dumping the current view elements of the application
print "Dumping current application screen..."
vc.dump(window='-1')
elementToAttributesDictionary = {}
for element in vc.viewsById:    # element is a string (uniqueID)
    # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
    elementAttributes = vc.viewsById[element].map
    # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
    elementToAttributesDictionary[elementAttributes['uniqueId']] = elementAttributes
    # Bounds of this specific UI elements are (startWidth, startHeight), (endWidth, endHeight)
    topHeight = elementAttributes['bounds'][0][1]
    bottomHeight = elementAttributes['bounds'][1][1]

    # Understanding in which section of the screen the element is located
    screenSection = 0
    if bottomHeight <= topScreenSection:
        # Case of TOP SECTION of screen
        if elementAttributes['clickable'] == 'true':
            activityObject.incrementnumClickableTop()
        if elementAttributes['scrollable'] == 'true':
            activityObject.incrementnumSwipeableTop()
        if elementAttributes['class'] == 'android.widget.EditText':
            activityObject.incrementnumEdittextTop()
        if elementAttributes['long-clickable'] == 'true':
            activityObject.incrementnumLongclickTop()
    elif bottomHeight <= middleScreenSection:
        # Case of MIDDLE SECTION of screen
        if elementAttributes['clickable'] == 'true':
            activityObject.incrementnumClickableMid()
        if elementAttributes['scrollable'] == 'true':
            activityObject.incrementnumSwipeableMid()
        if elementAttributes['class'] == 'android.widget.EditText':
            activityObject.incrementnumEdittextMid()
        if elementAttributes['long-clickable'] == 'true':
            activityObject.incrementnumLongclickMid()
    else:
        # Case of BOTTOM SECTION of screen
        if elementAttributes['clickable'] == 'true':
            activityObject.incrementnumClickableBot()
        if elementAttributes['scrollable'] == 'true':
            activityObject.incrementnumSwipeableBot()
        if elementAttributes['class'] == 'android.widget.EditText':
            activityObject.incrementnumEdittextBot()
        if elementAttributes['long-clickable'] == 'true':
            activityObject.incrementnumLongclickBot()
    # Doing last checks
    if elementAttributes['password'] == 'true':
        activityObject.incrementnumPassword()
    if elementAttributes['checkable'] == 'true':
        activityObject.incrementnumCheckable()
    # Incrementing the total number of UI elements for this activity
    activityObject.incrementnumTot()

# Setting all the UI elements in the object for backup purposes
activityObject.setAllUIElements(elementToAttributesDictionary)

# Taking a screenshot
print "Done.\nCapturing Screenshot..."
device.takeSnapshot().save("./screenshots/screenshot.PNG", 'PNG')
loadedScreenshot = cv2.imread("./screenshots/screenshot.PNG")
# Converting the screenshot to grayscale
grayScreenshot = cv2.cvtColor(loadedScreenshot, cv2.COLOR_BGR2GRAY)
# Cropping the image to remove top and bottom system bars
croppedScreenshot = grayScreenshot[topScreenCropping:(screenHeight-bottomScreenCropping), 0:screenWidth]
# Rescaling the image to make it smaller (45% of original size)
smallerScreenshot = cv2.resize(croppedScreenshot, (0,0), fx=0.45, fy=0.45)
print "Screenshot resized to " + str(smallerScreenshot.shape)
# Setting that screenshot to the object
activityObject.setScreenshot(smallerScreenshot)
#cv2.imshow('image', activityObject.screenshot)
#cv2.waitKey()


# Requesting to the user to input the type of the recorded activity
print "Insert type of activity:\n\tToDo = 1\n\tAd = 2\n\tLogin = 3\n\tListScreen = 4\n\tPortal = 5\n\tBrowser = 6\n\tMap = 7\n\tMessages = 8\n"
userInput = 0
while True:
  try:
      userInput = int(input("Enter category number: "))
  except Exception:
      # Case of string
      print("Not an integer!")
      continue
  else:
      # Case of integer
      if userInput >=1 and userInput<=numCategories:
        print "You selected \'" + activityTypeDictionary[userInput] + "\'"
        activityObject.setLabel(activityTypeDictionary[userInput], userInput)
        break
      else:
        print "Number out of range"
        continue

# Adding the new object to the list
labeledList.append(activityObject)
# Saving the list to file
print "Saving list to file..."
with open(storePath, "wb") as fp:   #Pickling
    pickle.dump(labeledList, fp)
print "Done."


