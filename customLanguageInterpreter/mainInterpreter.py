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
        # TODO Here we should be going to the state specified by the test
        # Now iterating through all commands of this test
        test.initDump()
        print "TEST: Found a command list of size: " + str(len(test.commandsList))
        for command in test.commandsList:
            # Interpreting and executing commands
            eval(command)
            # Let one second go by after a command
            time.sleep(1)

        print "\n"


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