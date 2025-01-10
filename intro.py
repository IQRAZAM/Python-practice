#############modules and pip
#modules are used to borrow someone else code we normally have two types of modules 
# 1.build in modules (already in python )
# 2.external modules (module written by other people )
#pip is like a package manager like if you need anything it gonna fetch from intenet and install it for you 
#  print("hello world")
# import pandas
# print("hello bro","nalle beroxgar")
# import hashlib    # --> not gonna give any error bcz it is build in module 
#import tensorflow  --> giving error bcz it is not a build in module we need to download it from internet
# print(7936)
# print(6*56)  #it gives computation as well 
################escape sequence (a caracter tat can not directly be used in string so we use escape charachers ) 
# print("hello im  \n ----not ---- \n having a good timw") #new line character 
# print("what is \"this\"") #doubke quote character
# print("not now ",8,"hell",sep="~") #titl character between values 
#default separator is space
###############variable in python 
# a = 2 
# b = "greet"
# c  = True 
# d = None 
# e = complex(4,9)
# print (a , b, c, d)
# print(type(a))
# print(type(b))
# print(type(d))
# print(e)
# print(type(e))
#we can also have list and tuplet list is mutable(can be changes ) while tuplet is imutable
# list1 = [3,6,3,[6.3,0.0],["harry"]]
# print(list1)
# tuplet  = ("parrot ", "sparrow")
# print(tuplet)
# #also we have mapped data known as dict which is like dictionary in which you give a key value pair to another value 
# dict  = {"marks":678, "name":"natasha "}
# print(dict)
#everythig in Python is an object e.g dictionary is an object if yiu create a boolaen it and object as well 
#operators in python
# print(8*4) #simple multiplication operator
# print(14/9)   #will give a float number
# print(14//9)  #modular operator(floor divison) , it will remove the decimal and only give value before decinal 
# print(5**3)  #exponential operator it will give ans of 5 raise to power 3
###################type casting in python ############
#the conversion of one data type into another is known as type casting .python supports a wide variety of functions like int() , float() , dict(),list(),set() etc 
#*********explicit typecasting
# a  = "5" 
# b = "78"
# print(a + b )  #2 strings are eing concatinated 
# print(int(a) + int(b))  #typecasting is being used here changing a and b from string to integer type
#types : explicit (user ask python to convert one type of daattype into another)   2.implicit(python by inself adjust the data type e.g lower type of vaiable type convert into higher type )
#*******implicit typecasting (give value to more preffered oe )
# x = 6.87 
# y = 8
# print(x+y)
##############inputs in python ( we take inpit in python by using input finction)
# a  = input("enter name of the student ")
# print("so the name of the stdent is :" , a)
# #input is always taken as a string , for example 
# x = input("enter first number ")
# y = input("enter seconf number ")
# print(x+y)
# # print(x/y)
# # print(x-y) will give an erroer as a string 
# print(int(x) + int(y))
############strings in oyrhon 
'''apple = "baat gulu ki zikr mehek ka acha lagta hai kyun!!"
# print(apple)
# print(apple[5])
# for character in apple:
#    print(character)    #take care of syntax while using loops ion pyhhon like the position of print 
print(len(apple))
print(apple[3:22])   #slicing string  (including first one like 3 but not the last one (22))
print(apple[0:len(apple)-6])
print(apple[0:-6])   # they will be same 
########string methods (operation with strings )
#if you perform any operation in string like if you want to convert string into upper case then a copy of string will be formed instead of changing the old string .Strings are immutable
print(apple.upper())
print(apple.lower())
print(apple.rstrip("!"))  #will remove the trailing characters (The term 'trailing' refers to the characters at the end of a string. By default, rstrip() removes any trailing spaces if no specific characters are defined.) 
print(apple)  #this string haven't changed at all
print(apple.replace("baat","naan"))
print(apple.split(" "))   #turn the charaters separted by a space into a separate character and make a list of them 
print(apple.capitalize())  #make first character upper case and all other lower case 
print(apple.center(56))  # print the string to centre of the console according the the spces given here 22
print(apple.count("a"))
print(apple.endswith("!"))
print(apple.endswith("at",2 ,4))
print(apple.find("gulu"))  #if not found will give -1
#print(apple.index("is"))  # same as find and if not there will produce a error exception
print(apple.isalnum())
print(apple.isalpha())
print(apple.isspace())
print(apple.swapcase())  #will convert uppercase to lower and vice versa 
print(apple.title())   #to make first letter upper case'''
############conditional statements (if else )########
# age = int(input("enter your age"))
# print("so the age of the student is ",age)
# if(age>18):
#     print("can drive ")   #print automatically written after space this is known as indentation in pythi which meas a new block is being created in oython that we create in c++ using curly brackets {} ;
# else:
#     print("cant drive ")
#########using elif as else if 
# num = int(input("enter the number"))
# print("so the number is ",num)
# if(num>0):
#     print("number is podittive")    
# elif(num==0):
#     print("number is zero")
# else:
#     print("number is negative")
#################MATCH CASE STATEMENTS #########
#they are a new addition in python and they are like switch case statements in c++ we will have cases and then we decide according to our coice like in c++ we won't use break statemt in python as we use to do in c++
'''x = int(input("what is value of number"))
match x :
 case 0:
  print("the value of x is zero")
 case 5:
  print("the value of x is 5")
 case 8:
  print("the value of x is 8") 
 case _ if x!=90:
  print(x , "is not qual to 90")
 case _:
  print(x)'''
