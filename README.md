# Python Basic Logic Scripts

This repository contains a collection of fundamental Python scripts demonstrating basic mathematical operations, number checking, sequence generation, and string manipulation[cite: 2]. It is highly interactive and runs sequentially from top to bottom.

---

## 🚀 Features

The script includes implementations for the following 8 logic problems[cite: 2]:

### 🔢 Mathematics & Numbers
*   **Sum of Two Numbers:** Takes two integer inputs from the user and calculates their sum[cite: 2].
*   **Odd or Even Checker:** Uses modulo logic (`num % 2 == 0`) to determine whether a given number is odd or even[cite: 2].
*   **Factorial Calculator:** Uses a recursive function (`n * factorial(n - 1)`) to compute the factorial of a provided number[cite: 2].
*   **Fibonacci Sequence:** Generates a Fibonacci sequence up to a user-specified number of terms[cite: 2].
*   **Leap Year Check:** Evaluates if a given year is a leap year using the standard rules (`year % 4 == 0 and year % 100 != 0` or `year % 400 == 0`)[cite: 2].
*   **Armstrong Number Check:** Verifies if a number is equal to the sum of its own digits, with each digit raised to the power of the total number of digits[cite: 2].

### 🔤 String Manipulation
*   **Reverse String:** Takes an input string and uses a `for` loop to concatenate characters in reverse order[cite: 2].
*   **Palindrome Checker:** Reverses an input string and compares it directly to the original to check if it reads the same forward and backward[cite: 2].

---

## 🛠️ Usage

To run these scripts, you will need Python 3 installed on your system.

1.  Clone this repository to your local machine.
2.  Navigate to the directory and run the Python file from your terminal:
    ```bash
    python task1.py
    ```
3.  The program will run interactively and prompt you for inputs sequentially[cite: 2]. 

### Example Prompts
When executing the script, you will be asked to provide inputs such as[cite: 2]:
*   `Enter first number:`[cite: 2]
*   `Enter a number to find its factorial:`[cite: 2]
*   `Enter a string to reverse:`[cite: 2]

---

## 💻 Code Structure

The logic is contained entirely within a single file. It utilizes core Python concepts, making it an excellent reference for beginners:
*   **Functions:** Defined using `def` for reusable logic[cite: 2].
*   **Control Flow:** Utilizes `if/else` statements for decision-making[cite: 2].
*   **Loops:** Uses `for` loops for sequences and string iteration[cite: 2].
*   **I/O:** Uses `input()` to gather data and formatted f-strings in `print()` to display results[cite: 2].
