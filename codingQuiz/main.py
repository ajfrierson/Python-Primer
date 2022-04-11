# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

#1) Given two numbers num1 and num2. The task is to write a Python program to find the addition of these two numbers.
def add(num1, num2):
    return num1 + num2


print(add(2, 4))



# 2) Given two numbers, write a Python code to find the Maximum of these two numbers.
def get_max():
    numbers = [12, 5]
    maximum = 0
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


print(get_max())


# 3) Given two positive integers start and end. The task is to write a Python program to print all Prime numbers in an Interval.

# 4) Given a positive integer N, The task is to write a Python program to check if the number is prime or not.

# 5) Given a number \’n\’, how to check if n is a Fibonacci number. First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ..
def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(9))