##########FOR LOOP IN PYTHON 
# name = "SULTANA"
# for s in name:
#     print(s)
#     if(s == 'A'):
#         print("its a special character")
# ##for loop for list 
# colors = ["green","yellow","blue","orange","zinc"]
# print("there is a list of colors as follows: ")
# for r in colors:
#     print(r)
#     for s in r:
#         print(s)
# for k in range(33):
#     print(k)
   # print(k+1)
##range from 23 to 33
# for p in range(23 ,33):
#     print(p)
# for g in range(0,12,2):
#     print(g)    # Range have 3 parameters (Strat , stop , step) Step is basically an difference between the first number and last number it may be varied as per the user .
############WHILE LOOP 
# x = 0
# while(x<7):
#     print(x)
#     x = x+1 
# i = int(input("enter the value of number"))
# while(i<40):
#     i = int(input("enter the value of number"))
#     print(i)
# else:
#  print("done with loop")   #there is no do while loop i python we can also use else after while loop 
############# Break and continue statements 
# for i in range(12):
#     print("5 * ", i , "=", 5 * i)
#     if(i==10):
#         break
# for i in range(12):
#  if(i==10):
#     continue
#  print("5 * ", i , "=", 5 * i)
 #we can emulate a do while loo in python by using an infinite loop 
# i = 1
# while True:
#    print(i)
#    i = i+1
#    if(i%100 == 0):
#     break
########FUBCTIO IN PYTHON 
#we make fuction in pythn to increase our code reusability 
# def countGeoMean(num1 , num2):
#     mean = (num1*num2)/num1+num2
#     print("so geometric mean is " ,mean)
# def liyNum(a,n):
#     pass   #it will pass the functio with only indentation without any error shwoing that the function's body is somewhere else and code shouls keep going without any error 
# a = 77 
# b = 46
# countGeoMean(a,b)    
#########ARGUMENTS IN FUNCTION 
#there are four ypes of arguments that can be provided in a function 
#1.defaukt argument  2.keyword argument 3.variable length argument 4.required arguments 
# def average(*numbers):
#   #tuple as an arguments (we can add as much number in function calling as we want )
#   sum = 0 
#   for i in numbers:
#    sum = sum + i
#   print("so avegae of numbers is ",sum/len(numbers ))
# average(3,6,2,1,8,7)
# def spa(**num) :
#   pass  #taking dictionary as a function arguments 
#########LISTS IN OYTHON 
#(lists are ordered collection of data items )
'''marks = [3,5,7,4,5,6,2,"star"] #length is 7 but index is 6
print(marks[1])
print(marks[0])
print(marks[-4])  #to convert this negative idnex into postive we will subtract it from total length of the list 
print(marks[len(marks)-4]) # all three of them will give same index as they have same meanig 
print(marks[3])
#we ca also find elements of list by using if stateents liken
if 10 in marks:
    print("yes")
else:
    print("no")
if "star" in marks:
    print("yes")
else:
    print("no")
if "st" in "star": #same thing applied of strings as well 
    print("yes")
else:
    print("no")
list = [i for i in range(5)]
print(list)
list = [i*i for i in range(10)]
print(list)
list = [i for i in range(10) if i%2 ==0] #wcan add condition in list to make selective nmbers to be printed 
print(list)'''
############METHODS OF LIST 
# l = [2,4,7,8,1,2,4,6,7,5]
# print(l)
# l.append(3)
# print(l)
# l.sort()
# print(l)
# l.sort(reverse = True)
# print(l)
# l.reverse()
# print(l)
# print(l.index(4))
# m = l.copy()
# m[4] = "harry"
# print(l)  #if we donr use copy and simply make m = l then eventually te list l will be changed with chnges in m 
# print(m)
# l.insert(3,"pookie baba")
# print(l)
# s = ["tu mera nhi",234,"error"]
# l.extend(s)
# print(l)
# # can also use another method as  k = l+s
## While loop Example
# count = 0
# while (count < 3):
#     count = count + 1 
#     print("Hello World")

