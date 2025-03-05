## path module
# import sys
# print(f"Python Path\n{sys.path}")

## using math module
# from math import pi
# def area(r):
#     return pi*r**2
# print(area(3))

# from math import sqrt as squre_root
# print(squre_root(81))

# import math
# x = 3.9
# y = 4
# z = 3
# print(math.ceil(x))
# print(math.floor(x))
# print(math.sqrt(y))
# print(math.pow(y,z))

## **---  creating our own module  ---**
# import My_module
# n = int(input("Enter a value: "))
# a = int(input("Enter a value: "))
# b = int(input("Enter a value: "))
# print(f"\nFibonacci Term : {My_module.fib(n)}")
# print(f"Factorial value : {My_module.fact(n)}")
# print(f"Large value : {My_module.large(a,b)}")
# print(f"Small value : {My_module.small(a,b)}")


## creating OTP 
# import random, math
# def generateOTP():
#     digits = "0123456789"
#     OTP = ""
#     for i in range(1,5):
#         a = random.random()
#         b = math.floor(a*10)
#         OTP += digits[b]
#     return OTP
# print(f"OTP of 4 digits : {generateOTP()}")

## another way
# import random, math
# def generateOTP():
#     OTP = ""
#     for i in range(1,5):
#         a = random.random()
#         b = math.floor(a*10)
#         OTP += str(b)
#     return OTP
# print(f"OTP of 4 digits : {generateOTP()}")