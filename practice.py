## 1.odd or even check
# num1 = int(input("Enter a number to check whether it is even or odd: "))

# if(num1 % 2 == 0):
#     print(f"{num1} is even number.")
# else:
#     print(f"{num1} is odd number.")
    
# ## checking multiple of both 5 and 7
# num1 = int(input("Enter a number to check whether it is multiple of both 5 and 7 : "))
# if(num1 % 5 == 0 ) and (num1 % 7 == 0):
#     print(f"{num1} is multiple of both 5 and 7 .")
# else:
#     print(f"{num1} is not multiple of both 5 and 7 .")


## 2.root of quadratic equation

# import math

# def find_roots(a, b, c):
#     discriminant = b**2 - 4 * a * c

#     if discriminant > 0:
#         root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#         return (root1, root2)
#     elif discriminant == 0:
#         root = -b / (2 * a)
#         return (root,)
#     else:
#         real_part = -b / (2 * a)
#         imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
#         return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))

# if a == 0:
#     print("'a' cannot be zero for a quadratic equation.")
# else:
#     roots = find_roots(a, b, c)
#     print("Roots of the quadratic equation:", roots)

# # 3.sum of first n natural number
# n = int(input("Enter the value of N for the sum of first N natural numbers : "))
# i = 1
# s = 0
# while i <= n:
#     s += i
#     i += 1
# print(s)

# # 4.count of digits in a number
# n = int(input("Enter a numbers to count of its digits : "))
# c = 0
# while n > 0:
#     c += 1
#     n =n // 10
# print("Count of digits : ", c)

# # 5.display value 1 to n 
# n = int(input("Enter a numbers to display value 1 to n : "))
# for i in range(1,n+1):
#     print(i,end=' ')

# # factorial of a value
# n = int(input("Enter a numbers to calculate factorial : "))
# f = 1
# for i in range(1,n+1):
#     f *= i
# print(f"Factorial of {n} is {f}")

# # 6.cube upto n
# n = int(input("Enter a numbers to calculate cube upto n : "))
# for i in range(1,n+1):
#     print(f"The cube of {i} is {i*i*i}.")


# # 7.sum of its digit in a given number
# n = int(input("Enter a numbers to calculate sum of its digit in a given number : "))
# s = 0
# while n>0:
#     d = n% 10
#     s += d 
#     n = n // 10
# print(s)

# # 8.display multliplication of table
# n = int(input("Enter a numbers to display multliplication of table : "))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")



# # 9.find out the average of a set of integers
# c = int(input("Enter a numbers to count find out the average of a set of integers : "))
# i = 0
# s = 0
# for i in range(c):
#     n = int(input("Enter a number: "))
#     s += n
# avg = s / c
# print(f"The average of numbers are : {avg}")



# #10.generate the prime numbers from 1 to N.
# num = int(input("Enter a numbers to generate the prime numbers from 1 to N: "))
# for n in range(2,num):
#     for i in range(2,n):
#         if(n%i==0):
#             break
#     else:
#         print(n)


# #11.to display the given integer in reverse
# n = int(input("Enter a numbers to display the given integer in reverse "))
# rev = 0
# while n>0:
#     d = n% 10
#     rev = (rev*10)+ d  
#     n = n // 10
# print(rev)


##12. multliply list of given number
# def multi(numbers):
#     total = 1
#     for i in numbers:
#         total *= i
#     return total
# print(multi([1,2,3,4,5]))


## 13. factorial of any number recursively
# def fact(num):
#     if num == 1 or num == 0:
#         return 1
#     else:
#         return num*fact(num - 1)
# num = int(input("Enter a number to get its factorial: "))
# print(f"Factorial of {num} is {fact(num)}")

## 14. lambda function as a argument to a function
# def fun(f,n):
#     print(f(n))
# twice = lambda x:x*2
# thrice = lambda x:x*3
# fun(twice,4)
# fun(thrice,3)

## 15. program to find sum of first 10 natural number use lambda fn
# x = lambda :sum((range(1,11)))
# print(x())


## 16. passing lambda function as a argument of regular function
# def small(a,b):
#     if a> b:
#         return b
#     else:
#         return a
# sum = lambda x,y : x+y
# diff = lambda x,y : x-y
# print(f"Smaller of two number: {small(sum(-3,-2),diff(-1,2))}")

## 17. default agfuments 
# def student(name,course = "MCA"):
#     print(f"Name: {name}")
#     print(f"Course: {course}")
# student('Siddharth')
# student(name='Siddharth')

## 18. keyword argument : in this we can change the order of arguments 
# def  display11(name,age,salary):
#     return (f"Name : {name} \nAge : {age} \nSalary : {salary}")
# n = "Siddharth Sundram"
# a = "20"
# s = "56000000"
# result = display11(salary=s,name=n,age=a)
# print(result)

## 19. variable length args : length or number of args will multiple or unknown
# def fun(name,*subjects):
#     print(f"\n{name}is likely to read")
#     for subject in subjects:
#         print(subject)
# fun("Siddharth","Python","Java","Javascript","Typescript")

## 20. Python program to print the numbers from a given number n till 0 using recursion
# num = int(input("Enter a number to print the numbers from a given number n till 0 using recursion: "))
# def dec(n):
#     if n == 0:
#         return
#     print(n)
#     n = n-1
#     dec(n)
# dec(num)

## 21.  Python program to find the factorial of a number using recursion
# num = int(input("Enter a number to find the factorial of a number using recursion: "))
# def fact(n):
#     if n == 0 and n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(num))


