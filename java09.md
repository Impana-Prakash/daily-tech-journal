#  Day 9: Java – For Loop, Break and Continue Statement

Today I learned about loops in Java, especially the `for` loop, and also understood how `break` and `continue` statements control loop execution. These concepts are essential for writing efficient programs.

---

## What I Learned

* For loop
* Syntax of for loop
* Break statement
* Continue statement
* How loop control works

---

## For Loop

A `for` loop is used when we know how many times a block of code needs to be executed.

---

## Syntax

```java id="k8p3x1"
for(initialization; condition; update) {
    // code
}
```

---

## Example 1: Print Numbers from 1 to 5

```java id="m4q7v2"
public class Main {
    public static void main(String[] args) {

        for(int i = 1; i <= 5; i++) {
            System.out.println(i);
        }
    }
}
```

---

## Example 2: Print Even Numbers

```java id="x9n2k5"
public class Main {
    public static void main(String[] args) {

        for(int i = 2; i <= 10; i += 2) {
            System.out.println(i);
        }
    }
}
```

---

## Example 3: Sum of First 10 Numbers

```java id="p6t8m3"
public class Main {
    public static void main(String[] args) {

        int sum = 0;

        for(int i = 1; i <= 10; i++) {
            sum += i;
        }

        System.out.println("Sum = " + sum);
    }
}
```

---

## Break Statement

The `break` statement is used to immediately stop the loop execution.

---

### Example

```java id="r2w9q7"
public class Main {
    public static void main(String[] args) {

        for(int i = 1; i <= 10; i++) {
            if(i == 5) {
                break;
            }
            System.out.println(i);
        }
    }
}
```

### Output:

1
2
3
4

---

## Continue Statement

The `continue` statement skips the current iteration and moves to the next one.

---

### Example

```java id="v5k1x8"
public class Main {
    public static void main(String[] args) {

        for(int i = 1; i <= 5; i++) {
            if(i == 3) {
                continue;
            }
            System.out.println(i);
        }
    }
}
```

### Output:

1
2
4
5

---

## Advantages

* Reduces repetitive code
* Makes programs efficient
* Easy to control iterations
* Useful for solving logical problems

---

## Disadvantages

* Can create infinite loops if condition is wrong
* Nested loops may reduce readability
* Misuse of break/continue can make logic confusing

---

## Key Understanding

* `for` loop is used for fixed iterations
* `break` stops loop completely
* `continue` skips current iteration
* Loops are essential for automation

---

## Conclusion

Today’s learning helped me understand how loops work in Java and how `break` and `continue` control execution flow. These concepts are very important for problem solving and writing optimized programs.
