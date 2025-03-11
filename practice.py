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


## 28. find vowels and consonent in a string
# mystr = input("Enter a string: ").lower()
# vcount = ccount = 0
# for i in mystr:
#     if(i.isalpha()):
#         if(i in 'aeiou'): vcount+=1
#         else: ccount+=1
# print(f"The number of vowel is {vcount} and consonent is {ccount}.")


# ## 29.Create a countdown function  
# import time
# def countDown(user_time):
#     while user_time > 0:
#         min ,sec = divmod(user_time,60)
#         timer = '{:02d}:{:02d}'.format(min,sec)
#         time.sleep(1)
#         user_time -= 1
#     print("Countdown Off !!!")
    
# if __name__ == '__main__':
#     user_time = int(input("Enter a time in second: "))
#     countDown(user_time)

## sum of all element of list
# l = [1,2,3,4,5,6,7,8,99,10]
# total = 0
# for i in l:
#     total += i
# print(f"Total is {total}")

## concatnate lists
# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = l1+l2
# print(l1)
# print(l2)
# print(l3)

## * operation
# l1 = [1,2,3]
# l3 = l1* 10 ## will repeate 10 times the list l1
# print(l3)


## 30. Write a Python program to check whether a string is palindrome or not ?
# def palindrome(str1):
#     i = len(str1)-1
#     new_str =''
#     while i>= 0:
#         new_str += str1[i]
#         i -= 1
#         if new_str == str1:
#             return f"{str1} is a palindrome."
#         else:
#             return f"{str1} is not a palindrome." 
# str1 = input("Enter a string: ")
# print(palindrome(str1))

## 31. Write  a Python program to Count the Number of matching characters in a pair of string.
# def countChar(str1,str2):
#     c = 0
#     found = ''
#     for i in str1:
#         if i in str2:
#             if i in found:
#                 continue
#             else:
#                 c += 1
#                 found += i
#         else:
#             pass
#     return f"Total characters match found in both string is : {c}."
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# print(countChar(str1,str2))


## another method
# def count(str1 ,str2) :
#         set_string1 = set(str1)
#         set_string2 = set(str2)
#         matched_characters = set_string1 & set_string2
#         print("No. of matching characters are : " + str(len(matched_characters)) )
# str1 = 'aabcddekll12@'
# str2 = 'bb2211@55k'
# count( str1 , str2 )

## 32. Write a python program to Remove all duplicates from a given string.
# str1 = input("Enter a string: ")
# str1 = set(str1)
# found = ''
# for i in str1:
#     if i in found:
#         pass
#     else:
#         found += i
# print(found)    
# print(str(str1))

## another way
# def removeDuplicate(str):
#     s=set(str)
#     s="".join(s)
#     print("Without Order:",s)
#     t=""
#     for i in str:
#         if(i in t):                               
#             pass
#         else:
#             t=t+i
#     print("With Order:",t)
# str=input("Enter a string: ")
# removeDuplicate(str)


## 33. remove bracket form an algebric expression.
# def removeBracket(str1):
#     for i in str1:
#         if i not in '()':
#             print(i,end='')
# str1 = input("Enter an expression: ")
# removeBracket(str1)


##34. write a program that accept filename as a input form user. Open the file and count the number of times a character apperas in file.
# filename = input("Enter filename (Ex:- filename.txt) : ")
# with open(filename) as file:
#     text = file.read() 
#     letter = input("Enter the caracter to be searched: ")
#     count = 0
#     for char in text:
#         if char == letter:
#             count +=1
# print("Count: ", count)

##35. write a program to copy first 10 bites of a binary file into another.
# with open('file.txt','rb') as file:
#     with open("newFile.txt",'wb') as file2:
#         buffer = file.read(10)
#         file2.write(buffer)
# print("File copied.")


# ## 36. Write a python program to match a string that has an 'a' followed by anything,ending in 'b'.
# import re
# def matching(text):
#     pattern = 'a.*?b$' ## .(dot)-> repersent 1 character,* -> represent any number of character and repeated multiple times and $ -> indicate ending with b
#     if re.search(pattern,text):
#         print("Match found.")
#     else:
#         print("Match not found.")
# matching('abosrb')
# matching('apple')
# matching('plafjjkafjkje')
# matching('addressaahhufapleB')  # match not found as it is case sensetive


