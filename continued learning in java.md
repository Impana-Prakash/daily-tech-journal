#  Day 11: Java – Memory Management, Data Types, Variables, and Examples

Today I continued learning Java and focused on understanding how Java programs work, how memory is used, and the different types of data types.

## Example

### Example 1: Hello World

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}

### Example 2: Using Variables

public class Main {
    public static void main(String[] args) {
        int a = 10;
        float b = 5.5f;

        System.out.println(a);
        System.out.println(b);
    }
}

### Example 3: Simple Calculation

public class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;

        int sum = a + b;
        System.out.println("Sum = " + sum);
    }
}

### Example 4: Using Boolean

public class Main {
    public static void main(String[] args) {
        boolean isJavaFun = true;
        System.out.println(isJavaFun);
    }
}

### Example 5: Using Character

public class Main {
    public static void main(String[] args) {
        char grade = 'A';
        System.out.println(grade);
    }
}

## Memory Management

Java manages memory automatically.

* Data is stored in **RAM** during execution
* Primitive data types are stored directly
* Objects are stored in heap memory
* Java uses **Garbage Collection** to remove unused data
* This ensures efficient memory usage

## Data Types

Java data types are divided into two categories:

### Primitive Data Types

Primitive data types are used to store simple values directly in memory and are the most basic building blocks in Java.

**1. Integer Types**
Used to store whole numbers without decimals.

* `byte` → 1 byte
* `short` → 2 bytes
* `int` → 4 bytes

**2. Floating Point Types**
Used to store decimal or fractional numbers.

* `float` → 4 bytes
* `double` → 8 bytes

**3. Character Type**
Used to store a single character.

* `char` → 2 bytes

**4. Boolean Type**
Used to store true or false values.

* `boolean` → 1 bit

### Non-Primitive Data Types

Non-primitive data types are used to store complex data and are created using classes and objects.

* String
* Array
* Class
* Object

## Variables

Variables are used to store values in a program.

### Rules:

* Variable names should not start with numbers
* Cannot use keywords as variable names
* Variables are case-sensitive
* Use meaningful variable names

## Conclusion

Today’s learning helped me understand how Java works internally, how memory is managed, and how different data types and variables are used in programs.

