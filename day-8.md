#  Day 7: Problem Solving on Dictionaries and Sets

Today I focused on solving multiple problems using dictionaries and sets in Python. Instead of learning new concepts, I spent time applying what I learned in the previous days.

I solved more than 10 problems, which helped me understand how dictionaries and sets work in real situations.

## What I Practiced

* Creating and updating dictionaries
* Accessing values using keys
* Checking if a key exists in a dictionary
* Using sets to remove duplicate values
* Performing operations like union, intersection, and difference
* Solving problems using real-world logic

## Key Features of Dictionary

* Stores data in key-value pairs
* Keys are unique and immutable
* Dictionaries are mutable
* Fast access using keys

## Advantages of Dictionary

* Quick data retrieval using keys
* Easy to update and modify
* Suitable for structured data
* Widely used in real-world applications

## Disadvantages of Dictionary

* Keys must be unique
* No indexing support
* Slightly higher memory usage
* Can be complex for beginners

##  Problems on Dictionary

**Problem 1:** Write a program to count the frequency of each character in a given string.

text = "programming"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

**Problem 2:** Write a program to merge two dictionaries into one.

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d1.update(d2)
print(d1)

**Problem 3:** Write a program to find the key with the maximum value in a dictionary.

d = {"a": 10, "b": 20, "c": 15}

max_key = max(d, key=d.get)
print(max_key)

**Problem 4:** Write a program to swap keys and values in a dictionary.

d = {"a": 1, "b": 2, "c": 3}

inv = {v: k for k, v in d.items()}
print(inv)

**Problem 5:** Write a program to check whether a given key exists in a dictionary.

d = {"name": "John", "age": 20}

print("name" in d)

## Key Features of Sets

* Stores unique elements only
* Unordered collection
* Mutable data structure
* Supports mathematical operations

## Advantages of Sets

* Automatically removes duplicates
* Fast membership checking
* Supports union, intersection, and difference
* Efficient for comparisons

## Disadvantages of Sets

* No indexing support
* Unordered data
* Cannot store duplicate values
* Limited methods compared to lists

##  Problems on Sets

**Problem 1:** Write a program to remove duplicate elements from a list.

nums = [1, 2, 2, 3, 4, 4]
unique = list(set(nums))

print(unique)

**Problem 2:** Write a program to find common elements between two sets.

a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))

**Problem 3:** Write a program to find the union of two sets.

a = {1, 2}
b = {3, 4}

print(a.union(b))

**Problem 4:** Write a program to find the difference between two sets.

a = {1, 2, 3}
b = {2, 4}

print(a.difference(b))

**Problem 5:** Write a program to check whether one set is a subset of another.

a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))

## Conclusion

Today’s practice helped me strengthen my understanding of dictionaries and sets. Solving problems gave me more confidence and improved my problem-solving skills.
