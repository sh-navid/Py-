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
<!-- 1 -->
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

___


### Block
<!-- 2 -->
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

___


### Dict Access
<!-- 3 -->
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

___


### Interface
<!-- 4 -->
***YourPy***
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

___


### Function
<!-- 5 -->
***Python***
```python
func = lambda a: print(a)

func = lambda a, b: print(a, b)
```

***YourPy***
```python
func = a: print(a)

func = a, b: print(a, b)
```

___


### Ternary
<!-- 6 -->
***Python***
```python
a = "low" if True else "high"
```

***YourPy***
```python
a = True ? "low" : "high"

a = if True "low" else "high"
```

### Multiple Condition
<!-- 7 -->
***Python***
```python
if 1:
    a = "One"
elif 2:
    a = "Two"
elif 2:
    a = "Three"
else:
    a = "Other"

```

***YourPy***
```python
a = ? 1 : "One", 2 : "Two", 3 : "Three", "Other"
```

