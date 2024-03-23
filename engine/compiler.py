import sys

if __name__=="__main__":
    (compiler,file)=sys.argv

    if compiler != "compiler.py":
        raise RuntimeError("Use compiler.py directly")