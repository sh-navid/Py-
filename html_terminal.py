import sys
from engine.feature.html import PyHtml


def read(path):
    with open(path,"r") as f:
        return f.read()
    
def write(path,content):
    with open(path,"w") as f:
        f.write(content)


if __name__=="__main__":
    ROOT=sys.path[0]
    PATH_IN=ROOT+"/testcase/10/main.pyn"
    PATH_OUT=ROOT+"/testcase/10/main.pyn.out.py"

    content = read(PATH_IN)
    if "pyn:compile" not in content:
        raise RuntimeError("There is no pyn:compile svsilsble in file")

    content=PyHtml().exec(content)
    write(PATH_OUT,content)