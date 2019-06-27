import subprocess
from com.dtmilano.android.viewclient import ViewClient, View, ViewClientOptions
from com.dtmilano.android.adb import adbclient
from com.dtmilano.android.common import debugArgsToDict


class testClass:

    # This class coincides with a test to execute (list of commands)
    def __init__(self, startingActivityType, sameDestination, endActivityType=None):
        # Saving the type of activity in which we have to execute the list of commands
        self.startingActivityType = startingActivityType
        # Saving whether the ending state after the commands are executed should be the same or not
        self.sameDestination = sameDestination
        # Initializing the list of commands to be executed for this test
        self.commandsList = []
        # Understanding whether we need to save a different destination activity type
        if sameDestination==False:
            self.endActivityType = endActivityType


    # Those must be function calls in string format!
    def appendCommandFunction(self, command):
        self.commandsList.append(command)




    ######################################################
    ######### LIST OF POSSIBLE COMMANDS ##################

    ### INIT FUNCTION TO SAVE THE DUMP ###
    def initDump(self):
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
        # Dumping
        vc.dump(window='-1')
        vc.sleep(1)
        elementToAttributesDictionary = {}
        for element in vc.viewsById:  # element is a string (uniqueID)
            # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
            elementAttributes = vc.viewsById[element].map
            # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
            elementToAttributesDictionary[elementAttributes['uniqueId']] = elementAttributes
        # Setting the class variable
        self.vc = vc
        self.elementToAttributesDictionary = elementToAttributesDictionary
        self.device = device


    ### LOGIN - TYPE 3 ###
    def loginInputName(self, inputName):
        success = False
        # Trying to find the 'name' field
        for element in self.elementToAttributesDictionary:
            # Finding out if this is an Edittext first
            if "edittext" in str(self.elementToAttributesDictionary[element]["class"]).lower():
                # Avoiding the password field
                if self.elementToAttributesDictionary[element]["password"]=="false":
                    # Finding the element and typing
                    address = self.vc.findViewByIdOrRaise(element)
                    address.type(inputName)
                    if self.device.isKeyboardShown():
                        self.device.press('KEYCODE_BACK')
                    success = True
        # Determining if we had success
        if success == True:
            print "Command OK!"
        else:
            print "Command NOT EXECUTED"

    def loginInputPassword(self, inputPassword):
        success = False
        # Trying to find the 'password' field
        for element in self.elementToAttributesDictionary:
            # Finding out if this is an Edittext first
            if "edittext" in str(self.elementToAttributesDictionary[element]["class"]).lower():
                # Finding the password field
                if self.elementToAttributesDictionary[element]["password"] == "true":
                    # Finding the element and typing
                    address = self.vc.findViewByIdOrRaise(element)
                    address.type(inputPassword)
                    if self.device.isKeyboardShown():
                        self.device.press('KEYCODE_BACK')
                    success = True
        # Determining if we had success
        if success == True:
            print "Command OK!"
        else:
            print "Command NOT EXECUTED"

    def clickNext(self):
        success = False
        # Trying to find the 'password' field
        for element in self.elementToAttributesDictionary:
            # Finding the button elements
            if "button" in str(self.elementToAttributesDictionary[element]["class"]).lower():
                # Checking that this is a 'next' button
                hints = ['login', 'log', 'signup', 'sign', 'create', 'next']
                text = str(self.elementToAttributesDictionary[element]["text"]).lower()
                for hint in hints:
                    if hint in text:
                        # Now we just have to find the element and click it
                        address = self.vc.findViewByIdOrRaise(element)
                        address.touch()
                        self.vc.sleep(1)
                        success = True

        # Determining if we had success
        if success == True:
            print "Command OK!"
        else:
            print "Command NOT EXECUTED"