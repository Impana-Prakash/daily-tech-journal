#  Day 11: Conditional Statements in Python

Today I learned about conditional statements in Python and how they are used to control the flow of a program based on certain conditions.


## What I Learned

* Using `if`, `else`, and `elif` statements
* Working with relational operators
* Using logical operators
* Understanding how conditions are evaluated in programs

## Conditional Statements

Conditional statements allow the program to make decisions based on conditions.

### Example:

age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

## if, else, elif

The `if` statement checks a condition.
The `else` block runs if the condition is false.
The `elif` clause is used to check multiple conditions.

### Examples:

**Example 1:**

num = 10

if num > 0:
    print("Positive number")

**Example 2:**

num = -5

if num > 0:
    print("Positive")
else:
    print("Negative")

**Example 3:**

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

## Relational Operators

Relational operators are used to compare values.

### Examples:

a = 10
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)

## Logical Operators

Logical operators are used to combine multiple conditions.

### Examples:

a = 10
b = 20

print(a > 5 and b > 15)
print(a > 15 or b > 15)
print(not(a > 5))

## Elif Clause

The `elif` clause allows checking multiple conditions in sequence.

### Example:

num = 0

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


## Conclusion

Today’s learning helped me understand how decision-making works in Python programs. Conditional statements are essential for controlling program flow and handling different situations effectively.