# # Single statement while block 
# count1 = 0
# while (count1 < 3):  # Change the condition to count1 < 3
#     print("Hello Nerds")
#     count1 += 1  # Increment count1 to avoid infinite loop
#############TUPLE IN PYTHON (uples are immutable we cannot change tuples we have to make the new one for any kind of change )
'''tup = (2,5,"love",7.89,"geet aur gori ",'stay alive')
print(type(tup),tup)
print(tup[-2])
if 34 in tup:
    print("yes its present in tuple ")
else:
    print("no its not present ")
##########mehods of tuple
#tuples can't be changed they will be converted ito list for anychange but they still be a new tuple for example
kdramas = ("love from another star","DOTS",'THE Heirs','love next door',"tale of the nine tailed ","the devil judge")
print(kdramas)
temp = list(kdramas)
temp.append("the ghost")
temp.pop(2)    #remove utem
kdramas = tuple(temp)
print(kdramas)
##also we can concatenate two tuples like
kdramas1 = ("love from another star","DOTS",'THE Heirs','love next door',"tale of the nine tailed ","the devil judge")
hindiMovies = ("love aj kal","bhool bhuliyan","12th fail","good newz")
entertain = kdramas1+hindiMovies
print(entertain)
tuple = (3,4,6,9,4,2,2,5,6,5,3,3,2,9)
print(tuple.count(3))
spa = tuple.index(5)
print(spa)'''
############PYTHON F strings 
#first we will see the old approach througgh whic we used strings 
# letters = "hey my name is {} and im from {}"
# name = "tania "
# country = "new zeland "
# print(letters.format(name, country))
# print(letters)
# #now in fstring we can directly enter the value of  variables inside 
# price = 300
# txt = f"the price of this shirt is {price : .2f} dollars"
# print(txt)
# #now if we want to show f string they way they are written then we will use 2 curly brackets together
# txt = f"the price of this shirt is {{price : .2f}} dollars"
# print(txt)
###########DOC STRING AND PEP8 IN PYTHON
# doc string is used to tell the purpose of the function and also it should be written below function to make it a doc 
# def square(n):
#     '''this function named as aqusre is used to find the square of a function'''
#     print(n**2)
# square(5)
# print(square.__doc__)
#by wriring import this in python we gonna get a poem which an esater egg in python which is zen of python
######recursion in python 
#let's find factorial of a number by using recursion
'''def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))'''
#now we will calculate fibonacci series 
# def fibo(fn):
#     if(fn == 0 ):
#       return 0
#     elif(fn == 1):
#       return 1 
#     else:
#       return fibo(fn-1)+fibo(fn-2)

# #print(fibo(12))
# for i in range(int(input("enter the number"))):
#    print(fibo(i),end = " ")
########set in python 
# set is a collection of well-defined objects which don't take anything in repeat and its idexes are not fixed 
'''s = {2,42,2,4,7,8,8,88,4,3,5,3,3}
print(s,type(s))
harry = {}
print(type(harry)) #tis will give a type dictionary as dictionary also starts and ends with { brackers } so in order to get empty set type as set we will use 
harry = set()
print(type(harry))
#set dont maintain order so if you apply a for loop to get value it maybe any value without mainatianing any order
s = {"daniel" , 46 , "ka",678.78,(-8,9)}
for value in s:
    print(value)'''
#methods of set in python 
'''s1 = {2,"goriya",6.8}
s2 = {3,2,7,9,120}
print(s1.union(s2))
s1.update(s2)  #to upate value of set s1 with values of s2 which are not present in s1 if we only use union then vale of s1 reamin same if we print it in next line but after usig updare fuction the value of set will be changed 
#print(s1)
print(s1.intersection(s2))
#symmetric diference in cells means all those values which are ot common (AUB)-(ANB)
print(s1.symmetric_difference(s2)) #all will be printed except ANB which was 2 in our case 
print(s1.issuperset(s2))  #are all values of s2 are present in s1
print(s2.issubset(s1)) #are values of s2 are also a aprt if s1
s1.add("ja ni ja tu gaira sang laaaaa")
print(s1)
s1.remove(7) #if that value is not present in set remove will give an error while discard won't give any error
s1.discard("goriya")
print(s1)
s3 = s1.pop()
print(s3) #onr random value will be remved from set 
print(s1)
del s1   #to delete whole set '''
###############dictionaries n python 
#it is a combination of key value pairs separated by coma e.g, (dictionaies were unordered before  but with ew python versio they are ordered now )
# dic = {
#     45 : "student1",
#     965 : "student2",
#     475 : "student4",
#     5 : "student6",
#     2465 : "student8"
# }
# print(dic[5])
# print(dic.items())
# print(dic.get(5)) #both will get value of 5 put .get wont throw an error if 
# for key in dic.keys():
#         print(dic[key])
# dic1 = {
#     45 : "student1",
#     965 : "student2",
#     475 : "student4",
#     5 : "student6",
#     2465 : "student8"
# }
# dic2 = {
#    1 : "stud1", 
#     2 : "stud2",
#      3 : "stud4",
#        4 : "stud6",
#     5 : "stud8"
# }
# dic1.update(dic2)
# #print(dic1)
# dic1.clear()
# dic2.pop(5)
# print(dic2)
# dic1.popitem() #it will remove last value pair 
#########using else wit for loop
# for i in range(5):
#     print(i)
# else:   #i will be printed tull range n-1 and then in last sorry statement will be printed 
#     print("sorry i is not present ")
# for i in []:
#     print(i)
# else:  #only else statements will be printed as  it in an empty list 
#     print("sorry i is not present ")
# for i in range(5):
#     print(i)
#     if(i==3):
#         break
# else:  #else statement won't be printed as it can be printed in the end of loop after all iterations are done but here the loop break after 3 
#     print("sorry i is not present ")
# for x in range(5):
#     print("iterations no {} in for loop ".format(x+1))
# else:
#     print("else block in loop ")
# print("out of loop")
#############EXCEPTION HANDLING IN PYTHON 
# a = input("enter the number ")  
# print(f"so te multiplication table of {a} is :")  #now if we give an string that can't be converted into intger then this will through and error and ramainig code will not run 
# for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)* i }")

