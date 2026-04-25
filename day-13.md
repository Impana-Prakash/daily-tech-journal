# Day 13: Functions in Python

Today I learned about functions in Python and how they help in organizing code into reusable blocks. Functions make programs more structured, readable, and easier to manage.

---

## What I Learned

* What are functions in Python
* Function syntax and structure
* Function definition and function call
* Types of functions
* Functions with arguments
* Default parameter values

---

## Functions in Python

A function is a block of code that performs a specific task and can be reused whenever needed. It helps reduce repetition and improves code readability.

---

## Function Syntax

```python id="4rht8v"
def function_name(parameters):
    # code block
```

---

## Function Definition and Function Call

* **Function Definition** → Writing the function
* **Function Call** → Executing the function

### Example:

```python id="q9yxr3"
def greet():
    print("Hello, Welcome!")

greet()
```

---

## Types of Functions in Python

* Built-in functions (like `print()`, `len()`)
* User-defined functions (created by the programmer)

---

## Function with Arguments

Functions can take inputs (arguments) to perform operations.

### Example:

```python id="9y4qfb"
def add(a, b):
    result = a + b
    print("Sum =", result)

add(5, 3)
```

---

### Example: Multiple Arguments

```python id="k0b1t9"
def display(name, age):
    print("Name:", name)
    print("Age:", age)

display("Impana", 20)
```

---

## Default Parameter Values

We can assign default values to parameters. If no value is passed, the default value is used.

### Example:

```python id="0qz9xr"
def greet(name="User"):
    print("Hello", name)

greet()
greet("Impana")
```

---

### Example: Calculation with Default Value

```python id="0d68rs"
def power(base, exp=2):
    print(base ** exp)

power(5)
power(5, 3)
```

---

## Conclusion

Today’s learning helped me understand how functions work in Python and how they can be used to make code reusable and organized. Using arguments and default values makes functions more flexible and powerful.

---
