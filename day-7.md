
#  Day 7: Dictionary and Sets in Python

Today I learned about dictionaries and sets in Python, along with their properties and operations. These data structures are very useful for storing and managing data efficiently.

## Dictionary in Python

A dictionary is a collection of key-value pairs. Each key is unique and is used to access its corresponding value.

### Properties:

* Dictionaries store data in key-value pairs
* Keys are unique and cannot be duplicated
* Dictionaries are mutable (can be changed)
* They are unordered (no fixed index position)

### Examples:

**Example 1:**

student = {"name": "John", "age": 20, "course": "CS"}
print(student)

**Example 2:**

print(student["name"])   # access value using key

**Example 3:**

student["age"] = 21
print(student)

**Example 4:**

student["grade"] = "A"
print(student)

**Example 5:**

print(student.keys())
print(student.values())

## Operations on Dictionary

### Properties:

* Values can be added, updated, and removed
* Data is accessed using keys
* Supports multiple built-in methods
* Useful for structured data

### Examples:

**Example 1:**

student = {"name": "John", "age": 20}
student.update({"age": 22})
print(student)

**Example 2:**

student.pop("age")
print(student)

**Example 3:**

student.clear()
print(student)

**Example 4:**

student = {"a": 1, "b": 2}
print("a" in student)

**Example 5:**

print(len(student))

## Sets in Python

A set is a collection of unique elements. Sets are unordered and do not allow duplicate values.

### Properties:

* Sets do not allow duplicate elements
* Sets are unordered
* Sets are mutable
* Useful for mathematical operations

### Examples:

**Example 1:**

s = {1, 2, 3, 4}
print(s)

**Example 2:**

s = {1, 2, 2, 3}
print(s)   # duplicates removed

**Example 3:**

s.add(5)
print(s)

**Example 4:**

s.remove(2)
print(s)

**Example 5:**

print(3 in s)

## Operations on Sets

### Properties:

* Supports mathematical operations like union and intersection
* Elements can be added or removed
* Efficient for membership testing
* Automatically removes duplicates

### Examples:

**Example 1:**

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

**Example 2:**

print(a.intersection(b))

**Example 3:**

print(a.difference(b))

**Example 4:**

print(a.symmetric_difference(b))

**Example 5:**

a.clear()
print(a)

## Conclusion

Today’s learning helped me understand how dictionaries store data using key-value pairs and how sets manage unique elements. These concepts are very useful for handling real-world data efficiently.