# print("some imp lines of code ")
# print("program ends here ")
# # so to avoid error we will use try and except method 
# a = input("enter the number ")  
# print(f"so te multiplication table of {a} is :")  #now if we give an string that can't be converted into intger then this will through and error and ramainig code will not run 
# a = input("enter the number ")  
# print(f"so te multiplication table of {a} is :")
# try:
#    for i in range(1,11):
#      print(f"{int(a)} X {i} = {int(a)* i }")
# # except Exception as e:
# #    print(e)   #it gave an error but other code keep running instead of makin a halt 
# except:  #can also wrie it like that 
#    print("invalid input error")

# print("some imp lines of code ")
# print("program ends here ")
###finally keyword in python which mean that the block of code should always be executed no matter what the situation is , for example if we have a a function which returns 0 we try works and 1 when except runs but last line(with print statement) wont run but if we use finally keyword with it then that last line will work eventually no matter what ever the rwturn value of function is 
'''try:
    l = [3,31,35,32,2]
    i = int(input("enter the index of the list yi want to print "))
    print(l[i])
except:
    print("an error occured!!!!!!!!!!!")
finally: 
    print("this code will e executed no matter what ")'''
##############rAISING CUSTOM ERRORS
# (we can raise cusrtom errors if we have problem with aynthing that we don't want to deal with also we can also make a whole exception error classs if we want to deal with specific kind of situation in the form of an error for example let we have a server closed we can make that thing into an error to deal with it properly  )
# a = int(input("enter the value of a between 5 and 10"))
# if(a<5 or a>10):
#     raise ValueError("the value of a is invalid")
# Short hand if else statements 
# a = 9273
# b= 34
# print("a") if a<b else print("=") if a==b else print("b")
###########ENUMERATE FUNCTIO IN PYHON 
#(through this function we can get both the value of the objects in list you can say that and also the index of the objects if we run a loop in it lets see it in an aexample )
'''marks = [2,47,6,32,81,123,24,18,1]
for index,mark in enumerate(marks):
    print(mark)
    if(index==5):
        print("awesommemeee brrooo!!!!")
fruits=["banaan","apple","orange","mango","grapes"]
for index,fruit in enumerate(fruits,start =1):
    print(fruit)
    if(index==2):
        print("favouriteee oneeee!!!!")'''
#########we creste virtual environments in python if diffreent packages diffreent people are using create any kind of conflicts so to avoid them we use virtual envirionment 
#so the packages of my version have nothin to do with the packages of opython i using in my computer doing notmal work with them
###########import in python
# we can use import methos in oython to import diffreent methods in that function or whatever it is 
# import math
# result = math.sqrt(25)
# print(result)
# we can also use secific functins from it by using it like
#from math import sqrt , pi  
#from math import *   to import all the methods of math but this procedure is not usable as it can cause a bit problem while compiling 
#we can also make short forms of methods like 
#from math import sqrt as s ( now we can use it as s(25))
# result = sqrt(25) * pi
# print(result)
# import math
# print(dir(math)) #dir function is used to print all the methods or functions present in math module
# from song import sing , SINGER #imported our functions from our own made file 
# sing()
# print(SINGER)
######################
#he if __name__ == "__main__": construct in Python is used to determine whether a Python script is being run as the main program or if it is being imported as a module in another script. This is important for controlling the execution of code in a way that allows for both standalone execution and modular use.
#__name__ Variable:

# In Python, every module has a built-in attribute called __name__.
# When a module is run directly, Python sets __name__ to "__main__".
# If the module is imported into another module, __name__ is set to the module's name (i.e., the filename without the .py extension).
#its very important as it can save your computer as if you import a file and it start executing its function then it can be dangerous 
##########OS MODULE
#The os module in Python provides a way to interact with the operating system. It offers a variety of functions to perform operations related to file and directory management, process management, environment variables, and more. The os module is part of the Python Standard Library, which means it comes pre-installed with Python and does not require any additional installatio
###########global and local variable 
# x = 10    #global variable
# def name():
#     x=3    #local variable
#     print(x)
# name()
# print(x)     #it will remain 10 as it is gloabla variable and the x in fuction only depends on that function
####now if we want to change the value of global variable in a function the we will have to use global keyword in function to make sure that we are dealing with global variable 
# def po():
#     global x 
#     x=67
# po()
# print(x)  #this will chamge the value of x to 67
###############file handling in python 
'''1.Read Mode ('r'):
with open('file.txt', 'r') as file:
    content = file.read()
2.Write Mode ('w')
with open('file.txt', 'w') as file:
    file.write('Hello, World!')
3.Append Mode ('a'):
with open('file.txt', 'a') as file:
    file.write('Appending this line.')
4.Read and Write Mode ('r+'):
with open('file.txt', 'r+') as file:
    content = file.read()
    file.write('Adding this line.')
5.Write and Read Mode ('w+'):
with open('file.txt', 'w+') as file:
    file.write('Writing this line.')
    file.seek(0)  # Move the cursor to the beginning of the file
    content = file.read()
6.Append and Read Mode ('a+'):
with open('file.txt', 'a+') as file:
    file.write('Appending this line.')
    file.seek(0)  # Move the cursor to the beginning of the file
    content = file.read()'''
########reading from a file 
# f = open("practice.txt", 'r')
# text = f.read()
# print(text)
#f.close()
#writing in a file 
# f = open("practice.txt", 'w')
# f.write("tph main kuch nhi mango dunya seee")
# f.close()
########appending
# f = open("practice.txt", 'a')
# f.write("toh main kuch nhi mango dunya seee")
# f.close()
# now mpstly we have to use file.close to make our function run but with another method we dont neew to use that file.close and ou commands will still work 
# with open("practice.txt", 'a') as f:
#     f.write("   mane na mane koi dunya ye sari mere ishq ki hai dewani ")
###########methods of file handling in oython
#readlines ()method
# f  = open("practice.txt",'r')
# while True:
#  line = f.readlines()
#  if not line :
#   break
#  print(line)
#example 
# f  = open("practice.txt",'r')
# i = 0 
# while True:
#  line = f.readlines()
#  if not line:
#   break
#  m1 = line.split(",")[0]
#  m2 = line.split(",")[1]
#  m3 = line.split(",")[2]
#  print(f"the marks of student {i} in maths is {m1}")
#  print(f"the marks of student {i} in english is {m2}")
#  print(f"the marks of student {i} in science is {m3}")
####code without error
# Open the file in read mode
'''f = open("practice.txt", 'r')

# Initialize a counter for students
i = 0 

# Iterate over each line in the file
for line in f:
     # Increment the student counter
    i += 1

    # Strip any leading/trailing whitespace (including newline characters)
    line = line.strip()
    
    # Check if the line is not empty
    if not line:
        continue  # Skip empty lines

    # Split the line by commas
    marks = line.split(",")
    
    # Ensure there are at least 3 marks
    if len(marks) < 3:
        print(f"Not enough data for student {i}.")
        continue

    # Extract marks for each subject
    m1 = marks[0]
    m2 = marks[1]
    m3 = marks[2]

    # Print the marks
    print(f"The marks of student {i} in maths is {m1}")
    print(f"The marks of student {i} in English is {m2}")
    print(f"The marks of student {i} in Science is {m3}")

    

# Close the file
f.close()

#wruite lines method 
f = open("practice.txt",'w')
lines = ["line 1\n","line 2\n","line 3\n"]
f.writelines(lines)
f.close()'''
#seek() and tell() amd other functions 
#The seek() function is used to change the current file position (the file pointer) to a specified location . The tell() function is used to get the current position of the file pointer in the file , It returns the current position as an integer, which represents the number of bytes from the beginning of the file.
# with open('text.txt','r') as fu:
#  print(type(fu))
# #Move to the 10th byte from the beginning
#  f.seek(10)
#  print(fu.tell())
#  data = fu.read(5)
#  print(data)
 #truncate( ) means to truncate the file size according to what yu need for example yiu can truncate file to 5 words ad there won't be any other words written in it 

# with open('text.txt','w') as fu:
#  fu.write("hello world")
#  fu.truncate(5)
# with open('text.txt','r') as fu:
#  print(fu.read())
 

#lambda function is an anonymous function without any name for eaxmple 
# def double(x):
#  return x*2
# print(double(3))

