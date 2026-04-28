#  Day 8: Java – Increment and Decrement Operators

Today I learned about increment and decrement operators in Java and how they work in different situations. These operators are very useful while working with loops and counters.

---

## What I Learned

* Increment operator (`++`)
* Decrement operator (`--`)
* Difference between pre and post operators
* How values change during execution

---

## Increment Operator (`++`)

The increment operator is used to increase the value of a variable by 1.

### Example:

```java id="f2k9p1"
public class Main {
    public static void main(String[] args) {

        int a = 5;
        a++;

        System.out.println(a);
    }
}
```

---

## Decrement Operator (`--`)

The decrement operator is used to decrease the value of a variable by 1.

### Example:

```java id="k8m3z2"
public class Main {
    public static void main(String[] args) {

        int a = 5;
        a--;

        System.out.println(a);
    }
}
```

---

## Pre-Increment (++a)

Value is increased first, then used.

### Example:

```java id="p4t7x9"
public class Main {
    public static void main(String[] args) {

        int a = 5;

        int b = ++a;

        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}
```

---

## Post-Increment (a++)

Value is used first, then increased.

### Example:

```java id="r6n1y8"
public class Main {
    public static void main(String[] args) {

        int a = 5;

        int b = a++;

        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}
```

---

## Pre-Decrement (--a)

Value is decreased first, then used.

### Example:

```java id="v9q2w5"
public class Main {
    public static void main(String[] args) {

        int a = 5;

        int b = --a;

        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}
```

---

## Post-Decrement (a--)

Value is used first, then decreased.

### Example:

```java id="u3k8m7"
public class Main {
    public static void main(String[] args) {

        int a = 5;

        int b = a--;

        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}
```

---

## Advantages

* Simple and quick way to update values
* Makes code shorter and cleaner
* Very useful in loops and counters
* Improves readability when used properly

---

## Disadvantages

* Can be confusing for beginners (pre vs post)
* May reduce readability if overused in complex expressions
* Mistakes can lead to logical errors
* Hard to debug when used inside larger expressions

---

## Key Understanding

* `++` increases value by 1
* `--` decreases value by 1
* Pre operators change value first
* Post operators use value first, then change
* These operators are widely used in loops

---

## Conclusion

Today’s learning helped me understand how increment and decrement operators work in Java and how pre and post operations affect the output. This is important for writing efficient programs, especially when using loops.
