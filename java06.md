#  Day 6: Java – Control Statements and Problem Solving

Today I focused on control statements in Java and practiced solving multiple problems to improve my logical thinking and coding skills.

---

## What I Practiced

* Solved **5 problems on GeeksforGeeks**
* Practiced **logical operators** (4 problems)
* Worked on **if-else statements** (5 problems)
* Solved problems on:

  * Even and odd number
  * Largest of three numbers
  * Second largest of three numbers
* Learned about **else-if ladder**

---

## Logical Operators

Logical operators are used to combine multiple conditions.

* `&&` → AND
* `||` → OR
* `!` → NOT

### Example:

```java id="l1p9x3"
public class Main {
    public static void main(String[] args) {

        int a = 10;
        int b = 20;

        System.out.println(a > 5 && b > 15);
        System.out.println(a > 15 || b > 15);
        System.out.println(!(a > 5));
    }
}
```

---

## If-Else Statement

Used to execute code based on a condition.

### Example: Even or Odd

```java id="n2k8v4"
public class Main {
    public static void main(String[] args) {

        int num = 7;

        if (num % 2 == 0) {
            System.out.println("Even");
        } else {
            System.out.println("Odd");
        }
    }
}
```

---

## Else-If Ladder

Used when there are multiple conditions to check.

### Example:

```java id="k7z3d1"
public class Main {
    public static void main(String[] args) {

        int marks = 75;

        if (marks >= 90) {
            System.out.println("Grade A");
        } else if (marks >= 75) {
            System.out.println("Grade B");
        } else if (marks >= 50) {
            System.out.println("Grade C");
        } else {
            System.out.println("Fail");
        }
    }
}
```

---

## Largest of Three Numbers

### Example:

```java id="p4x9m2"
public class Main {
    public static void main(String[] args) {

        int a = 10, b = 25, c = 15;

        if (a > b && a > c) {
            System.out.println("Largest is a");
        } else if (b > a && b > c) {
            System.out.println("Largest is b");
        } else {
            System.out.println("Largest is c");
        }
    }
}
```

---

## Second Largest of Three Numbers

### Example:

```java id="r8y2q7"
public class Main {
    public static void main(String[] args) {

        int a = 10, b = 25, c = 15;

        if ((a > b && a < c) || (a > c && a < b)) {
            System.out.println("Second largest is a");
        } else if ((b > a && b < c) || (b > c && b < a)) {
            System.out.println("Second largest is b");
        } else {
            System.out.println("Second largest is c");
        }
    }
}
```

---

## Key Understanding

* Logical operators help combine multiple conditions
* `if-else` helps in decision making
* `else-if ladder` is useful for multiple conditions
* Practicing problems improves logical thinking
* Writing full programs improves syntax clarity

---

## Conclusion

Today’s learning was focused on control statements and problem-solving. Solving multiple problems helped me improve my understanding of logic and how conditions work in Java.

