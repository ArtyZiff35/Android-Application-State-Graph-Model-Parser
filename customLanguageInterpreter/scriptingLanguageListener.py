# Generated from scriptingLanguage.g4 by ANTLR 4.7.1
from antlr4 import *
from testClass import testClass

# This class defines a complete listener for a parse tree produced by scriptingLanguageParser.
class scriptingLanguageListener(ParseTreeListener):

    # This function the INITIALIZATION function called when the Listener is instantiated
    def __init__(self, suiteObject):
        # Setting the variables that will be used by the other functions that will be called in the future
        self.testValue = 33
        self.suiteObject = suiteObject

    # Enter a parse tree produced by scriptingLanguageParser#suite.
    def enterSuite(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#suite.
    def exitSuite(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#apptype.
    def enterApptype(self, ctx):
        # Finding out the app category
        appCategory = ctx.children[0]
        # Setting it to the suiteObject
        self.suiteObject.setTargetAppCategory(appCategory)
        pass

    # Exit a parse tree produced by scriptingLanguageParser#apptype.
    def exitApptype(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testlist.
    def enterTestlist(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testlist.
    def exitTestlist(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testtype1.
    def enterTesttype1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testtype1.
    def exitTesttype1(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testtype2.
    def enterTesttype2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testtype2.
    def exitTesttype2(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testtype3.
    def enterTesttype3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testtype3.
    def exitTesttype3(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testtype4.
    def enterTesttype4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testtype4.
    def exitTesttype4(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testtype5.
    def enterTesttype5(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testtype5.
    def exitTesttype5(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testtype6.
    def enterTesttype6(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testtype6.
    def exitTesttype6(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testtype7.
    def enterTesttype7(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testtype7.
    def exitTesttype7(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testtype8.
    def enterTesttype8(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testtype8.
    def exitTesttype8(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testsame1.
    def enterTestsame1(self, ctx):
        # This is the case of LOGIN activity
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, True)
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame1.
    def exitTestsame1(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testdiff1.
    def enterTestdiff1(self, ctx):
        # This is the case of LOGIN activity
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, False, str(ctx.children[6].children[0]))
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff1.
    def exitTestdiff1(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testsame2.
    def enterTestsame2(self, ctx):
        # This is the case of LOGIN activity
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, True)
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame2.
    def exitTestsame2(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testdiff2.
    def enterTestdiff2(self, ctx):
        # Retrieving the starting activity type
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, False, str(ctx.children[6].children[0]))
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff2.
    def exitTestdiff2(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testsame3.
    def enterTestsame3(self, ctx):
        # This is the case of LOGIN activity
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, True)
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame3.
    def exitTestsame3(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff3.
    def enterTestdiff3(self, ctx):
        # Retrieving the starting activity type
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, False, str(ctx.children[6].children[0]))
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff3.
    def exitTestdiff3(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame4.
    def enterTestsame4(self, ctx):
        # This is the case of LOGIN activity
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, True)
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame4.
    def exitTestsame4(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff4.
    def enterTestdiff4(self, ctx):
        # Retrieving the starting activity type
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, False, str(ctx.children[6].children[0]))
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff4.
    def exitTestdiff4(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame5.
    def enterTestsame5(self, ctx):
        # This is the case of LOGIN activity
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, True)
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame5.
    def exitTestsame5(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff5.
    def enterTestdiff5(self, ctx):
        # Retrieving the starting activity type
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, False, str(ctx.children[6].children[0]))
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff5.
    def exitTestdiff5(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame6.
    def enterTestsame6(self, ctx):
        # This is the case of LOGIN activity
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, True)
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame6.
    def exitTestsame6(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff6.
    def enterTestdiff6(self, ctx):
        # Retrieving the starting activity type
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, False, str(ctx.children[6].children[0]))
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff6.
    def exitTestdiff6(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame7.
    def enterTestsame7(self, ctx):
        # This is the case of LOGIN activity
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, True)
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame7.
    def exitTestsame7(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff7.
    def enterTestdiff7(self, ctx):
        # Retrieving the starting activity type
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, False, str(ctx.children[6].children[0]))
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff7.
    def exitTestdiff7(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame8.
    def enterTestsame8(self, ctx):
        # This is the case of LOGIN activity
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, True)
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame8.
    def exitTestsame8(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff8.
    def enterTestdiff8(self, ctx):
        # Retrieving the starting activity type
        startingActivity = str(ctx.children[1])
        print "\nAbout to parse a test for activity: " + startingActivity
        # Instantiating the test object
        testObject = testClass(startingActivity, False, str(ctx.children[6].children[0]))
        # Setting this object as temporary up to when we have filled all its commands
        self.tempTest = testObject
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff8.
    def exitTestdiff8(self, ctx):
        # Eventually adding the test to its suite
        self.suiteObject.addTestObject(self.tempTest)
        print "Done with " + str(len(self.suiteObject.testCasesList)) + " tests"
        pass


    # Enter a parse tree produced by scriptingLanguageParser#activitytype.
    def enterActivitytype(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#activitytype.
    def exitActivitytype(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist1.
    def enterCommandlist1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist1.
    def exitCommandlist1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command1ver1.
    def enterCommand1ver1(self, ctx):
        # Retrieving the input string for the note name
        inputString = str(ctx.children[2])
        # Creafting the command string
        commandString = "test.todoAddNewNote(" + inputString + ")"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command1ver1.
    def exitCommand1ver1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command1ver2.
    def enterCommand1ver2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command1ver2.
    def exitCommand1ver2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command1ver3.
    def enterCommand1ver3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command1ver3.
    def exitCommand1ver3(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command1ver4.
    def enterCommand1ver4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command1ver4.
    def exitCommand1ver4(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command1ver5.
    def enterCommand1ver5(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command1ver5.
    def exitCommand1ver5(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command1ver6.
    def enterCommand1ver6(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command1ver6.
    def exitCommand1ver6(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command1ver7.
    def enterCommand1ver7(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command1ver7.
    def exitCommand1ver7(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist2.
    def enterCommandlist2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist2.
    def exitCommandlist2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command2ver1.
    def enterCommand2ver1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command2ver1.
    def exitCommand2ver1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command2ver2.
    def enterCommand2ver2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command2ver2.
    def exitCommand2ver2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command2ver3.
    def enterCommand2ver3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command2ver3.
    def exitCommand2ver3(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist3.
    def enterCommandlist3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist3.
    def exitCommandlist3(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#command3ver1.
    def enterCommand3ver1(self, ctx):
        # Retrieving and elaborating the input string
        inputString = str(ctx.children[2])
        # Crafting the command string
        commandString = "test.loginInputName(" + inputString + ")"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command3ver1.
    def exitCommand3ver1(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#command3ver2.
    def enterCommand3ver2(self, ctx):
        # Retrieving and elaborating the input string
        inputString = str(ctx.children[2])
        # Crafting the command string
        commandString = "test.loginInputPassword(" + inputString + ")"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command3ver2.
    def exitCommand3ver2(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#command3ver3.
    def enterCommand3ver3(self, ctx):
        # Simply adding the 'click next' command
        commandString = "test.clickNext()"
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command3ver3.
    def exitCommand3ver3(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist4.
    def enterCommandlist4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist4.
    def exitCommandlist4(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command4ver1.
    def enterCommand4ver1(self, ctx):
        # Retrieving and elaborating the input string
        lineNumber = str(ctx.children[2])
        # Crafting the command string
        commandString = "test.clickListLine(" + lineNumber + ")"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command4ver1.
    def exitCommand4ver1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command4ver2.
    def enterCommand4ver2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command4ver2.
    def exitCommand4ver2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command4ver3.
    def enterCommand4ver3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command4ver3.
    def exitCommand4ver3(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command4ver4.
    def enterCommand4ver4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command4ver4.
    def exitCommand4ver4(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command4ver5.
    def enterCommand4ver5(self, ctx):
        # Crafting the command string
        commandString = "test.customPressBack()"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command4ver5.
    def exitCommand4ver5(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command4ver6.
    def enterCommand4ver6(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command4ver6.
    def exitCommand4ver6(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command4ver7.
    def enterCommand4ver7(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command4ver7.
    def exitCommand4ver7(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist5.
    def enterCommandlist5(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist5.
    def exitCommandlist5(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command5ver1.
    def enterCommand5ver1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command5ver1.
    def exitCommand5ver1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command5ver2.
    def enterCommand5ver2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command5ver2.
    def exitCommand5ver2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command5ver3.
    def enterCommand5ver3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command5ver3.
    def exitCommand5ver3(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command5ver4.
    def enterCommand5ver4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command5ver4.
    def exitCommand5ver4(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist6.
    def enterCommandlist6(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist6.
    def exitCommandlist6(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command6ver1.
    def enterCommand6ver1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command6ver1.
    def exitCommand6ver1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command6ver2.
    def enterCommand6ver2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command6ver2.
    def exitCommand6ver2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command6ver3.
    def enterCommand6ver3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command6ver3.
    def exitCommand6ver3(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist7.
    def enterCommandlist7(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist7.
    def exitCommandlist7(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command7ver1.
    def enterCommand7ver1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command7ver1.
    def exitCommand7ver1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command7ver2.
    def enterCommand7ver2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command7ver2.
    def exitCommand7ver2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command7ver3.
    def enterCommand7ver3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command7ver3.
    def exitCommand7ver3(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command7ver4.
    def enterCommand7ver4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command7ver4.
    def exitCommand7ver4(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command7ver5.
    def enterCommand7ver5(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command7ver5.
    def exitCommand7ver5(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command7ver6.
    def enterCommand7ver6(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command7ver6.
    def exitCommand7ver6(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command7ver7.
    def enterCommand7ver7(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command7ver7.
    def exitCommand7ver7(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist8.
    def enterCommandlist8(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist8.
    def exitCommandlist8(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command8ver1.
    def enterCommand8ver1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command8ver1.
    def exitCommand8ver1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command8ver2.
    def enterCommand8ver2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command8ver2.
    def exitCommand8ver2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command8ver3.
    def enterCommand8ver3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command8ver3.
    def exitCommand8ver3(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command8ver4.
    def enterCommand8ver4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command8ver4.
    def exitCommand8ver4(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command8ver5.
    def enterCommand8ver5(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command8ver5.
    def exitCommand8ver5(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#commandCustomClick.
    def enterCommandCustomClick(self, ctx):
        # Retrieving screen coordinates
        x = ctx.children[2].children[0]
        y = ctx.children[2].children[1]
        # Crafting the command string
        commandString = "test.customClick(" + str(x) + "," + str(y) + ")"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandCustomClick.
    def exitCommandCustomClick(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandCustomLongClick.
    def enterCommandCustomLongClick(self, ctx):
        # Retrieving screen coordinates
        x = ctx.children[3].children[0]
        y = ctx.children[3].children[1]
        # Crafting the command string
        commandString = "test.customLongClick(" + str(x) + "," + str(y) + ")"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandCustomLongClick.
    def exitCommandCustomLongClick(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandCustomDrag.
    def enterCommandCustomDrag(self, ctx):
        # Retrieving screen coordinates and drag duration
        xStart = ctx.children[3].children[0]
        yStart = ctx.children[3].children[1]
        xEnd = ctx.children[5].children[0]
        yEnd = ctx.children[5].children[1]
        duration = ctx.children[7]
        # Crafting the command string
        commandString = "test.customDrag(" + str(xStart) + "," + str(yStart) + "," + str(xEnd) + "," + str(yEnd) + "," + str(duration) + ")"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandCustomDrag.
    def exitCommandCustomDrag(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandCustomType.
    def enterCommandCustomType(self, ctx):
        # Retrieving screen coordinates
        inputString = ctx.children[2]
        # Crafting the command string
        commandString = "test.customType(" + str(inputString) + ")"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandCustomType.
    def exitCommandCustomType(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandCustomBack.
    def enterCommandCustomBack(self, ctx):
        # Crafting the command string
        commandString = "test.customPressBack()"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandCustomBack.
    def exitCommandCustomBack(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#commandCustomSleep.
    def enterCommandCustomSleep(self, ctx):
        # Getting the seconds of sleep
        inputString = ctx.children[2]
        # Crafting the command string
        commandString = "test.customSleep(" + str(inputString) + ")"
        # Adding the command to the list of the temporary test
        self.tempTest.appendCommandFunction(commandString)
        print "Entering command: " + commandString
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandCustomSleep.
    def exitCommandCustomSleep(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#coordinate.
    def enterCoordinate(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#coordinate.
    def exitCoordinate(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testCustom.
    def enterTestCustom(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testCustom.
    def exitTestCustom(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testSlot1.
    def enterTestSlot1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testSlot1.
    def exitTestSlot1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testSlot2.
    def enterTestSlot2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testSlot2.
    def exitTestSlot2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testSlot3.
    def enterTestSlot3(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testSlot3.
    def exitTestSlot3(self, ctx):
        pass