## 22. Python program to find the Nth term in a Fibonacci series 
# n = int(input("Enter a number to find a Fibonacci series : "))
# fb1 = 0
# fb2 = 1
# fb3 = 0
# if n < 0:
#     print("Please enter value greater then 0.")
# elif n >= 0:
#     print(fb1)
# elif n >= 1:
#     print(fb2)
# for i in range(1,n):
#     fb3 = fb1 + fb2
#     print(fb3)
#     fb1 = fb2
#     fb2 = fb3

## 23. Python program to find the Nth term in a Fibonacci series using recursion
# num = int(input("Enter a number to find the Nth term in a Fibonacci series using recursion: "))
# def fib(n):
#     if n <= 0:
#         return ("Please enter value greater then 0.")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(num))


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

## creating our own module
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


# ## mean median mode of a given set of numbers in a list
# from statistics import mean, median,mode
# list1 = [10,23,5,36,7,8,12,43,4,6,77,99,23,123]
# print(f"Mean : {mean(list1)}")
# print(f"Median : {median(list1)}")
# print(f"Mode : {mode(list1)}")


## Calculate the square root of the sum of two numbers.
# import math
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result = a + b
# print(math.sqrt(result))

##  Calculate the circumference and area of a circle.
# import math
# r = int(input("Enter radius: "))
# circum = 2 * math.pi *r
# area = math.pi*r**2
# print(circum)
# print(area)


## Calculate the trigonometric functions of an angle.
# import math
# r = int(input("Enter an angle in degrees.: "))
# rad = math.radians(r)
# print(f"Sine : {math.sin(rad)}")
# print(f"Cosine : {math.cos(rad)}")
# print(f"Tangent : {math.tan(rad)}")



## learning list
# lst1 = [12,32,56,87,43,88,12,53,83,12,16,31]
# print(lst1[0])
# print(lst1[3])
# print(lst1[2:5])#slicing
# print(lst1[2:])
# print(lst1[:5])
# print(lst1[-1])
# print(lst1[-5])

# for i in lst1:
#     print(i)
#     print(i, end=" ")

# n = len(lst1)
# for i in range(n):
#     print(lst1[i])
    # print(lst1[i], end=" ")

# del lst1[0] #delete from list
# print(lst1)

# print(lst1.index(87)) # to find index of element

# print(lst1.count(12))  # use to count frequency of element

# print("Original :",lst1)
# lst1.append(20) # use to add element in the list
# print("After append :",lst1)

# print("Original :",lst1)
# lst1.remove(12) # use to add element in the list
# print("After remove :",lst1)

# print("Original list : ",lst1)
# lst1 = ["Hello",23,4.21,300]
# print("Modified list : ",lst1)

## multi-dimensional list
# lst2 = [[1,2,3],[4,5,6],[7,8,9]]
# print(lst2[0])
# print(lst2[0][0])
# print(lst2[0][2])
# print(lst2[2][2])

## nested list
# lst2 =[1,2,[4,5,6,7,8]]
# print(lst2)
# print(lst2[1])
# print(lst2[2])
# print(lst2[2][2])


# ## Tuple
# tpl1 = (1,2,3,4,5,6,7,7,8,9)
# print(tpl1)
# print(tpl1[1])
# print(tpl1[1:4])
# print(tpl1[1:])
# print(tpl1[:3])

# tpl2 = 1,2,3,4,5,6,7,8  # Tuple can be created by assining multiple value to single variable
# print(tpl2, type(tpl2))


# ## Set
# set1 = {1,2,3,4}
# set2 = {5,6,7,8}
# print(set1,type(set1))
# print(set())# creating empty set
# print(1 in set1) # way to check that element 1 is in set1 or not
# print(9 in set2) # way to check that element 9 is in set2 or not


## Dictionary
# dict1 = {"x":1,"y":2,"z":3}
# print(dict1, type(dict1))
# print(dict1["x"])
# dict1["y"] = 123 #changing value using assignment operator
# print(dict1)
# dict1["w"] = 30 #adding new key: value using assignment operator
# print(dict1)
# print(dict1.get("a"))    #getting value using get() by putting key in it.
# print(dict1.get("x"))    
# myDict = {1:"Siddharth",3:2,"Roll":6}
# print(myDict)


## 24. Write a Python program to display the sum of n numbers using a list.
# num =[]
# inp  = int(input("Enter limit: "))
# for i in range(inp):
#     x = int(input(f"Enter {i}th number: "))
#     num.append(x)
# print(f"Sum of n numbers using list = {sum(num)}")

##25. Write a Python program to implement linear search on a List of elements
# lmt  = int(input("Enter limit of list: "))
# list1 =[]
# for i in range(lmt):
#     x = int(input(f"Enter {i}th number: "))
#     list1.append(x)
# print("Your entered list : ",list1)
# search = int(input("Enter the search element number: "))
# found = False
# for item in range(len(list1)):
#     if list1[item] == search:
#         print(f"Element {search} is found on index {item}.")
#         found = True
#         break
# if found == False:
#     print(f"Element {search} is not found in list.")
    
## 26. Write a Python program to find the odd numbers in a List.
# lmt  = int(input("Enter limit of list: "))
# list1 =[]
# for i in range(lmt):
#     x = int(input(f"Enter {i}th number: "))
#     list1.append(x)
# print("Your entered list : ",list1)
# oddNum = []
# for item in range(len(list1)):
#     if list1[item] % 2 != 0:
#         oddNum.append(list1[item])
# print(f"Odd Number list : {oddNum}")

## 27. Write a Python program to print all the items in a dictionary.
# my_dict = {
#     "name": "Siddharth",
#     "age": 20,
#     "city": "Kolkatta",
#     "occupation": "Engineer"
# }
# print("Dictionary items:")
# for key, value in my_dict.items():
#     print(f"{key}: {value}")