# #OR SAME THIG IS 
# double = lambda x: x*2 
# print(double(3))
# avg = lambda x,y : (x+y)/2
# print(avg(3,6))
# #we can also use lamda function for using it inside a function as well for example lets we see
# def lee(fx , value):
#  return 4 + fx(value)
# print(lee(double,6)) 
# print(lee(lambda x : x*2 , 6))
# print(lee(lambda x : x*x*x,5))
#############MAP FILTER REDUCE METHOD 
# def cube(x):
#     return x*x*x
# lt = [5,8,4,2,4,1,0,9]
#let we want cube of every element of list
# newlist = []
# for l in list:
#     newlist.append(cube(l))
# print(newlist)
#this method is quite long so instead of this we will use map 
# newlist = list(map(cube,lt))
#can use lambda s\as well 
#newlist = list(map(lambda x : x*x*x,lt))
# print(newlist)
#now filtering the elemnts through the list 
# newli = []
# def filter_function(a):
#     return a>4
# newli = list(filter(filter_function , lt))
# print(newli)
###we need to import reduce to make it work 
'''from functools import reduce
list = [2,3,4,6,7]
def dum(x,y):
    return x+y
sum = reduce(dum , list)
print(sum)'''
######is and vs keyword in python 
# a = 6
# b = "6"
# print(a is  b)  #compare location of object in memory(vcompare identity)
# print(a==b)  #compare value 
############OOP IN PYTHON 
# class person:
#     name = "Natalia"
#     occupation = "hacker"
#     age = 23 
#     def info(self): #self is a keyword ,self means the obejct for this the method is being called 
#         print(f"{self.name} is a professional {self.occupation} and she can help you in any kind of investigation")
# a = person()
# print(a.name , a.occupation , a.age)
# a.info()
# b = person()
# b.name = "sara"
# b.age  = 45
# b.info()
###########constructor
# class person:
#     def __init__(self , n , o):
#         # print("hey im a constructor ")
#         self.name = n 
#         self.occupation = o
#     def info(self):
#         print(f"hey im {self.name} and i'm a {self.occupation} !!")
# x = person("Sana" , "accountant")
# y = person("Haris","HR")
# x.info()
# y.info()
########DECORATOS IN PYTHON 
#lets we make greet as a decorator and it takes the real function inside it and aslo the function which add functionality into the real function when we call it with decorator greet 
# def greet(fx):
#     def mfx(s,p):
#         print("good moring sir !")
#         fx(s,p)
#         print("thanks for using decorator within the function")
#     return mfx
# #The wrapper function (mfx in your example) needs to accept the same arguments as the original function (fx). This is important because when you call the decorated function, you want to ensure that it can accept any arguments that the original function can accept. If you didn't pass the arguments to the wrapper, you wouldn't be able to pass them to the original function.
    
# @greet
# def add(a , m):
#     print("the sum of two numbers is ", a+m)
# add(3,6)
#In Python, getters and setters are methods that allow you to access and modify the attributes of a class in a controlled way. They are part of the concept of encapsulation, which is one of the fundamental principles of object-oriented programming.
# Getters
# A getter is a method that retrieves the value of an attribute. It allows you to access the value of a private or protected attribute from outside the class.
# Setters
# A setter is a method that sets or updates the value of an attribute. It allows you to modify the value of a private or protected attribute from outside the class, often with additional validation or processing.
# class Person:
#     def __init__(self, name, age):
#         self._name = name  # Using a single underscore to indicate a protected attribute
#         self._age = age

#     # Getter for name
#     @property
#     def name(self):
#         return self._name

#     # Setter for name
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise ValueError("Name must be a string")
#         self._name = value

#     # Getter for age
#     @property
#     def age(self):
#         return self._age

#     # Setter for age
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError("Age must be a non-negative integer")
#         self._age = value

# # Example usage
# person = Person("Alice", 30)

# # Using the getter
# print(person.name)  # Output: Alice
# print(person.age)   # Output: 30

# # Using the setter
# person.name = "Bob"  # Valid
# print(person.name)    # Output: Bob

# # person.name = 123  # This would raise a ValueError

# person.age = 35  # Valid
# print(person.age)  # Output: 35

# person.age = -5  # This would raise a ValueError
#########aonther example using setters and getters 
# class myClass:
#     def __init__(self,value):
#         self._value = value
#     def show(self):
#         print(f"value is {self._value}")
#     @property
#     def ten_value(self):
#         return 10 * self._value
#     @ten_value.setter
#     def ten_value(self , new_value):
#         self._value =  new_value/10
# obj = myClass(34)
# obj.ten_value = 45
# print(obj.ten_value)
# obj.show()
###########INHERTANCE IN PYTHON 
# class employee:
#     def __init__(self , id , name):
#         self.id = id 
#         self.name = name

