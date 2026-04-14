### Day 4: Strings, Slicing, Escape Characters, and String Functions

Today I learned about strings in Python and how to work with them using different operations.

A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.

A string is mutable we can not change the exsiting valves


## Strings in Python

# Example 1:

name = "Python"
print(name)

# Example 2:

message = 'Hello World'
print(message)

#Example 3:

text = """This is a multi-line string"""
print(text)

# Example 4:

a = "123"
print(type(a))   # string

# Example 5:

b = "Python" + " Programming"
print(b)

## String Slicing

String slicing is used to access parts of a string using index positions.

# Example 1:

text = "Python"
print(text[0:4])   # Pyth

# Example 2:

print(text[:3])    # Pyt

# Example 3:

print(text[2:])    # thon

Example 4:

print(text[::2])   # Pto

# Example 5:

print(text[-1])    # n

# Example 6:

print(text[::-1])  # nohtyP (reverse)

## Escape Characters

Escape characters are used to include special characters in a string.

# Example 1:

print("Hello\nWorld")

Example 2:

print("Hello\tWorld")

# Example 3:

print("She said \"Hi\"")

# Example 4:

print('It\'s Python')

# Example 5:

print("Line1\nLine2\nLine3")

## String Functions

Python provides built-in functions to manipulate strings.

# Example 1:

text = "python programming"
print(text.upper())

# Example 2:

print(text.lower())

# Example 3:

print(text.title())

Example 4:

print(text.capitalize())

# Example 5:

print(text.replace("python", "java"))

# Example 6:

print(len(text))

# Example 7:

print(text.strip())   # removes spaces from both sides

# Example 8:

print(text.lstrip())  # removes left spaces

# Example 9:

print(text.rstrip())  # removes right spaces

# Example 10:

print(text.find("programming"))  # returns index

# Example 11:

print(text.count("m"))  # count occurrences

# Example 12:

print(text.startswith("python"))
print(text.endswith("ing"))

## Conclusion

Today’s learning helped me understand how to create and manipulate strings in Python. These concepts are very useful and are used in almost every Python program
