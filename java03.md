#  Day 12: Java – Examples, Literals, Characters, Input, and Operators

Today I continued learning Java and focused on understanding literals, characters, user input, and arithmetic operations through practical examples.

---

## Example

### Example 1: Basic Data Types

```java
public class Main {
    public static void main(String[] args) {
        int a = 10;
        float b = 5.2f;
        char c = 'A';
        String name = "Java";

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(name);
    }
}
```

---

### Example 2: Multiple Values

```java
public class Main {
    public static void main(String[] args) {
        byte b = 10;
        short s = 100;
        long l = 10000L;

        System.out.println(b + " " + s + " " + l);
    }
}
```

---

### Example 3: Simple Output

```java
public class Main {
    public static void main(String[] args) {
        int x = 5;
        int y = 2;

        System.out.println("Result: " + (x + y));
    }
}
```

---

## Literals

Literals are constant values assigned directly to variables. They represent fixed data stored in memory.

### Types of Literals:

* Integer → `10, 20`
* Floating → `5.2, 3.14`
* Character → `'A'`
* Boolean → `true, false`
* String → `"Java"`

### Example:

```java
int a = 10;
float b = 5.2f;
char c = 'A';
boolean flag = true;
String str = "Hello";
```

---

## Characters in Java

A character represents a single letter, digit, or special symbol and is written inside single quotes.

* Stored in **2 bytes (16 bits)**
* Uses **UTF-16 encoding**
* ASCII is a subset of Unicode

### Common ASCII Values:

* `'A' → 65`
* `'a' → 97`
* `'0' → 48`

### Example:

```java
public class Main {
    public static void main(String[] args) {
        char ch = 'A';

        System.out.println(ch);
        System.out.println((int) ch); // ASCII value
    }
}
```

---

## User Input in Java

Java uses the `Scanner` class to take input from the user.

### Example:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.println("Hello " + name);
    }
}
```

---

## Addition of Two Numbers

### Example:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        int sum = a + b;
        System.out.println("Sum = " + sum);
    }
}
```

---

## Arithmetic Operators

Arithmetic operators are used to perform basic mathematical operations.

* `+` → Addition
* `-` → Subtraction
* `*` → Multiplication
* `/` → Division
* `%` → Modulus

### Example:

```java
public class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;

        System.out.println("Addition: " + (a + b));
        System.out.println("Subtraction: " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division: " + (a / b));
        System.out.println("Modulus: " + (a % b));
    }
}
```

---

## Conclusion

Today’s learning helped me understand how Java handles literals, characters, and user input. I also practiced writing programs using arithmetic operations, which are essential for building logic in Java.
