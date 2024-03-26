import sys

from engine.compiler import Compiler


if __name__=="__main__":
    # (script, file) = sys.argv
    
    Compiler.compile_pyp(sys.path[0]+"/testcase/1/main.pyp")