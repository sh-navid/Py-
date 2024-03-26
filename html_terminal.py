import sys
from engine.feature.html import PyHtml
from engine.compiler import File




if __name__=="__main__":
    ROOT=sys.path[0]
    PATH_IN=ROOT+"/testcase/10/main.pyn"
    PATH_OUT=ROOT+"/testcase/10/main.pyn.out.py"

    content = File.read(PATH_IN)
    if "pyn:compile" not in content:
        raise RuntimeError("There is no pyn:compile svsilsble in file")

    content=PyHtml().exec(content)
    File.write(PATH_OUT,content)