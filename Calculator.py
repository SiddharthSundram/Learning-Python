while True:
    print("Choose the operation you want to perform: ")
    print("Enter 1 : Addition.")
    print("Enter 2 : Subtraction.")
    print("Enter 3 : Multliplication.")
    print("Enter 4 : Division.")
    print("Enter 5 : Square Root.")
    print("Enter 6 : Exit.")
    i = int(input("Enter your choice: "))
    
    if(i == 1):
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        print(f"Additon: a + b = {a+b}")
    
    if(i == 2):
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        print(f"Subtraction: a - b = {a-b}")
    
    if(i == 3):
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        print(f"Multliplication: a * b = {a*b}")
    
    if(i == 4):
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        print(f"Division: a / b = {a/b}")
    
    if(i == 5):
        a = int(input("Enter first value: "))
        print(f"Square Root of a = {a ** 0.5}")
    
    if(i == 6):
        print("Thank You for using Calculator!!!")
        break