#     def show(self):
#         print(f"so the name of the employee {self.id} is {self.name}")
# class programmer(employee):
#     def showLan(self):
#         print("so the languahe of the programmer is python")
# class hacker(programmer):
#     def skill(self):
#         print("so the main skill of the hacker is penetartion testig and web serving ")
# e1 = employee("harry",34)
# e1.show()
# e2 = programmer("sunit",67897)
# e2.show()
# e2.showLan()
# e3 = hacker("black rose",7018375469)
# e3.show()
# e3.showLan()
# e3.skill()
 ####in python there is no specific terms for access modifiers but for conevnience we can use  them as private by  adding double underscore __ with variable name and still acess the, directly by using name mangling(e.g,   e1._employee__name) . for protected it is single undercsore _   covention van be adopted that single score ,ay use for private sometimes according to people if they dont want to use ame mangking 
###sometime you can write function without passing self as an argument and this is possible by using statuc method lets see an example
# class numbers:
#     def __init__(self , num):
#         self.num = num
#     def add(self , n):
#         return self.num + n
#     @staticmethod
#     def addtonum(a,b):
#         return a+b
# number = numbers(3)
# print(number.add(8))
# print(number.addtonum(86,87))
        
#############instance and class variables 
# class employee:
#     companyName="APPLE"
#     def __init__(self, name):
#         self.name = name
#         self.raise_amount = 6.976
#     def showDetails(self):
#         print(f" so the name of the employee is {self.name} and raise is {self.raise_amount} and company is {self.companyName}")
# e1 = employee("harry")
# e1.companyName = "Apple canada"  #istance variable first compiler check if there is  a instance variabe of e1 if not then it will go to class variable 
# e1.showDetails()
# e2= employee("daniel")
# e2.showDetails()
##########OS MODULE
###The os module in Python is a standard library module that provides a way to interact with the operating system. It allows you to perform various operating system-related tasks such as file and directory manipulation, process management, and environment variable handling. The os module is particularly useful for writing cross-platform applications, as it abstracts away many of the differences between operating systems.
# os.mkdir(path): Creates a new directory at the specified path.
# os.rmdir(path): Removes an empty directory at the specified path.
# os.makedirs(path): Creates a directory and any necessary parent directories.
# os.removedirs(path): Removes a directory and any empty parent directories.
# os.listdir(path): Returns a list of the entries in the specified directory.
# os.getcwd(): Returns the current working directory.
# os.chdir(path): Changes the current working directory to the specified path.
# os.rename(src, dst): Renames a file or directory from src to dst.
# os.remove(path): Deletes a file at the specified path.
# os.path submodule: Contains functions for manipulating file paths (e.g., os.path.join(), os.path.exists(), os.path.isfile(), etc.).
# import os

# # # Get current working directory
# current_directory = os.getcwd()
# print("Current Directory:", current_directory)

# # # Create a new directory
# new_directory = "test_dir"
# os.mkdir(new_directory)
# print(f"Directory '{new_directory}' created.")

# # # List files and directories in the current directory
# print("Contents of the current directory:", os.listdir(current_directory))

# ##Change to the new directory
# os.chdir(new_directory)
# print("Changed to directory:", os.getcwd())

# # # Go back to the original directory
# os.chdir(current_directory)
# print("Changed back to directory:", os.getcwd())

# # Remove the created directory
# os.rmdir(new_directory)
# print(f"Directory '{new_directory}' removed.")
#######class methods 
#in a function the by default variable in a function is instance variable for examle copany(cls , newName) in which cls is instance variable it will be changed for a specific object but not for thw whole class but if we want to chnge that for the whole class we can maje a method named as @classmethod whih will chnage the name for the whole class and class will be given as an argument in function instead of a variable 
# class Employee:
#     company = "apple"
#     def show(self):
#         print(f"so the name of the employee is {self.name} and name of the compny is {self.company}")
#     @classmethod
#     def changeCompany(cls , newCom):
#         cls.company = newCom
# e1 = Employee()
# e1.name = "guarana"
# e1.show()
# e1.changeCompany("rhysu")
# e1.show()
# print(Employee.company)  
###class methods as alternative constructors 
# class employee:
#     def __init__(self,name,salary):
#         self.name = name 
#         self.salary = salary
#     @classmethod
#     def fromstr(cls , string):
#         return cls(string.split('-')[0] ,string.split('-')[1] )
# e1 = employee("harry" , 4566)
# print(e1.name)
# print(e1.salary)
# stri = "goriya-620000"
# e2 = employee.fromstr(stri)
# print(e2.name)
# print(e2.salary)
#########dir(), __dict__ , help() methods 
'''list = [34,89,"john",35,533,"duianmin"]
print(dir(list))  #wil tell us about all components using in list or maybe tupke 
print(list.__add__)

class student:
    def __init__(self, name , grade):
        self.name  = name
        self.grade = grade
        print(f"so the name of the student is {self.name} and grade of the student is {self.grade}")
s1 = student("maris",7)
print(s1.__dict__)   #will give information about all the attribues if the class as dictionary
print(help(s1))  #will give all the information about the obj 
print(help(student))'''
#####super keyword in python is used to refer to parent calss it is specially useful when a child class is inherits from multiple parent classes and you want to inheit a mathod from a specific parent class 
# class parentClass:
#     def parent_method(self):
#         print("calling parent method")
# class childClass(parentClass):
#     def child_method(self):
#         print("calling child method")
#         super().parent_method()
# c1 = childClass()
# c1.child_method()
#we can use this method to call constructirs as well lets say 
# class employee:
#     def __init__(self, name ,id):
#         self.name = name
#         self.id  = id
# class programmer(employee):
#     def __init__(self,name,id ,lang):
#         super().__init__(name,id)   #self.name = name andself.id  = id we dont have to use this code again
#         self.lang = lang
# p1 = programmer("john",67890,"java")
# print(p1.lang)
#############MAGIC/DUNDER METHODS
# Special Naming: Magic methods are always surrounded by double underscores (e.g., __init__, __str__, __add__). This naming convention distinguishes them from regular methods.

