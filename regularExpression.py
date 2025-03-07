## match(pattern,string) - search only at begining of the string
# import re   #importing regular expression
# string = "She sells sea shells on she shore."
# pattern1 = 'sells'
# pattern2 = 'She'
# if re.match(pattern1,string):
#     print('Pattern1 Match found.')  # will not print this because match function search only at begining of the string
# elif re.match(pattern2,string):
#     print('Pattern2 Match found.') # will be printed because found at begining
# else:
#     print("No match found.")

## search(pattern,string) - search entire string
# import re
# string = "She sells sea shells on she shore."
# pattern = 'sells'
# if re.search(pattern,string):
#     print('Pattern Search found.')  # will print this because search() search entire string
# else:
#     print("No search found.")
    
## sub(pattern,replpacement_string,string,max=0) - will replace the patter in a string upto max time (like : 1 ,2,3,...)
# import re
# string = "She sells sea shells on sea shore."
# pattern = 'sea'
# repl ='Ocean'
# new_str =  re.sub(pattern,repl,string, 1)  #  will replace stirng upto max limti (for entire string to be replaced with pattern change max to 0) 
# print('Pattern is replaced: ',new_str)


## findall(pattern,input_str,flags=0)
# import re
# pattern = r"[a-zA-Z]+ \d+"  # will search for a to z and A to Z with digit
# matches = re.findall(pattern,'LTE 302,SID 110,SLFid 839,TESLA is a car company)') 
# for i in matches:
#     print(i,end=' ') 


# ## write a python program to match a string that has an 'a' followed by anything,ending in 'b'.
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


## Write a python program that matches a string that has an 'a' followed by three 'b'.
## i/p : abbb
## o/p : match found

# import re
# def matching(text):
#     pattern = 'ab{3}?'
#     if re.search(pattern,text):
#         print("Match found")
#     else:
#         print("Match not found")
# matching('abbbliee')
# matching('abbee')
# matching('skldkdl')


## Write a python program that matches a string that only upper case letters
# import re
# def matching(text):
#     pattern = '^[A-Z]*$'
#     if re.search(pattern,text):
#         print("Match found")
#     else:
#         print("Match not found")
# matching('APPLE')
# matching('abbee')


## Write a python program that matches a string that only lower case letters
# import re
# def matching(text):
#     pattern = '^[a-z]*$'
#     if re.search(pattern,text):
#         print("Match found")
#     else:
#         print("Match not found")
# matching('APPLE')
# matching('abbee')


## Write a python program that matches a string that has lower and upper case letters ,digits ,underscore (_)
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


## Write  python program that matches a word contaning z.
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