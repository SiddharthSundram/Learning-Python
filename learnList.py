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

## insert operation on list
# lst1 = ["Monday","Thursday","Tuesday","Sunday"]
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.append("Saturday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.append("Friday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.append("Wednesday")
# print(lst1,len(lst1),type(lst1),id(lst1))


# lst1 = ["Monday","Thursday","Tuesday","Sunday"]
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.insert(3,"Saturday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.insert(3,"Friday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.insert(1,"Wednesday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.insert(100,"Weekday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(lst1[7]) ## will print Weekday because python will remove all the garbage/empty space in-between Sunday and Weekday indexes



## delete operation on list

## clear method
# lst1 = ["Monday","Thursday","Tuesday","Sunday"]
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.clear()
# print(lst1,len(lst1),type(lst1),id(lst1)) # will print empty list


## del method
# lst1 = ["Monday","Thursday","Tuesday","Sunday"]
# print(lst1,len(lst1),type(lst1),id(lst1))
# del lst1
# print(lst1,len(lst1),type(lst1),id(lst1)) # will generate an nameError  because list is compeletely deleted


## remove method
# lst1 = ['Monday','Friday','Thursday','Tuesday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.remove("Monday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.remove("Friday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.remove("Tuesday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.remove("Thursday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.remove("Sunday")
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.remove("Sunday")
# print(lst1,len(lst1),type(lst1),id(lst1))  #generate valueError  as Sunday is not in list.


## pop method 

# lst1 = ['Monday','Friday','Thursday','Tuesday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.pop()
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1.pop(2)
# print(lst1,len(lst1),type(lst1),id(lst1))


## updating operation on list

# lst1 = ['Monday','Friday','Thursday','Tuesday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst1[1] = "Wednesday"
# print(lst1,len(lst1),type(lst1),id(lst1))


## list concatination 
# lst1 = ['Monday','Friday','Thursday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst2 = ['Tuesday','Sunday','Wednesday']
# print(lst2,len(lst2),type(lst2),id(lst2))

# ## using + operator
# result = lst1 +lst2  #concatination
# print(result,len(result),type(result),id(result))

# ## using extend method
# lst1.extend(lst2)  ## will add the all the elemnts of lst2 in lst1 
# print(lst1,len(lst1),type(lst1),id(lst1))

## += operator
# lst1 += lst2  ## will add the all the elemnts of lst2 in lst1 
# print(lst1,len(lst1),type(lst1),id(lst1))


## list of lists / multi-dimensional list
# lst1 = ['Monday','Friday','Thursday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# lst2 = ['Tuesday','Sunday','Wednesday']
# print(lst2,len(lst2),type(lst2),id(lst2))

# result = [lst1 ,lst2 ] #list of lists
# print(result,len(result),type(result),id(result))

## slicing
# lst1 = [['Monday', 'Thursday','Saturday','Tuesday',], ['Friday', 'Sunday']]
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(lst1[0][1],lst1[-2][-3],lst1[1][1],lst1[-1][-1])

# print(lst1[0][2][2:5],lst1[-2][-2][-6:-3])



## sort method
# lst1 = [12,34,53,11,67,85,23,78,24]
# print(lst1,len(lst1),type(lst1),id(lst1))

# lst1.sort() # will sort in existing list
# print(lst1,len(lst1),type(lst1),id(lst1))

# lst1.sort(reverse= True)
# print(lst1,len(lst1),type(lst1),id(lst1))



# lst1 = [12,34,53,11,67,85,23,78,24]
# print(lst1,len(lst1),type(lst1),id(lst1))

# result = sorted(lst1)  # will crete a new list
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(result,len(result),type(result),id(result)) 

# result = sorted(lst1, reverse=True)
# print(result,len(result),type(result),id(result))


## count method
# lst1 = ['Friday','Monday','Tuesday','Friday','Tuesday','Thursday','Friday','Tuesday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(lst1.count("Friday"), lst1.count("Tuesday"))



# lst1 = ['Friday','Monday','Tuesday','Thursday','Friday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))

# lst2 = lst1
# print(lst2,len(lst2),type(lst2),id(lst2))

# lst1[0] = "Wednesday"
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(lst2,len(lst2),type(lst2),id(lst2))  # will change both list because in python when we assign one variable to another it give its reference to the memory location 



# lst1 = ['Friday','Monday','Tuesday','Thursday','Friday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))

# lst2 = lst1
# lst2[:] = lst1
# print(lst2,len(lst2),type(lst2),id(lst2))

# lst1[1] = "Saturday"
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(lst2,len(lst2),type(lst2),id(lst2)) 


## using copy method
# lst1 = ['Friday','Monday','Tuesday','Thursday','Friday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))

# lst2 = lst1.copy()
# print(lst2,len(lst2),type(lst2),id(lst2))

# lst1[0] = "Monday"
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(lst2,len(lst2),type(lst2),id(lst2)) 


## all method
# lst1 = ['Friday','Monday','Tuesday','Thursday','Friday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(all(lst1)) ## return True when  all the term in list is true

# lst1 = ['Friday','Monday',False,'Tuesday','Thursday','Friday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(all(lst1))


## any method
# lst1 = ['Friday','Monday','Tuesday','Thursday','Friday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(any(lst1)) ## return True when any of the term in list is true

# lst1 = ['Friday','Monday',False,'Tuesday','Thursday','Friday','Sunday']
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(any(lst1))

# lst1 = [False,False,False,False]
# print(lst1,len(lst1),type(lst1),id(lst1))
# print(any(lst1))


def myFunc(mylst):
    mylst[3] = "Wednesday"

lst1 = ['Friday','Monday','Tuesday','Thursday','Sunday']
print(lst1,len(lst1),type(lst1),id(lst1))
myFunc(lst1)
print(lst1,len(lst1),type(lst1),id(lst1))
