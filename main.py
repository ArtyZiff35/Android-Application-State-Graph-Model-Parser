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

#TODO: Each line of the txt file corresponds to an entry of the dictionary vc.viewsById, which has as keys the UniqueIDs and as values the dictionary of attributes (e.g. vc.viewsById['id/no_id/14'])


################################
########## FUNCTIONS ###########

# Given a dump line, this function returns the name/value pair corresponding to the given argument string (needle)
def findPairContaining(originalStr = "", needle = ""):
    wordList = originalStr.split()
    for word in wordList:
        word = word.strip()
        if needle in word:
            return word
    return ""

# Given a dump line, this function returns the name/value pairs contained in it (all UI element's attributes)
def extractAttributesDictionaryFromDumpLine(dumpLine =""):
    # Get every field except for bound
    dictionary = {}
    wordList = dumpLine.split()
    for word in wordList:
        if '=' in word and 'bounds=' not in word:
            (name,value) = word.split("=",1)
            dictionary[name] = value
    # Bound field is discarded due to its different structure, so we need to find it manually now
    boundRegex = re.search("bounds.*\)\)", dumpLine)
    if boundRegex:
        found = boundRegex.group(0)
        if '=' in found:
            (name, value) = found.split("=")
            dictionary[name] = value

    return dictionary

# This function dumps the current view and transform it into a viewList
def dumpAndReturnViewList(vc):
    # Updating the dump for the current view: need to dump every time the view changes
    vc.dump(window='-1')
    # Printing the dump structure to output file
    myFileHandle = open("output.txt", "w+")
    transform = View.__str__  # This parameter tells the dump traverser to print all informations
    vc.traverse("ROOT", "", transform, myFileHandle)
    myFileHandle.close()

    # Parsing the saved dump into the viewList variable
    with open("output.txt", "r") as myFileHandle:
        line = myFileHandle.readline()
        viewList = []
        while line:
            viewList.append(line.strip())
            line = myFileHandle.readline()
    return viewList

# Generator used to get UI elements from a state queue until None is returned
def UIelementGenerator(state):
    while True:
        element = state.popUIelementToAnalyze()
        if element is None:
            break
        yield element

# This method moves from the root state to the argument state, following its roadmap
def traverseFromRootToState(startActivityName, finalState):
    print "---> Reaching state " + finalState.getStateName() + " from root " + startActivityName
    roadMapToFollow = finalState.getRoadMap()
    print "---> Following roadMap " + str(roadMapToFollow)
    device.startActivity(startActivityName)
    # Iterate through all UI elements necessary to reach that state from root
    vc.sleep(3)
    for element in roadMapToFollow:
        vc.dump(window='-1')
        if element != 'START':
            handle = vc.findViewWithAttributeOrRaise('uniqueId', element, "ROOT")
            (x, y) = handle.getXY()
            # Press it
            vc.touch(x, y)
            vc.sleep(3)


# This method tries to reduce the duplicate states
def shrinkStates(statesToExploreQueue, numAddedNewStates):
    # If we know the number of states added in the last iteration, we just need to check them
    numAdded = numAddedNewStates
    totLength = len(statesToExploreQueue)
    while numAdded > 0:
        # Finding the index of the state to check
        index = totLength - numAdded
        numAdded = numAdded - 1
        stateToConsider = statesToExploreQueue[index]
        # Checking if this state is in the 'completed list'
        toRemove = False
        for completed in statesCompletelyExplored:
            if completed.getAttributesDictionary() == stateToConsider.getAttributesDictionary():
                toRemove = True
                # Adjusting the children list for the father, which is now pointing to nothing
                fatherDictionary = stateToConsider.getFather().getOutgoingStateDictionary()
                for ui, state in fatherDictionary.items():
                    if state.getStateName() == stateToConsider.getStateName():
                        fatherDictionary[ui] = completed
                stateToConsider.getFather().updateOutgoingStateDictionary(fatherDictionary)
        # Checking if this state is in the 'still to explore list'
        if toRemove == False:
            for i in range(0, totLength):
                if i != index and statesToExploreQueue[i].getAttributesDictionary() == stateToConsider.getAttributesDictionary():
                    if i > index:
                        numAdded = numAdded - 1
                    toRemove = True
                    # Adjusting the children list for the father, which is now pointing to nothing
                    fatherDictionary = stateToConsider.getFather().getOutgoingStateDictionary()
                    for ui, state in fatherDictionary.items():
                        if state.getStateName() == stateToConsider.getStateName():
                            fatherDictionary[ui] = statesToExploreQueue[i]
                    stateToConsider.getFather().updateOutgoingStateDictionary(fatherDictionary)
        # Removing if necessary
        if toRemove == True:
            statesToExploreQueue.remove(stateToConsider)
            totLength = totLength - 1
            print '[[ REMOVED DUPLICATE STATE ' + stateToConsider.getStateName() + " ]]"
        else:
            print '[[ No duplicates were removed from queue ]]'
    return statesToExploreQueue

