## learning list

''' *   List is a collection of data items of same or different datatypes with in square brackets.
    *   Lists items are mutable as INSERT,DELETE, AND UPDATE operations can be carried out on them.    '''

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


# lst1 = [100,500,200,400,300]
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(max(lst1), min(lst1))
# print('Sum: ',sum(lst1),'Average: ' ,sum(lst1)/len(lst1))

# lst1 = ['Monday','Friday','Thursday','Tuesday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(max(lst1), min(lst1))
# print('Sum: ',sum(lst1),'Average: ' ,sum(lst1)/len(lst1)) ## will generate unsupported  operand typeError


# lst1 = [100,500.45,200,False,400.3,True,300]
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(max(lst1), min(lst1))
# print('Sum: ',sum(lst1),'Average: ' ,sum(lst1)/len(lst1))


## indexing and slicing
# lst1 = ['Sunday','Tuesday','Friday','Saturday','Thursday']
# print(lst1[2],lst1[-3],lst1[4],lst1[-1])
# print(lst1[0::2],lst1[1::2],lst1[::-1])
# print(lst1[3],lst1[2:5],lst1[-2],lst1[-6:-3])


## defining empty list ,empty tuple, empty dictionary ,empty set , empty frozen-set
# var1 =[] # empty list
# print(var1,len(var1),type(var1),id(var1))
# var1 = () # empty tuple
# print(var1,len(var1),type(var1),id(var1))
# var1 = {} #empty dictionary
# print(var1,len(var1),type(var1),id(var1))
# var1 = set() # empty set
# print(var1,len(var1),type(var1),id(var1))
# var1 = frozenset([])
# print(var1,len(var1),type(var1),id(var1))
# var1 = (9,) # singleton representation of a tuple
# print(var1,type(var1),id(var1))


## converting string to list , tuple, set and frozen set
# mystr = "my word mississippi"
# print(mystr,len(mystr))
# result = list(mystr)
# print(result,len(result),type(result),id(result))
# result = tuple(mystr)
# print(result,len(result),type(result),id(result))
# result = set(mystr)
# print(result,len(result),type(result),id(result))
# result = frozenset(mystr)
# print(result,len(result),type(result),id(result))

