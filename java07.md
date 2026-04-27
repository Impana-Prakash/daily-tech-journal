#  Day 7: Java – Switch Statement and Problem Solving

Today I practiced problem solving and learned about the `switch` statement in Java in detail. This helped me understand how to handle multiple conditions in a clean and structured way.

---

## What I Practiced

* Solved **Leap Year problem**
* Learned **switch statement in detail**
* Understood rules, properties, advantages, and limitations
* Practiced multiple examples using switch

---

## Program: Leap Year Check

A year is a leap year if:

* It is divisible by 4
* Not divisible by 100 unless also divisible by 400

### Example:

```java id="s1k9x2"
public class Main {
    public static void main(String[] args) {

        int year = 2024;

        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            System.out.println("Leap Year");
        } else {
            System.out.println("Not a Leap Year");
        }
    }
}
```

---

## Switch Statement

The `switch` statement is used to select one block of code from multiple options based on a value.

---

## Syntax

```java id="x4p8z1"
switch (expression) {
    case value1:
        // code
        break;

    case value2:
        // code
        break;

    default:
        // code
}
```

---

## Important Points

* `default` is **not compulsory**
* Duplicate `case` values are **not allowed**
* `float` is **not allowed** (due to precision issues)
* Expression inside `switch` must return:

  * `int`, `char`, `byte`, `short`, `String`
* Expressions are **allowed in switch**, but
* Expressions are **not allowed in case labels** (must be constant values)

---

## Examples

### Example 1: Basic Switch

```java id="k7v2m3"
public class Main {
    public static void main(String[] args) {

        int day = 2;

        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            default:
                System.out.println("Invalid");
        }
    }
}
```

---

### Example 2: Without Break (Fall-through)

```java id="n3x8q5"
public class Main {
    public static void main(String[] args) {

        int num = 1;

        switch (num) {
            case 1:
                System.out.println("One");
            case 2:
                System.out.println("Two");
            default:
                System.out.println("Done");
        }
    }
}
```

---

### Example 3: Using Char

```java id="z8k1p4"
public class Main {
    public static void main(String[] args) {

        char grade = 'A';

        switch (grade) {
            case 'A':
                System.out.println("Excellent");
                break;
            case 'B':
                System.out.println("Good");
                break;
            default:
                System.out.println("Average");
        }
    }
}
```

---

### Example 4: Using String

```java id="q2m9t6"
public class Main {
    public static void main(String[] args) {

        String role = "admin";

        switch (role) {
            case "admin":
                System.out.println("Access granted");
                break;
            case "user":
                System.out.println("Limited access");
                break;
            default:
                System.out.println("No access");
        }
    }
}
```

---

### Example 5: Expression in Switch

```java id="r5p3k9"
public class Main {
    public static void main(String[] args) {

        int a = 10;
        int b = 20;

        switch (a + b) {
            case 30:
                System.out.println("Sum is 30");
                break;
            default:
                System.out.println("Other value");
        }
    }
}
```

---

## Key Properties of Switch

* Used for multi-way decision making
* Improves readability compared to multiple `if-else`
* Works with fixed values (constants)
* Supports `int`, `char`, `String` types
* Uses `break` to stop execution

---

## Advantages

* Cleaner and more readable code
* Easier to manage multiple conditions
* Faster than multiple `if-else` in some cases
* Good for menu-driven programs

---

## Disadvantages

* Cannot handle complex conditions
* Only works with specific data types
* No support for ranges (like `>`, `<`)
* Missing `break` may cause errors (fall-through)

---

## Conclusion

Today’s learning helped me understand how the switch statement works and when to use it. Practicing different examples made it easier to understand its behavior and limitations.
