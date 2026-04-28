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
def fab(num):
    a, b = 0, 1
    for i in range(num):
        print(a, end=' ')
        a, b = b, a + b
    print()  
num = int(input("Number of terms for Fibonacci sequence: "))
fab(num)    

#reverse string
s = input("Enter a string to reverse: ")
reversed_string = ""
for char in s:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)

#palindrome checker
s = input("enter to check palindrom ")
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)

if s == reversed_s:
    print("The string is a palindrome.")
else:
    print("not a palindrome")