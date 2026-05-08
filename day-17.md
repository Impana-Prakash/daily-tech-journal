
# Day-17: Problems in Python

## 1. Armstrong Number

### Explanation:

An Armstrong number is a number equal to the sum of its digits raised to the power of total digits.

Example:

```text id="arm11"
153 = 1³ + 5³ + 3³
```

```python id="arm53"
n = int(input("Enter a number: "))

temp = n
power = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
```

---

## 2. Linear Search

### Explanation:

Linear Search checks each element one by one until the target is found.

```python id="lin29"
arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")
```

---

## 3. Count Vowels in a String

### Explanation:

This program counts the number of vowels (`a, e, i, o, u`) in a string.

```python id="vow74"
s = input("Enter a string: ")

count = 0
vowels = "aeiouAEIOU"

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
```

---

## 4. Factorial of a Number

### Explanation:

Factorial of a number is the product of all positive integers up to that number.

Example:

```text id="fac12"
5! = 5 × 4 × 3 × 2 × 1 = 120
```

```python id="fac91"
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)
```

---

## 5. Binary Search

### Explanation:

Binary Search works only on sorted arrays.
It repeatedly divides the search space into half.

```python id="bin65"
arr = list(map(int, input("Enter sorted elements: ").split()))
target = int(input("Enter element to search: "))

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print("Element found at index", mid)
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

else:
    print("Element not found")
```
