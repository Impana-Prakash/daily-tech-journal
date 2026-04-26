#  Day 14: Python – Functions, Arguments, and Advanced Concepts

Today I continued learning functions in Python and explored different types of arguments, variable scope, and lambda functions. This helped me understand how to write more flexible and efficient code.

---

## Function without Arguments

A function can be defined without passing any parameters.

### Example:

```python id="p9d2k1"
def fun():
    print("This is a simple function")

fun()
```

---

## Positional Arguments

In positional arguments, values are passed in the same order as parameters.

### Example:

```python id="t3x8v2"
def add(a, b):
    print("Sum =", a + b)

add(5, 3)
```

---

## Keyword Arguments

In keyword arguments, values are passed using parameter names.

### Example:

```python id="m7q2z4"
def display(name, age):
    print("Name:", name)
    print("Age:", age)

display(age=20, name="Impana")
```

---

## Default Arguments

Default values are assigned to parameters if no value is provided.

### Example:

```python id="b4k9n6"
def greet(name="User"):
    print("Hello", name)

greet()
greet("Impana")
```

---

## Function with Variable Input

A function can take input dynamically (for example, string input).

### Example:

```python id="c8w3y1"
def fun(variable):
    print("Value is:", variable)

fun("Python")
```

---

## *args and **kwargs

These are used to pass a variable number of arguments to a function.

### *args (multiple positional arguments)

```python id="x1r6p3"
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum =", total)

add(1, 2, 3, 4)
```

---

### **kwargs (multiple keyword arguments)

```python id="z5u2m7"
def display(**data):
    for key, value in data.items():
        print(key, ":", value)

display(name="Impana", age=20)
```

---

## Local and Global Variables

* **Local variables** are defined inside a function and can be used only within that function.
* **Global variables** are defined outside and can be accessed anywhere in the program.

### Example:

```python id="n2k8d5"
x = 10  # global variable

def fun():
    y = 5  # local variable
    print("Local:", y)
    print("Global:", x)

fun()
print("Global outside:", x)
```

---

## Lambda Function

A lambda function is a small anonymous function defined using the `lambda` keyword.

### Example:

```python id="v6q1p9"
square = lambda x: x * x

print(square(5))
```

---

### Example: Lambda with Multiple Values

```python id="r4t7b2"
add = lambda a, b: a + b

print(add(3, 7))
```

---

## Key Understanding

* Functions help organize and reuse code
* Arguments can be passed in different ways
* `*args` and `**kwargs` make functions flexible
* Local and global variables define scope
* Lambda functions are useful for short operations

---

## Conclusion

Today’s learning helped me understand advanced function concepts in Python. These concepts make code more flexible, reusable, and efficient for real-world programming.

