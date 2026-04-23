#  Day 13: Java – Type Casting

Today I learned about type casting in Java and how it helps in converting one data type into another. This concept is important when working with different types of data in a program.

---

## What is Type Casting

Type casting is the process of converting a value from one data type to another. In Java, this is mainly used when we need to work with different data types in the same program.

There are two types of type casting:

* Implicit Type Casting
* Explicit Type Casting

---

## Implicit Type Casting

Implicit type casting happens automatically when a smaller data type is converted into a larger data type.

### Key Points:

* Done automatically by Java
* No data loss occurs
* Smaller data type is converted to a larger one
* Safe and commonly used

---

### Examples:

**Example 1:**

```java
public class Main {
    public static void main(String[] args) {
        int a = 10;
        double b = a;

        System.out.println(b);
    }
}
```

---

**Example 2:**

```java
public class Main {
    public static void main(String[] args) {
        char ch = 'A';
        int num = ch;

        System.out.println(num);
    }
}
```

---

**Example 3:**

```java
public class Main {
    public static void main(String[] args) {
        float f = 5;
        double d = f;

        System.out.println(d);
    }
}
```

---

### Not Allowed in Implicit Casting

* Converting a larger data type into a smaller one
* Any conversion that may result in data loss

---

## Explicit Type Casting

Explicit type casting is done manually when we need to convert a larger data type into a smaller data type.

### Key Points:

* Done using casting operator
* May cause data loss
* Requires careful handling
* Used when implicit casting is not possible

---

### Examples:

**Example 1:**

```java
public class Main {
    public static void main(String[] args) {
        double d = 10.5;
        int i = (int) d;

        System.out.println(i);
    }
}
```

---

**Example 2:**

```java
public class Main {
    public static void main(String[] args) {
        int a = 130;
        byte b = (byte) a;

        System.out.println(b);
    }
}
```

---

**Example 3:**

```java
public class Main {
    public static void main(String[] args) {
        float f = 5.9f;
        int n = (int) f;

        System.out.println(n);
    }
}
```

---

**Example 4:**

```java
public class Main {
    public static void main(String[] args) {
        char ch = 'A';
        byte b = (byte) ch;

        System.out.println(b);
    }
}
```

---

**Example 5:**

```java
public class Main {
    public static void main(String[] args) {
        double x = 100.99;
        int y = (int) x;

        System.out.println(y);
    }
}
```

---

## Conclusion

Today’s learning helped me understand how type casting works in Java and how data can be converted between different types. This concept is very useful when handling different types of values in real programs.

---
