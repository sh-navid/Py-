# YourPy

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

Python

```python
from dir.sub1.sub2.name import Name

Name.show()
```

YourPy

```python
# ypy:compile

from module name import Name

Name.show()
```

### Block

Python

```python
for x in [1,2,3]:
  print(x)
```

YourPy

```python
for x in [1,2,3]:
  print(x)
# and
for x in [1,2,3]{
  print(x)
}
```