## 37. Write a python program that matches a string that only upper case letters
# import re
# def matching(text):
#     pattern = '^[A-Z]*$'
#     if re.search(pattern,text):
#         print("Match found")
#     else:
#         print("Match not found")
# matching('APPLE')
# matching('abbee')


## 38. Write a python program that matches a string that only lower case letters
# import re
# def matching(text):
#     pattern = '^[a-z]*$'
#     if re.search(pattern,text):
#         print("Match found")
#     else:
#         print("Match not found")
# matching('APPLE')
# matching('abbee')


## 39. Write a python program that matches a string that has lower and upper case letters ,digits ,underscore (_)
# import re
# def matching(text):
#     pattern = '^[a-zA-Z0-9_]*$'
#     if re.search(pattern,text):
#         print("Match found")
#     else:
#         print("Match not found")
# matching('APPLE')
# matching('_AP98artyPLE')
# matching('abbee44')
# matching('Abbee_65')


## 40. Write python program that matches a word contaning z.
# import re
# def matching(text):
#     pattern = '\w*z.\w*'
#     if re.search(pattern,text):
#         print("Match found")
#     else:
#         print("Match not found")
# matching('abbeezhhh')
# matching('APPLE664')
# matching('_AP98artyPLE')
# matching('Abbee_65')

## 41. Write a Python program to count the number of characters (character frequency) in a string.
# s = input("Enter a string: ")
# count = ''
# for i in s:
#     n = s.count(i)
#     if n > 1:
#         if i in count:
#             continue
#         count += i
#     print(f"{i} occurs {n} times in {s}.")
        
## another
# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))

## 42. Write a Python program to count the occurrences of each word in a given sentence.
# def word_count(str):
#     counts = dict()
#     words = str.split()
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#     return counts
# print( word_count('the quick brown fox jumps over the lazy dog.'))


## 43. Write a program to Reverse a List in Python.
# lst = [1,2,8,3,5]
# rev = lst[::-1]
# print(rev)


'''
46. Write a Python program to remove all the duplicated tuples from the given list.
Examples:
Input : [(1, 2), (5, 7), (3, 6), (1, 2)]
Output : [(1, 2), (5, 7), (3, 6)]

'''
# def removeDuplicates(lst):
#     return [t for t in (set(tuple(i) for i in lst))]
# lst = [(1, 2), (5, 7), (3, 6), (1, 2)]
# print(removeDuplicates(lst))

# # Another method
# list_input=[(1,2),(2,3),(3,4),(2,3)]
# output=list(set(list_input))
# print(output,type(output))

'''
 45. Remove adjacent duplicate characters from a string
Given a string, remove adjacent duplicates characters from it. In other words, remove all consecutive
same characters except one.
For example,
Input:  AABBBCDDD
Output: ABCD

'''
# def remove_adjacent_duplicates(s):
#     result = []
#     for i in range(len(s)):
#         if i == 0 or s[i] != s[i - 1]:
#             result.append(s[i])
#     return ''.join(result)
# input_string = "aaabbccdaa"
# output_string = remove_adjacent_duplicates(input_string)
# print("String after removing adjacent duplicates:", output_string)


## WAP to take a list from user and print alternative elements.
# l=[]
# n = int(input("How many element you want to enter: "))
# print(f'Enter {str(n)} elements.')
# for i in range(n):
#     l.append(int(input("Enter element: ")))
# print(f"The element in the list is : {l}")
# print("Alternate elements are: ")
# for i in range(0,n,2):
#     print(l[i])
    

## WAP to find maximum element from the list
l=[]
n = int(input("How many element you want to enter: "))
print(f'Enter {str(n)} elements.')
for i in range(n):
    l.append(int(input("Enter element: ")))
print(f"The list is : {l}")
max = 0
for i in range(0,n):
    if l[i] > max:
        max = l[i]
print(f"The maximum value is : {max}")