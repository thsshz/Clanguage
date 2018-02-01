import sys
from antlr4 import *
from ClanguageLexer import ClanguageLexer
from ClanguageParser import ClanguageParser
from PythonVisitor import PythonVisitor


def main(argv):
    input = FileStream(argv[1])
    lexer = ClanguageLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ClanguageParser(stream)
    tree = parser.root()
    visitor = PythonVisitor()
    visitor.visit(tree)
    res_file = open('result.py', 'w')
    res_file.write(visitor.res_code)
    main_str = "if __name__ == '__main__':\n    main()"
    res_file.write(main_str)
    res_file.close()


if __name__ == '__main__':
    main(sys.argv)
