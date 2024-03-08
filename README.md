# YourPy
An engine to append some simple features to the default python interface

## File
Simple example of YourPy

```python
# ypy:compile

print("YPY")
```

## Features

### Module Import
Imagine this directory structure

- dir
  - sub1
    - sub2
      - `name.py`

***Python***
```python
from dir.sub1.sub2.name import Name

Name.show()
```

***YourPy***
```python
# ypy:compile

from module name import Name

Name.show()
```

### Block
***Python***
```python
for x in [1,2,3]:
  print(x)
```

***YourPy***
```python
# ypy:compile

for x in [1,2,3]:
  print(x)

# and

for x in [1,2,3]{
  print(x)
}
```

### Dict Access
***Python***
```python
words = {
    "w1": "word1",
    "w2": "word2",
    "w3": "word3",
    "w4": "word4",
}

print(words["w1"])
```

***YourPy***
```python
# ypy:compile

words = {
    w1: "word1",
    w2: "word2",
    w3: "word3",
    w4: "word4",
}

print(words.w1)
```

### Interface
```python
# ypy:compile

interface IFactory:
    show(str)->str
    make(int,int,str)->bool

class Factory:
    def show(self, a:str)->str:    
        pass

    def make(self, a:int, b:int, c:str)->bool:    
        pass
```
