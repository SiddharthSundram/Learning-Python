

# ## Set
# set1 = {1,2,3,4}
# set2 = {5,6,7,8}
# print(set1,type(set1))
# print(set())# creating empty set
# print(1 in set1) # way to check that element 1 is in set1 or not
# print(9 in set2) # way to check that element 9 is in set2 or not


# lang = {'c','c++','python','java','js','c++'}
# print(lang,type(lang),len(lang),id(lang))
# print()


# #forming a set form tuple
# lang = set(('c','c++','python','java','js','c++'))
# print(lang,type(lang),len(lang),id(lang))
# print()

# #formin a set
# lang = {'c','c++','python','java','js','c++'}
# print(lang,type(lang),len(lang),id(lang))
# print()


# substraction 
# lang = {'c','c++','python'}
# print(lang,type(lang),len(lang),id(lang))

# snack = {'wiper','python','cobra'}
# print(snack,type(snack),len(snack),id(snack))

# result = lang.difference(snack)
# print(result,type(result),len(result),id(result))

# result = lang - snack
# print(result,type(result),len(result),id(result))



# lang.difference_update(snack)
# print(lang,type(lang),len(lang),id(lang))
# print(snack,type(snack),len(snack),id(snack))



# # symetric diff
# lang = {'c','c++','python'}
# print(lang,type(lang),len(lang),id(lang))

# snack = {'wiper','python','cobra'}
# print(snack,type(snack),len(snack),id(snack))

# result = lang.symmetric_difference(snack)
# print(result,type(result),len(result),id(result))


# result = lang ^ snack
# print(result,type(result),len(result),id(result))


# # intersection update
# lang = {'c','c++','python'}
# print(lang,type(lang),len(lang),id(lang))

# snack = {'wiper','python','cobra'}
# print(snack,type(snack),len(snack),id(snack))

# result = lang.intersection(snack)
# print(result,type(result),len(result),id(result))


# result = lang & snack  # & sumbol of inteersction
# print(result,type(result),len(result),id(result))

# lang.intersection_update(snack)
# print(lang,type(lang),len(lang),id(lang))



# lang = {'c','c++','python'}
# print(lang,type(lang),len(lang),id(lang))

# snack = {'wiper','python','cobra'}
# print(snack,type(snack),len(snack),id(snack))

# result = lang.union(snack)
# print(result,type(result),len(result),id(result))


# result = lang |snack  # | sumbol of union
# print(result,type(result),len(result),id(result))