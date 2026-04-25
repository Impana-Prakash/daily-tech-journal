

#  Day 5: Java – Problem Solving using Operators and Logic

Today I focused more on solving problems in Java rather than just learning theory. I practiced writing complete programs using operators and improved my understanding of logic building.

---

## What I Practiced

* Writing complete Java programs (class, main method)
* Solving logic-based problems using arithmetic operations
* Extracting digits using division and modulus
* Working with user input
* Understanding relational (comparison) operators

---

## Program 1: Sum of Hundreds and Thousands Digit

This program calculates the sum of digits present in the **hundreds and thousands place**.

### Example:

Input: `12345`
Output: `5`

```java id="3rk0ss"
public class Main {
    public static void main(String[] args) {

        int n = 12345;

        int sum = (n / 100) % 10 + (n / 1000) % 10;

        System.out.println("Sum = " + sum);
    }
}
```

### Explanation:

* `(n / 100) % 10` → gives **hundreds digit**
* `(n / 1000) % 10` → gives **thousands digit**

---

## Program 2: Cash Denomination Problem

This program calculates how to distribute an amount using ₹100, ₹50, ₹10, and ₹1 notes.

### Example:

Input: `167`

```java id="n5t66m"
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter amount: ");
        int amount = sc.nextInt();

        int hundred = amount / 100;
        amount = amount % 100;

        int fifty = amount / 50;
        amount = amount % 50;

        int ten = amount / 10;
        amount = amount % 10;

        int one = amount;

        System.out.println("100s: " + hundred);
        System.out.println("50s: " + fifty);
        System.out.println("10s: " + ten);
        System.out.println("1s: " + one);
    }
}
```

---

## Relational (Comparison) Operators

Relational operators are used to compare two values. The result of these operations is always a **boolean value (true or false)** in Java.

### Operators:

* `>` → Greater than
* `<` → Less than
* `==` → Equal to
* `!=` → Not equal to
* `>=` → Greater than or equal to
* `<=` → Less than or equal to

---

### Example:

```java id="w17zdi"
public class Main {
    public static void main(String[] args) {

        int a = 10;
        int b = 20;

        System.out.println(a > b);   // false
        System.out.println(a < b);   // true
        System.out.println(a == b);  // false
        System.out.println(a != b);  // true
        System.out.println(a >= b);  // false
        System.out.println(a <= b);  // true
    }
}
```

---

## Key Understanding

* Java always returns **true or false** for comparisons
* It does not return `0` or `1` like some other languages
* Arithmetic operators help in solving logic-based problems
* Using `/` and `%` makes it easy to extract digits
* Writing full programs improves clarity in syntax and logic

---

## Conclusion

Today’s learning was focused on problem-solving and understanding how operators work in Java. Practicing these problems helped me improve my logical thinking and coding skills.
