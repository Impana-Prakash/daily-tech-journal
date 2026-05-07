

# Day-16: Python DSA Problems and Solutions

## 1. Reverse a String

### Problem

Write a function to reverse a string.

### Solution

```python
s = input("Enter a string: ")
print(s[::-1])
```

---

## 2. Check Prime Number

### Problem

Check whether a number is prime or not.

### Solution

```python
n = int(input("Enter number: "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
```

---

## 3. Fibonacci Series

### Problem

Print Fibonacci series up to n terms.

### Solution

```python
n = int(input("Enter number of terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

---

## 4. Palindrome Check

### Problem

Check whether a string is palindrome.

### Solution

```python
s = input("Enter string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

## 5. Find Largest Element in Array

### Problem

Find the largest element in a list.

### Solution

```python
arr = list(map(int, input().split()))

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest:", largest)
```

---

## 6. Bubble Sort

### Problem

Sort an array using Bubble Sort.

### Solution

```python
arr = list(map(int, input().split()))

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
```

---

## 7. Factorial of a Number

### Problem

Find factorial of a number.

### Solution

```python
n = int(input("Enter number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)
```

---

## 8. Count Vowels in a String

### Problem

Count vowels in a string.

### Solution

```python
s = input("Enter string: ")

count = 0
vowels = "aeiouAEIOU"

for ch in s:
    if ch in vowels:
        count += 1

print("Vowels:", count)
```

---

## 9. Linear Search

### Problem

Search an element in an array.

### Solution

```python
arr = list(map(int, input().split()))
key = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Element not found")
```

---

## 10. Armstrong Number

### Problem

Check whether a number is an Armstrong number.

### Solution

```python
n = int(input("Enter number: "))

num = n
power = len(str(n))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** power
    num //= 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
```

---

## 11. Kadane’s Algorithm

### Problem

Find the maximum subarray sum.

### Solution

```python
arr = list(map(int, input().split()))

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print("Maximum Subarray Sum:", max_sum)
```

---

## 12. Binary Search

### Problem

Perform Binary Search on a sorted array.

### Solution

```python
arr = list(map(int, input().split()))
key = int(input("Enter element to search: "))

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == key:
        print("Element found at index", mid)
        break
    elif arr[mid] < key:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Element not found")
```

---

# Conclusion

These Python programs cover beginner to intermediate-level Data Structures and Algorithms concepts including searching, sorting, arrays, strings, and mathematical problems. They are useful for coding practice, interviews, and GitHub portfolio projects.
