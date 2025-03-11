def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

def large(a,b):
    if a > b:
        return a
    else:
        return b

def small(a,b):
    if a < b:
        return a
    else: 
        return b