################################
################################


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


################################################################
print "################## Android OS VERSION TEST ####################"
# Starting an activity by its name
#device.startActivity('com.android.settings/.Settings')
#device.startActivity('com.google.android.apps.messaging/com.google.android.apps.messaging.ui.ConversationListActivity')
print 'Starting exploration...'

# Saving the name of the starting activity
startingActivityName = device.getFocusedWindowName()

# Preparing the initial START STATE of the application
vc.dump(window='-1')
elementToAttributesDictionary = {}
for element in vc.viewsById:    # element is a string (uniqueID)
    # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
    elementAttributes = vc.viewsById[element].map
    # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
    elementToAttributesDictionary[elementAttributes['uniqueId']] = elementAttributes
# Generating the Start State
startState = stateNode(['START'], elementToAttributesDictionary)


# Preparing the queue of state that we will analyze
statesToExploreQueue = []
statesCompletelyExplored = []
statesToExploreQueue.append(startState)
numAddedNewStates = 0

print 'Start state successfully generated and states queue initialized!'

# Main loop: keep going as long as we have new states to explore in our queue
while len(statesToExploreQueue) != 0:

    print "---------------------------------------------------"
    # Trying to reduce the number of states in the queue
    statesToExploreQueue = shrinkStates(statesToExploreQueue, numAddedNewStates)
    # Drawing graph chart
    gp.drawCurrentlyExploredNodes(statesCompletelyExplored)
    numAddedNewStates = 0
    # Pop a state
    currentState = statesToExploreQueue.pop(0)
    # Move from root to that state and update the dump to allow for button pressure
    traverseFromRootToState(startingActivityName, currentState)
    vc.sleep(6)
    # UPDATING THE UI ELEMENTS DICTIONARY FOR POPPED STATE
    vc.dump(window='-1')
    newDictionary = {}
    for element in vc.viewsById:  # element is a string (uniqueID)
        # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
        elementAttributes = vc.viewsById[element].map
        # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
        newDictionary[elementAttributes['uniqueId']] = elementAttributes
    currentState.updateAttributes(newDictionary)
    print '\nAnalyzing state ' + currentState.getStateName()


    while True: # This loop is necessary to keep retrying if UI elements are not found
        try:
            # Inner loop: keep going as long as we have UI elements still to explore
            for UiElement in UIelementGenerator(currentState):

                currentDictionary = currentState.getAttributesDictionary()
                # if currentDictionary[UiElement]['clickable'] == 'true' or currentDictionary[UiElement]['long-clickable'] == 'true' or currentDictionary[UiElement]['focusable'] == 'true' or currentDictionary[UiElement]['checkable'] == 'true':
                print '\nYet to analyze ' + str(currentState.getCurrentQueueLength()) + ' UI elements'
                # UiElement is the UniqueId of the UI element in question
                viewHandle = vc.findViewWithAttributeOrRaise('uniqueId', UiElement, "ROOT")
                (x, y) = viewHandle.getXY()
                # Press it
                print 'Pressing ' + str(UiElement)
                vc.touch(x, y)
                vc.sleep(6)

                # Now we MIGHT have ended in a new state...
                # First check if state has changed by dumping its content
                vc.dump(window='-1')
                newDictionary = {}
                for element in vc.viewsById:  # element is a string (uniqueID)
                    # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
                    elementAttributes = vc.viewsById[element].map
                    # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
                    newDictionary[elementAttributes['uniqueId']] = elementAttributes

                # Determine if the resulting state is new
                if newDictionary == currentState.getAttributesDictionary():
                    # Same State
                    print 'Still in same state'
                else:
                    # New State: generating it
                    newRoadMap = currentState.getRoadMap()
                    newRoadMap.append(UiElement)
                    newState = stateNode(newRoadMap, newDictionary, currentState)
                    # Insert it into the states queue
                    statesToExploreQueue.append(newState)
                    # Update the outgoing dictionary for the current state
                    currentState.addOutgoingState(UiElement, newState)
                    # Now go back to the 'current state'...
                    print 'NEW STATE: ' + newState.getStateName() + ' ||| Queue to explore size: ' + str(
                        len(statesToExploreQueue))
                    traverseFromRootToState(startingActivityName, currentState)
                    numAddedNewStates = numAddedNewStates + 1
                    vc.sleep(4)
                    vc.dump(window='-1')
            break
        except:
            print "+++ UI has changed and could not find an element. Trying again! +++"
            # UPDATING THE UI ELEMENTS DICTIONARY FOR POPPED STATE
            traverseFromRootToState(startingActivityName, currentState)
            vc.sleep(6)
            vc.dump(window='-1')
            newDictionary = {}
            for element in vc.viewsById:  # element is a string (uniqueID)
                # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
                elementAttributes = vc.viewsById[element].map
                # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
                newDictionary[elementAttributes['uniqueId']] = elementAttributes
            currentState.updateAttributes(newDictionary)
            print '\nAnalyzing state ' + currentState.getStateName()


    # We finished exploring the current state, so we put it into the 'completed list'
    statesCompletelyExplored.append(currentState)



















