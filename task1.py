# sum of two numbers
def sum(a, b):
    return a + b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"the sum of {a} and {b} is {sum(a, b)}")

# odd or even checker
def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number to check odd/even: "))
print(f"{num} is {odd_even(num)}")

#factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")

#fabonacci sequence

