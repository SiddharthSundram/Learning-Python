'''
    * String is a collection of alpha numeric and special characters.
    * String is immutable as insert, delete , update operations can't be carried out on a given string.
'''
# mystr = "university"
# print(mystr,len(mystr),type(mystr),id(mystr))

# # indexing
# print(mystr[6],mystr[-4],mystr[8],mystr[-2],mystr[9],mystr[-1])  

# #slicing
# print(mystr[1:6],mystr[-9:-4],mystr[1:-4],mystr[-9:6])
# print(mystr[0:6],mystr[:6],mystr[-10:-4],mystr[:-4])
# print(mystr[6:],mystr[-4:])
# print(mystr[3:6],mystr[-7:-4],mystr[3:-4],mystr[-7:6])
# print(mystr[::2],mystr[1::2])
# print(mystr[::-1]) # reverse the string



## case method
# mystr = "tEChno iNDia uNIveRSiTy"
# print(mystr,len(mystr),type(mystr),id(mystr))
# print(mystr.upper())
# print(mystr.lower())
# print(mystr.casefold())
# print(mystr.swapcase())
# print(mystr.capitalize())
# print(mystr.title())


## bool check
# mystr = "abcd"
# print(mystr,mystr.isalpha(),mystr.isalnum(),mystr.isdigit(),mystr.isnumeric())
# mystr = "1234"
# print(mystr,mystr.isalpha(),mystr.isalnum(),mystr.isdigit(),mystr.isnumeric())
# mystr = "1234abcd"
# print(mystr,mystr.isalpha(),mystr.isalnum(),mystr.isdigit(),mystr.isnumeric())
# mystr = "abcd@1234"
# print(mystr,mystr.isalpha(),mystr.isalnum(),mystr.isdigit(),mystr.isnumeric())



# mystr = "charity begins at home"
# print(mystr,len(mystr),type(mystr),id(mystr))
# print(mystr.startswith("charity"))
# print(mystr.startswith("begi"),mystr.startswith("begi",8),mystr.startswith('begi',8,20),mystr.startswith("begi",8,11))
# print(mystr.endswith('home'),mystr.endswith('at'),mystr.endswith('at',0,17),mystr.endswith('at',15,17))


## find mehtod
# mystr = "charity begins at home"
# print(mystr,len(mystr),type(mystr),id(mystr))
# print(mystr.find("begins"))
# print(mystr.find("at"))
# print(mystr.find("school")) # if not found return -1
# print(mystr.find("home"))


# ## index method
# mystr = "charity begins at home"
# print(mystr,len(mystr),type(mystr),id(mystr))
# print(mystr.index("begins"))
# print(mystr.index("home"))
# print(mystr.index("school")) ## will return valueError : substring not found
# print(mystr.index("at"))


## using try and except method to cath error
# mystr = "charity begins at home"
# print(mystr,len(mystr),type(mystr),id(mystr))
# try:
#     print(mystr.index("begins"))
#     print(mystr.index("at"))
#     print(mystr.index("school")) ## will return valueError : substring not found
# except ValueError as ve:
#     print("Unsuccessful search has taken place !!!") 
#     print("Error message:",ve)
#     print(mystr.index("home"))


## count method
# mystr = 'mississippi'
# print(mystr,len(mystr),type(mystr),id(mystr))
# print(mystr.count('i'),mystr.count('p'))

# ## replace method
# mystr = 'Good morning'
# print(mystr,len(mystr),type(mystr),id(mystr))
# print(mystr.replace('morning', 'night'))
# print(mystr,len(mystr),type(mystr),id(mystr))

## strip method
# mystr = '   Good    morning     '
# print(mystr,len(mystr),type(mystr),id(mystr))

# result = mystr.strip()
# print(result,len(result))
# result = mystr.lstrip()
# print(result,len(result))
# result = mystr.rstrip()
# print(result,len(result))

# mystr = '#@@#good#@##morning@#@'
# print(mystr,len(mystr),type(mystr),id(mystr))

# result = mystr.strip('#@')
# print(result,len(result))
# result = mystr.lstrip('@#')
# print(result,len(result))
# result = mystr.rstrip('#@')
# print(result,len(result))


## split method (string --> list)
# mystr = 'charity begins at home'
# print(mystr,len(mystr),type(mystr),id(mystr))

# result = mystr.split()
# print(result,len(result))
# result = mystr.split('i')
# print(result,len(result))

# result = mystr.split('x')
# print(result,len(result))


## list ---> string
# lst1 = ['charity', 'begins', 'at', 'home']
# print(lst1,len(lst1),type(lst1),id(lst1))

# mystr = " ".join(lst1)
# print(mystr,len(mystr),type(mystr),id(mystr))

# mystr = ", ".join(lst1)
# print(mystr,len(mystr),type(mystr),id(mystr))

# mystr = " - ".join(lst1)
# print(mystr,len(mystr),type(mystr),id(mystr))

# ## itetrating string
# mystr = "university"
# for i in range(len(mystr)):
#     print(mystr[i], end=", ")

# print()
# for i in mystr:
#     print(i , end=", ")

## find vowels and consonent in a string
mystr = input("Enter a string: ").lower()
vcount = ccount = 0
for i in mystr:
    if(i.isalpha()):
        if(i in 'aeiou'): vcount+=1
        else: ccount+=1
print(f"The number of vowel is {vcount} and consonent is {ccount}.")