# Updating the dump for the current view: need to dump every time the view changes
vc.dump(window='-1')
# Printing the dump structure to output file
myFileHandle = open("output.txt","w+")
transform = View.__str__                            # This parameter tells the dump traverser to print all informations
vc.traverse("ROOT", "", transform, myFileHandle)
myFileHandle.close()

# Parsing the saved dump into the viewList variable
with open("output.txt","r") as myFileHandle:
    line = myFileHandle.readline()
    viewList = []
    while line:
        viewList.append(line.strip())
        line = myFileHandle.readline()


# Trying to press UI elements
previousActivity = device.getFocusedWindowName()
counter = 0
tot = len(viewList)
for viewElement in viewList:
    counter = counter + 1
    print "Touching element " + str(counter) + "/" + str(tot)
    # Extract all attributes for the current UI element
    elementAttributes = extractAttributesDictionaryFromDumpLine(viewElement)
    # Use its uniqueID to get an handle for it
    uniqueID = elementAttributes['uniqueId']
    viewHandle = vc.findViewWithAttributeOrRaise('uniqueId',uniqueID,"ROOT")
    (x,y) = viewHandle.getXY()
    # Press it
    vc.touch(x,y)
    vc.sleep(1)
    currentActivity = device.getFocusedWindowName()
    print currentActivity
    vc.sleep(2)
    # Press back if we ended up in a new activity
    if currentActivity != previousActivity:
        # Press back again if keyboard has come up
        if device.isKeyboardShown():
            subprocess.call("adb shell input keyevent KEYCODE_BACK", shell=True)
        if 'PopupWindow' in currentActivity:
            print "A popup with " + str(len(dumpAndReturnViewList(vc))) + " has been found!"
        subprocess.call("adb shell input keyevent KEYCODE_BACK", shell=True)
        vc.sleep(1)
    # If we end up with new screen items in the same activity
    elif dumpAndReturnViewList(vc) != viewList:
        print "Different screen!!!!"
    # Press back if the keyboard has come up but we're still in same search (search bar)
    if device.isKeyboardShown():
        subprocess.call("adb shell input keyevent KEYCODE_BACK", shell=True)

# Find a specific view from the dump of the view, get its coordinates, and touch them
foundButton = vc.findViewWithTextOrRaise("Battery","ROOT")
(x,y) = foundButton.getXY()
print device.getFocusedWindowName()
vc.touch(x,y)
vc.sleep(3)
print device.getFocusedWindowName()
# Pressing back button on OS bottom bar
subprocess.call("adb shell input keyevent KEYCODE_BACK",shell=True)
foundButton = vc.findViewWithTextOrRaise("Display","ROOT")
(x,y) = foundButton.getXY()
print device.getFocusedWindowName()
vc.touch(x,y)
vc.sleep(3)
print device.getFocusedWindowName()

