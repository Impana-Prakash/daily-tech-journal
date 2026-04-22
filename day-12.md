# Day 12: Loops in Python

Today I learned about loops in Python and how they help in executing a block of code multiple times. Loops are essential for handling repetitive tasks and writing efficient programs.

---

## What I Learned

* Types of loops in Python
* Working with `while` loop
* Using lists and tuples with loops
* `for` loop and `range()` function
* `for-else` concept
* Control statements: `break`, `continue`, and `pass`

---

## Types of Loops in Python

Python mainly provides two types of loops:

* **for loop** → used when the number of iterations is known
* **while loop** → used when the condition controls execution

---

## While Loop

A `while` loop runs as long as a condition is true.

### Example: Print sum of first 10 natural numbers

```python
i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)
```

---

## List using While Loop

We can use a `while` loop to iterate through list elements.

### Example: Find even numbers in a list

```python
numbers = [10, 15, 20, 25, 30, 35]

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(numbers[i])
    i += 1
```

---

## Tuple using While Loop

Similar to lists, tuples can also be traversed using a `while` loop.

### Example: Count elements greater than 5

```python
t = (2, 6, 3, 8, 1, 9)

i = 0
count = 0

while i < len(t):
    if t[i] > 5:
        count += 1
    i += 1

print("Count =", count)
```

---

## For Loop

A `for` loop is used to iterate over a sequence.

### Example: Print factorial of a number

```python
n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
```

---

## Range Function in Python

The `range()` function generates a sequence of numbers.

### Example: Print squares of numbers

```python
for i in range(1, 6):
    print("Square of", i, "=", i * i)
```

---

## For Loop with Else

The `else` block executes when the loop completes normally.

### Example: Search for an element in a list

```python
numbers = [1, 3, 5, 7, 9]
key = 5

for num in numbers:
    if num == key:
        print("Element found")
        break
else:
    print("Element not found")
```

---

## Break Statement

The `break` statement exits the loop immediately.

### Example: Stop when number divisible by 7 is found

```python
for i in range(1, 20):
    if i % 7 == 0:
        print("First divisible by 7:", i)
        break
```

---

## Continue Statement

The `continue` statement skips the current iteration.

### Example: Skip odd numbers

```python
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i)
```

---

## Pass Statement

The `pass` statement acts as a placeholder.

### Example:

```python
for i in range(5):
    if i == 3:
        pass
    print(i)
```

---

## Conclusion

Today’s learning helped me understand how loops work in Python and how they can be used effectively with different data structures. These concepts are essential for solving real-world problems and writing efficient programs.
