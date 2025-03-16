'''
    *   When error occurs, or exception we call it, Python will normally stop and generate error message.
    
    Example:-
        print(x)
        This will generate an error because x is not defined.
'''
## syntax
# try:
#     print('Block of that code which may have chance of error will be written in the try block.')
#     print(x)
# except:
#     print("Will handle the error here.")
#     print("something went worng !!!")


## 
# try:
#     print(x)
# except:
#     print("something went worng !!!")
# else:
#     print("Will execute bolck of code when no error occurs in the program.")


## 
# try:
#     print(x)
# except:
#     print("something went worng !!!")
# finally:
#     print("Will execute bolck of code either an error occurs in the program or not.")


## To throw or raise exception , use the raise keyword
# x = -1
# if x <0:
#     raise Exception("Sorry, numbers below are not allowed")


## Raise a TypeError if x is not an integer.
# x = 'hello'
# if not type(x) is int:
#     raise TypeError("Only integer are allowed.")




x = ('apple','mango','barry')

y = enumerate(x)
print(y)
print(list(y)) # will return in this format [(index1,value1),(index2,value2),(index3,value3)]