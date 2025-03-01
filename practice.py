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


# 11.to display the given integer in reverse
# n = int(input("Enter a numbers to display the given integer in reverse "))
# rev = 0
# while n>0:
#     d = n% 10
#     rev = (rev*10)+ d  
#     n = n // 10
# print(rev)
