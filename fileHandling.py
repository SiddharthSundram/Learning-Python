## how to create and write in file.
# file = open('File.txt','w')
# # file.write("Hello Python World.") # for sinle line
# lines = ['Hello world.\n','This is Siddharth.','\nLearning python']
# lines2 = '\nHello i am trying to learn python from basic to advance level.\nHope my attempt will give me knowledge.'
# file.writelines(lines) ## for multiple lines 
# file.writelines(lines2)
# file.close()
# print("Data is written into the file.") ## just for confirmation 


## how to append text in existing file.
# file = open('File.txt','a')
# file.write("\nPython is very simple but powerful language.") # for sinle line
# file.close()
# print("Data is written into the file.") ## just for confirmation 


## for read operation in file.
##syntax -> fileObj.read([count])
# file = open('File.txt','r')
# print(file.read(20)) #read only 20 characters
# file.close()


## how to perform read line by line 
# file = open('File.txt','r')
# print(file.readline()) #read line one at once
# print(file.readline()) 
# print(file.readline()) 
# print(file.readlines())  ## will read all the lines in single time
# file.close()


# ## how to perform list of file
# file = open('File.txt','r')
# # syntax -> list(fileObj)
# print(list(file))  ## will read all in a list
# file.close()


# ## how to entire line of file
# file = open('File.txt','r')
# for line in file:
#     print(line)
# file.close()


## rename a existing file
## syntax -> rename(old_filename, new_filename)
# import os
# # os.rename('file.txt','Renamed_file.txt')
# os.rename('Renamed_file.txt','file.txt')  #back to  same name file.txt
# print('File name renamed.')

## remove a existing file
## syntax -> remove('filename')
# import os
# os.remove('file2.txt')  
# print('File is removed.')


## open file with "with" keyword
# with open("file.txt",'r') as file:
#     print(file.read())
# file.close()


# with open("file.txt",'r') as file:
#     line = file.readline()
#     # words= line.split()
#     # words= line.split(' ')
#     # words= line.split(',')
#     words= line.split('\n')
#     print(words)
# file.close()


# ## write a program that accept filename as a input form user. Open the file and count the number of times a character apperas in file.
# filename = input("Enter filename (Ex:- filename.txt) : ")
# with open(filename) as file:
#     text = file.read() 
#     letter = input("Enter the caracter to be searched: ")
#     count = 0
#     for char in text:
#         if char == letter:
#             count +=1
# print("Count: ", count)

## write a program to copy first 10 bites of a binary file into another.
# with open('file.txt','rb') as file:
#     with open("newFile.txt",'wb') as file2:
#         buffer = file.read(10)
#         file2.write(buffer)
# print("File copied.")