import sys
from antlr4 import *
from scriptingLanguageLexer import scriptingLanguageLexer
from scriptingLanguageParser import scriptingLanguageParser
from scriptingLanguageListener import scriptingLanguageListener


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


    # Instantiating the Listener
    htmlChat = scriptingLanguageListener()
    walker = ParseTreeWalker()
    walker.walk(htmlChat, tree)




if __name__ == '__main__':
    main(sys.argv)