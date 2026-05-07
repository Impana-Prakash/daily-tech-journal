# Problems in java

## 1. Reverse a String

### Explanation:

This program reverses a string using `StringBuilder`.
`reverse()` is a built-in method in Java that reverses the characters of the string.

```java id="y3gm39"
import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();

        String reversed = new StringBuilder(s).reverse().toString();

        System.out.println(reversed);
    }
}
```

---

# 2. Prime Number Check

### Explanation:

A prime number is divisible only by `1` and itself.
We check divisibility from `2` to `√n`.
If any number divides `n`, then it is not prime.

```java id="ul35ts"
import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        boolean isPrime = true;

        if (n <= 1) {
            isPrime = false;
        } else {
            for (int i = 2; i * i <= n; i++) {
                if (n % i == 0) {
                    isPrime = false;
                    break;
                }
            }
        }

        if (isPrime)
            System.out.println("Prime");
        else
            System.out.println("Not Prime");
    }
}
```

---

# 3. Fibonacci Series

### Explanation:

Fibonacci series starts with `0` and `1`.
Each next number is the sum of the previous two numbers.

Example:

```text id="m8c4r5"
0 1 1 2 3 5 8
```

```java id="jlwmqv"
import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int a = 0, b = 1;

        for (int i = 0; i < n; i++) {
            System.out.print(a + " ");

            int temp = a + b;
            a = b;
            b = temp;
        }
    }
}
```

---

# 4. Palindrome Check

### Explanation:

A palindrome reads the same forward and backward.

Examples:

```text id="9n5obq"
madam → Palindrome
level → Palindrome
java → Not Palindrome
```

We reverse the string and compare it with the original string.

```java id="vsm2jl"
import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();

        String rev = new StringBuilder(s).reverse().toString();

        if (s.equals(rev))
            System.out.println("Palindrome");
        else
            System.out.println("Not Palindrome");
    }
}
```

---

# 5. Bubble Sort

### Explanation:

Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.
After every pass, the largest element moves to the end.

Example:

```text id="9vk5j4"
Input: 5 3 1 4
Output: 1 3 4 5
```

```java id="d3o4r8"
import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {

                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        System.out.println(Arrays.toString(arr));
    }
}
```

---

# 6. Kadane’s Algorithm (Maximum Subarray Sum)

### Explanation:

Kadane’s Algorithm finds the maximum sum of a continuous subarray.

At every step:

* Either start a new subarray
* Or continue the previous subarray

Example:

```text id="l7igp0"
Input: [2, 3, -8, 7, -1, 2, 3]
Output: 11
```

Maximum subarray:

```text id="8mw6d6"
[7, -1, 2, 3]
```

```java id="e6m7wh"
import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int currentSum = arr[0];
        int maxSum = arr[0];

        for (int i = 1; i < n; i++) {
            currentSum = Math.max(arr[i], currentSum + arr[i]);
            maxSum = Math.max(maxSum, currentSum);
        }

        System.out.println("Maximum Subarray Sum: " + maxSum);
    }
}
```
