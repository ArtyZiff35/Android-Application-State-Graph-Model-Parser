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
import numpy as np
from sklearn.linear_model import LogisticRegression


class activityStateDetector:
    ########## IMPORTANT VARIABLES ################
    topScreenLimitPercentage = 0.2  # 20% from top (considering 1920 pixels in height)
    middleScreenLimitPercentage = 0.6  # 60% center of screen
    activityTypeDictionary = {  # Dictionary to convert from number to string label
        1: "Todo",
        2: "Ad",
        3: "Login",
        4: "List",
        5: "Portal",
        6: "Browser",
        7: "Map",
        8: "Messages"
    }
    ###############################################

    @staticmethod
    def trainModel():
        # Reading X and Y vectors
        filehandler = open('./../savedKerasModels/X.dat', 'rb')
        X = pickle.load(filehandler)
        filehandler.close()
        filehandler = open('./../savedKerasModels/Y.dat', 'rb')
        Y = pickle.load(filehandler)
        filehandler.close()
        # Training the model
        # Instantiating the logistic Regression model
        logisticRegr = LogisticRegression(solver='newton-cg', multi_class='ovr')
        # Fitting the model
        logisticRegr.fit(X, Y)

        return logisticRegr


    @classmethod
    def detectActivity(cls, logisticRegr):
        # Setting the ViewClient's options
        kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': True}
        kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True,
                   'autodump': False, 'startviewserver': True, 'compresseddump': False}
        # Connecting to the Device
        device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)
        # Instatiation of the ViewClient for the selected Device: this is an interface for the device's views
        vc = ViewClient(device, serialno, **kwargs2)
        if vc.useUiAutomator:
            print "ViewClient: using UiAutomator backend"

        # Getting the screen size via adb shell command
        output = subprocess.check_output("adb shell dumpsys window | find \"width\"", shell=True)
        # Parsing the result in order to find the width
        matchResult = re.search("width=[0-9]+,", output)
        screenWidth = output[matchResult.start() + 6: matchResult.end() - 1]
        screenWidth = int(screenWidth)
        # Parsing the result in order to find the height
        matchResult = re.search("height=[0-9]+,", output)
        screenHeight = output[matchResult.start() + 7: matchResult.end() - 1]
        screenHeight = int(screenHeight)

        # Calculating the percentage of screen sections
        topScreenSection = int(cls.topScreenLimitPercentage * screenHeight)
        middleScreenSection = int(topScreenSection + (cls.middleScreenLimitPercentage * screenHeight))

        # Instantiation of the activityDataClass object and getting the activity name
        activityObject = activityDataClass(device.getTopActivityName())

        ##############-------------------#######################

        # Dumping the current view elements of the application
        print "\nDumping current application screen..."
        vc.dump(window='-1')
        elementToAttributesDictionary = {}
        for element in vc.viewsById:  # element is a string (uniqueID)
            # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
            elementAttributes = vc.viewsById[element].map
            # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
            elementToAttributesDictionary[elementAttributes['uniqueId']] = elementAttributes
            # Bounds of this specific UI elements are (startWidth, startHeight), (endWidth, endHeight)
            topHeight = elementAttributes['bounds'][0][1]
            bottomHeight = elementAttributes['bounds'][1][1]

            # Understanding in which section of the screen the element is located
            screenSection = 0
            activityObject.initializeFocusable()
            activityObject.initializeEnabled()
            activityObject.initializeImageViews()
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
                if elementAttributes['focusable'] == 'true':
                    activityObject.incrementnumFocusableTop()
                if elementAttributes['enabled'] == 'true':
                    activityObject.incrementnumEnabledTop()
                if elementAttributes['class'] == 'android.widget.ImageView':
                    activityObject.incrementnumImageViewsTop()
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
                if elementAttributes['focusable'] == 'true':
                    activityObject.incrementnumFocusableMid()
                if elementAttributes['enabled'] == 'true':
                    activityObject.incrementnumEnabledMid()
                if elementAttributes['class'] == 'android.widget.ImageView':
                    activityObject.incrementnumImageViewsMid()
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
                if elementAttributes['focusable'] == 'true':
                    activityObject.incrementnumFocusableBot()
                if elementAttributes['enabled'] == 'true':
                    activityObject.incrementnumEnabledBot()
                if elementAttributes['class'] == 'android.widget.ImageView':
                    activityObject.incrementnumImageViewsBot()
            # Doing last checks
            if elementAttributes['password'] == 'true':
                activityObject.incrementnumPassword()
            if elementAttributes['checkable'] == 'true':
                activityObject.incrementnumCheckable()
            # Incrementing the total number of UI elements for this activity
            activityObject.incrementnumTot()

        # Setting all the UI elements in the object for backup purposes
        activityObject.setAllUIElements(elementToAttributesDictionary)

        ##############-------------------#######################

        print "Preparing data for input array format"
        # Concatenating all metadata for the activity
        metaInputList = []
        tmpArray = []
        tmpArray.append(activityObject.numClickableTop)
        tmpArray.append(activityObject.numClickableMid)
        tmpArray.append(activityObject.numClickableBot)
        tmpArray.append(int(
            activityObject.numSwipeableTop + activityObject.numSwipeableMid + activityObject.numSwipeableBot))  # Adding the sum too
        tmpArray.append(activityObject.numEdittextTop)
        tmpArray.append(activityObject.numEdittextMid)
        tmpArray.append(activityObject.numEdittextBot)
        tmpArray.append(int(
            activityObject.numLongclickTop + activityObject.numLongclickMid + activityObject.numLongclickBot))  # Adding the sum too
        tmpArray.append(activityObject.numFocusableTop)
        tmpArray.append(activityObject.numFocusableMid)
        tmpArray.append(activityObject.numFocusableBot)
        tmpArray.append(int(
            activityObject.numImageViewsTop + activityObject.numImageViewsMid + activityObject.numImageViewsBot))  # Adding the sum too

        tmpArray.append(activityObject.numPassword)
        tmpArray.append(activityObject.numCheckable)
        tmpArray.append(activityObject.presentDrawer)
        tmpArray.append(activityObject.numTotElements)

        ##############-------------------#######################

        # Getting desired format
        metaInputList.append(tmpArray)
        # Converting to numpy arrays
        metaInputList = np.array(metaInputList)

        print "Predicting..."
        # Trying to predict
        predictedNumber = logisticRegr.predict(metaInputList)
        # Adding one to adjust numeric format
        predictedNumber = predictedNumber
        # Converting from number to string
        predictedCategory = cls.activityTypeDictionary[predictedNumber[0]]

        print "((( I predicted " + str(predictedCategory) + " )))"

        return predictedCategory