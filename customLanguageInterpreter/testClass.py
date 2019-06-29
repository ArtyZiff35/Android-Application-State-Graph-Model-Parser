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
        # Initializing dictionary
        self.startingElementToAttributesDictionary = None


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
        self.startingElementToAttributesDictionary = elementToAttributesDictionary
        self.device = device


    ### FINAL FUNCTION TO CHECK THE STATE WHERE WE ARE ARRIVED
    def finalStateCheck(self):
        # Dumping for the final state
        self.vc.dump(window='-1')
        self.vc.sleep(1)
        elementToAttributesDictionary = {}
        for element in self.vc.viewsById:  # element is a string (uniqueID)
            # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
            elementAttributes = self.vc.viewsById[element].map
            # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
            elementToAttributesDictionary[elementAttributes['uniqueId']] = elementAttributes

        # Finally comparing the current dump with the one of the initial state
        if elementToAttributesDictionary == self.startingElementToAttributesDictionary:
            return "SAME"
        else:
            # TODO: Here we would check which type of state is this and return its type
            return "DIFFERENT"

    ### TODO - TYPE 1 ###
    def todoAddNewNote(self, inputNoteTitle):
        success = False
        # Trying to find an Image button (generally the "add note button" is a fab in the bottom of the screen)
        for element in self.startingElementToAttributesDictionary:
            if "imagebutton" in str(self.startingElementToAttributesDictionary[element]["class"]).lower():
                if self.startingElementToAttributesDictionary[element]["clickable"] == "true":
                    # Now we need to find some keywords that are generally hidden in the resource id of the element
                    hints = ['fab', 'add', 'new', 'create', 'write']
                    text = str(self.startingElementToAttributesDictionary[element]["resource-id"]).lower()
                    for hint in hints:
                        if hint in text:
                            # We have found the right "add note button", therefore click it
                            address = self.vc.findViewByIdOrRaise(element)
                            address.touch()
                            if self.device.isKeyboardShown():
                                self.device.press('KEYCODE_BACK')
                            self.vc.sleep(2)
                            success = True
                            break

        # If everything went ok up to now, find an EditText where to write the note title
        if success == True:
            success = False
            # Dumping
            self.vc.dump(window='-1')
            self.vc.sleep(1)
            elementToAttributesDictionary = {}
            for element in self.vc.viewsById:  # element is a string (uniqueID)
                # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
                elementAttributes = self.vc.viewsById[element].map
                # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
                elementToAttributesDictionary[elementAttributes['uniqueId']] = elementAttributes
            # Find an edittext
            for element in elementToAttributesDictionary:
                if "edittext" in str(elementToAttributesDictionary[element]["class"]).lower():
                    # Finding some hints
                    hints = ['task', 'title', 'name']
                    text = str(elementToAttributesDictionary[element]["text"]).lower()
                    for hint in hints:
                        if hint in text:
                            # Finding the element and typing
                            address = self.vc.findViewByIdOrRaise(element)
                            address.type(inputNoteTitle)
                            if self.device.isKeyboardShown():
                                self.device.press('KEYCODE_BACK')
                            success = True
                            self.vc.sleep(2)
                            break
        # Now that we have added the note, we need to press "next" button
        if success == True:
            success = False
            # Dumping
            self.vc.dump(window='-1')
            self.vc.sleep(1)
            elementToAttributesDictionary = {}
            for element in self.vc.viewsById:  # element is a string (uniqueID)
                # Getting the dictionary of attributes for this specific UI element ('attribute name -> value')
                elementAttributes = self.vc.viewsById[element].map
                # Adding that to the general dictionary for all UI elements of this state ('UI element -> attributes dictionary')
                elementToAttributesDictionary[elementAttributes['uniqueId']] = elementAttributes
            # Find an edittext
            for element in elementToAttributesDictionary:
                if elementToAttributesDictionary[element]["clickable"] == "true":
                    # Finding some hints
                    hints = ['add', 'next']
                    text = str(elementToAttributesDictionary[element]["text"]).lower()
                    for hint in hints:
                        if hint in text:
                            # We have found the right "add note button", therefore click it
                            address = self.vc.findViewByIdOrRaise(element)
                            address.touch()
                            self.vc.sleep(1)
                            success = True
                            break
        # Determining if we had success
        if success == True:
            print "Command OK!"
            return True
        else:
            print "Command NOT EXECUTED"
            return False

    ### LOGIN - TYPE 3 ###
    def loginInputName(self, inputName):
        success = False
        # Trying to find the 'name' field
        for element in self.startingElementToAttributesDictionary:
            # Finding out if this is an Edittext first
            if "edittext" in str(self.startingElementToAttributesDictionary[element]["class"]).lower():
                # Avoiding the password field
                if self.startingElementToAttributesDictionary[element]["password"]== "false":
                    # Finding the element and typing
                    address = self.vc.findViewByIdOrRaise(element)
                    address.type(inputName)
                    if self.device.isKeyboardShown():
                        self.device.press('KEYCODE_BACK')
                    success = True
        # Determining if we had success
        if success == True:
            print "Command OK!"
            return True
        else:
            print "Command NOT EXECUTED"
            return False

    def loginInputPassword(self, inputPassword):
        success = False
        # Trying to find the 'password' field
        for element in self.startingElementToAttributesDictionary:
            # Finding out if this is an Edittext first
            if "edittext" in str(self.startingElementToAttributesDictionary[element]["class"]).lower():
                # Finding the password field
                if self.startingElementToAttributesDictionary[element]["password"] == "true":
                    # Finding the element and typing
                    address = self.vc.findViewByIdOrRaise(element)
                    address.type(inputPassword)
                    if self.device.isKeyboardShown():
                        self.device.press('KEYCODE_BACK')
                    success = True
        # Determining if we had success
        if success == True:
            print "Command OK!"
            return True
        else:
            print "Command NOT EXECUTED"
            return False

    def clickNext(self):
        success = False
        # Trying to find the 'password' field
        for element in self.startingElementToAttributesDictionary:
            # Finding the button elements
            if "button" in str(self.startingElementToAttributesDictionary[element]["class"]).lower():
                # Checking that this is a 'next' button thanks to some hint words
                hints = ['login', 'log', 'signup', 'sign', 'create', 'next']
                text = str(self.startingElementToAttributesDictionary[element]["text"]).lower()
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
            return True
        else:
            print "Command NOT EXECUTED"
            return False