# Automatic Invocation: These methods are automatically called by Python in response to certain operations. For example, when you use the + operator, Python internally calls the __add__ method.

# Customization: Magic methods allow you to customize the behavior of your objects, making them more intuitive and easier to use.
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

# # Usage
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)

# # Using __str__ method
# print(v1)  # Output: Vector(2, 3)

# # Using __add__ method
# v3 = v1 + v2
# print(v3)  # Output: Vector(6, 8)

# # Using __eq__ method
# print(v1 == v2)  # Output: False
# print(v1 == Vector(2, 3))  # Output: True
########__call__ method example 
#Certainly! The __call__ magic method in Python allows an instance of a class to be called as if it were a function. When you implement the __call__ method in a class, you can define what happens when an instance of that class is called with parentheses.
# class adder:
#     def __init__(self,incre):
#         self.incre = incre
#     def __call__(self,value):
#         self.value = value
#         return self.value + self.incre
# a1 = adder(6)
# result = a1(78)
# # print(result)
#######method overiding in python
# class shape:
#     def __init__(self,x,y):
#         self.x = x 
#         self.y = y
#     def area(self):
#         return self.x * self.y

# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius 
#         super().__init__(radius,radius)
#     def area(self):
#         return 3.14 * super().area()
# c0 = shape(5,7)
# print(c0.area())
# c1 = circle(1)

# print(c1.area())#
#  ##################pypdf module is python for manipulating pdf files 
# The pypdf module is a Python library designed for working with PDF files. It provides a range of functionalities that allow users to read, manipulate, and create PDF documents. The library is a fork of the original PyPDF2 library and has been updated and maintained to improve performance and add new features.
# Custom Function:

# merge_pdfs(pdf_list, output_filename): This function is defined by the programmer to encapsulate the logic for merging PDF files.
# Library Methods and Attributes:

# pypdf.PdfWriter(): Constructor for creating a PDF writer.
# pypdf.PdfReader(file): Constructor for creating a PDF reader.
# pdf_reader.pages: Attribute that provides access to the pages of the PDF.
# pdf_writer.add_page(page): Method to add a page to the writer.
# pdf_writer.write(output_file): Method to write the merged PDF to a file.
'''import pypdf
def merge_pdf(pdf_list , outputfile_name):
    pdf_writer = pypdf.PdfWriter()
    for pdf in pdf_list:
        with open(pdf ,'rb') as file:
            pdf_reader = pypdf.PdfReader(file)
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])
    with open(outputfile_name,'wb') as outputfile:
        pdf_writer.write(outputfile)
pdf_files = ['OOP.pdf', 'dld.pdf', 'cover page.pdf']  # Replace with your PDF file names
output_pdf = 'merged_output.pdf' 
merge_pdf(pdf_files, output_pdf)

print(f"Merged PDF saved as '{output_pdf}'")
'''
#########operator overloading 
# class vector:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k 
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self,x):
#         return vector(self.i + x.i , self.j+x.j , self.k+x.k)
# v1 = vector(2,3,4)
# v2 = vector(7,1,6)
# print(v1)
# print(v2)
# print(v1+v2)
#######inheritance (single level)
# class animal:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#         print(f"my animal name is {self.name} and its color is {self.color}")
#     def sound(self):
#         print("it makes a sound")
# class cat(animal):
#     def sound(self):
#         print("it meowsss!!!!!")
# a1 = animal("tonny","olive green")
# a1.sound()
# a2 = cat("kittuuuu","while and grey")
# a2.sound()
#########multiple inheritance 
class programmer:
    def __init__(self):
        print("this employee is a programmer")
class cyberanalyst:
    def __init__(self):
        print("this employee is a cyber security expert")
class employee(programmer,cyberanalyst):
    def show(self):
        print("he is a parogarmmer and cyber analyst at the same time ")
w1 = employee()
w1.show()
print(employee.mro()) #which shows that class programmer will be preffered and ts costrunctor will be printed as it was written first 
