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
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame1.
    def exitTestsame1(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testdiff1.
    def enterTestdiff1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff1.
    def exitTestdiff1(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testsame2.
    def enterTestsame2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame2.
    def exitTestsame2(self, ctx):
        pass

    # Enter a parse tree produced by scriptingLanguageParser#testdiff2.
    def enterTestdiff2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff2.
    def exitTestdiff2(self, ctx):
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
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff3.
    def exitTestdiff3(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame4.
    def enterTestsame4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame4.
    def exitTestsame4(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff4.
    def enterTestdiff4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff4.
    def exitTestdiff4(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame5.
    def enterTestsame5(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame5.
    def exitTestsame5(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff5.
    def enterTestdiff5(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff5.
    def exitTestdiff5(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame6.
    def enterTestsame6(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame6.
    def exitTestsame6(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff6.
    def enterTestdiff6(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff6.
    def exitTestdiff6(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame7.
    def enterTestsame7(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame7.
    def exitTestsame7(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff7.
    def enterTestdiff7(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff7.
    def exitTestdiff7(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testsame8.
    def enterTestsame8(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testsame8.
    def exitTestsame8(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#testdiff8.
    def enterTestdiff8(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#testdiff8.
    def exitTestdiff8(self, ctx):
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


    # Enter a parse tree produced by scriptingLanguageParser#command1.
    def enterCommand1(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command1.
    def exitCommand1(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist2.
    def enterCommandlist2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist2.
    def exitCommandlist2(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command2.
    def enterCommand2(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command2.
    def exitCommand2(self, ctx):
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


    # Enter a parse tree produced by scriptingLanguageParser#command4.
    def enterCommand4(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command4.
    def exitCommand4(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist5.
    def enterCommandlist5(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist5.
    def exitCommandlist5(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command5.
    def enterCommand5(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command5.
    def exitCommand5(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist6.
    def enterCommandlist6(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist6.
    def exitCommandlist6(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command6.
    def enterCommand6(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command6.
    def exitCommand6(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist7.
    def enterCommandlist7(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist7.
    def exitCommandlist7(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command7.
    def enterCommand7(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command7.
    def exitCommand7(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#commandlist8.
    def enterCommandlist8(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#commandlist8.
    def exitCommandlist8(self, ctx):
        pass


    # Enter a parse tree produced by scriptingLanguageParser#command8.
    def enterCommand8(self, ctx):
        pass

    # Exit a parse tree produced by scriptingLanguageParser#command8.
    def exitCommand8(self, ctx):
        pass


