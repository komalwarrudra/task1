# sum of two numbers
def sumof(a, b):
    return a + b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"the sum of {a} and {b} is {sumof(a, b)}")


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


#leap year check
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year to check if it's a leap year: "))
if is_leap_year(year):
    print("year is a leap year")
else:
    print("year is not a leap year")


# armstrong check
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num 
num = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")    