import sys
from antlr4 import *
from scriptingLanguageLexer import scriptingLanguageLexer
from scriptingLanguageParser import scriptingLanguageParser
from scriptingLanguageListener import scriptingLanguageListener
from suiteClass import *
import time




def executeTests(suiteObject):

    print "\n\n\n-------------------------------------------------------\n"
    print "Found " + str(len(suiteObject.testCasesList)) + " tests to be executed!\n"
    # Iterating through all of the test
    for test in suiteObject.testCasesList:

        positiveResult = True
        # TODO Here we should be going to the state specified by the test
        # Making the initial dump for the starting state
        test.initDump()
        print "TEST: Found a command list of size: " + str(len(test.commandsList))
        # Now iterating through all commands of this test
        for command in test.commandsList:
            # Interpreting and executing commands
            result = eval(command)
            if result==False:
                positiveResult = False
                break
            # Let one second go by after a command
            time.sleep(1)

        # Checking the result of the test execution (only if everything up to now was ok)
        if positiveResult==True:
            # Finding out the arrival state
            resultingState = test.finalStateCheck()
            print resultingState
            # Comparing the arrival state with the expected state
            if test.sameDestination == True and resultingState != "SAME":
                positiveResult = False
            elif test.sameDestination == False and resultingState != test.endActivityType:
                positiveResult = False

        # Printing out the esit of the test
        if positiveResult == True:
            print "---> TEST PASSED!\n"
        else:
            print "---> TEST FAILED...\n"




def main(argv):

    # Setting the input file containing the input string
    input = FileStream("./input.txt")

    # Instantiating the Lexer
    lexer = scriptingLanguageLexer(input)
    stream = CommonTokenStream(lexer)
    # Instantiating the Parser
    parser = scriptingLanguageParser(stream)
    # Calling the ROOT of the parser (it will have the same name as the most upper parser token)
    tree = parser.suite()

    # Instantiating the suiteClass object
    suiteObject = suiteClass()

    # Instantiating the Listener
    results = scriptingLanguageListener(suiteObject)
    walker = ParseTreeWalker()
    walker.walk(results, tree)

    # EXECUTING THE TESTS
    executeTests(suiteObject)



if __name__ == '__main__':
    main(sys.argv)