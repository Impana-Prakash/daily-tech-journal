#  Day 15: Python – Comprehensions and Error Handling

Today I learned about list and dictionary comprehensions, along with error handling in Python. These concepts help in writing cleaner code and handling unexpected situations effectively.

---

## What I Learned

* List comprehension
* Dictionary comprehension
* Try-except structure
* Different types of errors in Python

---

## List Comprehension

List comprehension provides a concise way to create lists.

### Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)
```

---

### Example: With Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even = [x for x in numbers if x % 2 == 0]

print(even)
```

---

## Dictionary Comprehension

Dictionary comprehension is used to create dictionaries in a compact way.

### Example:

```python
numbers = [1, 2, 3, 4]

square_dict = {x: x * x for x in numbers}

print(square_dict)
```

---

### Example: With Condition

```python
numbers = [1, 2, 3, 4, 5]

even_dict = {x: x * x for x in numbers if x % 2 == 0}

print(even_dict)
```

---

## Try-Except (Error Handling)

The `try-except` block is used to handle errors and prevent the program from crashing.

### Structure:

```python
try:
    # code that may cause error
except:
    # code to handle error
```

---

### Example:

```python
try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except:
    print("Error occurred")
```

---

## Types of Errors in Python

### 1. Syntax Error

Occurs when the code structure is incorrect.

```python
# Missing colon
if True
    print("Error")
```

---

### 2. Runtime Errors

These occur during execution.

#### ZeroDivisionError

Occurs when dividing by zero.

```python
a = 10
b = 0
print(a / b)
```

---

#### ValueError

Occurs when invalid input is given.

```python
num = int("abc")
```

---

#### TypeError

Occurs when an operation is performed on incompatible data types.

```python
a = "10"
b = 5
print(a + b)
```

---

#### IndexError

Occurs when accessing an index that does not exist.

```python
lst = [1, 2, 3]
print(lst[5])
```

---

### 3. Logical Error

Program runs but produces incorrect output.

```python
a = 5
b = 3
print("Sum =", a - b)  # wrong logic
```

---

## Key Understanding

* Comprehensions make code shorter and more readable
* Conditions can be added inside comprehensions
* `try-except` helps handle errors safely
* Errors can be syntax, runtime, or logical
* Common runtime errors include ZeroDivisionError, ValueError, TypeError, and IndexError

---

## Conclusion

Today’s learning helped me write cleaner Python code using comprehensions and understand how to handle errors effectively. These concepts are very useful for writing robust and efficient programs.

