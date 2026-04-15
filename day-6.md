# Day 5: Lists, List Methods, Tuples, and Tuple Methods

Today I learned about lists and tuples in Python, along with their commonly used methods. These are important data structures that help in storing and managing multiple values.

## Lists in Python

A list is a collection of items stored in a single variable. Lists are ordered, mutable (which means they can be changed), and they allow duplicate values.

### Key Features:

* Lists are ordered, so elements have a fixed position
* Lists are mutable, so values can be changed
* Lists allow duplicate values
* Lists can store different data types

### Examples:

**Example 1:**

numbers = [1, 2, 3, 4, 5]
print(numbers)

**Example 2:**

fruits = ["apple", "banana", "cherry"]
print(fruits)

**Example 3:**

mixed = [1, "Python", 3.5]
print(mixed)

**Example 4:**

print(numbers[0])   # first element
print(numbers[-1])  # last element

**Example 5:**

numbers[0] = 10
print(numbers)

## List Methods

Python provides built-in methods to work with lists, making it easier to modify and manage data.

### Key Features:

* Methods help in adding and removing elements
* Lists can be sorted and reversed easily
* Built-in functions simplify operations
* Methods modify the original list

### Examples:

**Example 1:**

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

**Example 2:**

numbers.insert(1, 10)
print(numbers)

**Example 3:**

numbers.remove(2)
print(numbers)

**Example 4:**

numbers.pop()
print(numbers)

**Example 5:**

numbers.sort()
print(numbers)

## Tuples in Python

A tuple is similar to a list, but it is immutable, which means its values cannot be changed after creation.

### Key Features:

* Tuples are ordered collections
* Tuples are immutable (cannot be changed)
* Tuples allow duplicate values
* Tuples are faster than lists

### Examples:

**Example 1:**

t = (1, 2, 3)
print(t)

**Example 2:**

t = ("apple", "banana", "cherry")
print(t)

**Example 3:**

print(t[0])
print(t[-1])

**Example 4:**

single = (5,)
print(type(single))

**Example 5:**

t = (1, 2, 3)
# t[0] = 10  # not allowed

## Tuple Methods

Tuples have only a few built-in methods compared to lists.

### Key Features:

* Tuples have limited methods
* They support basic operations like count and index
* Tuples are memory efficient
* Useful for fixed data

### Examples:

**Example 1:**

t = (1, 2, 3, 2, 2)
print(t.count(2))

**Example 2:**

print(t.index(3))

**Example 3:**

t = (10, 20, 30)
print(len(t))

**Example 4:**

t = (1, 2, 3)
print(2 in t)

**Example 5:**

t = (1, 2, 3)
print(max(t))

## Conclusion

Today’s learning helped me clearly understand the difference between lists and tuples. Lists are flexible and can be modified, while tuples are fixed and useful when data should not be changed.
