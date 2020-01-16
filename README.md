# PyStack
PyStack is my implementation of stack data structure using Python 3 and mypy. 
## Code 
This project is actually 2 files of source code. `node.py` is simple data node used by `Stack` in `stack.py`.

## Example usage
Usage of this code is very simple. You just declare your Stack and its type. Here is example using `int` type:

```python
stack = Stack[int]()
```

You can also pass some initial arguments to put on stack at initialization.

```python
stack = Stack[int](12, 13, 14)
```

NOTE: if you want to pass Python list as arguments, use spread operator with it

```python
stack = Stack[int](*[12, 13, 14])
```

## API
Stack class has very simple and (for those who know what stack data structure is) intuitive API. It offers methods like:

```python
.push(data)
.pop()
.is_empty()
.get_state()
```

### `.push(data)`
This method adds new data to stack. `data` param is of a type of your Stack.

### `.pop()`
This methods removes data from top of stack and returns it. If your Stack is empty, it will return `None`.

### `.is_empty()`
This method returns `bool` stating whether there is any data on stack (`False`) or stack is empty (`True`)

### `.get_state()`
This method returns list of data on stack. Data is of a type of your Stack.

 