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
tup = (2,5,"love",7.89,"geet aur gori ",'stay alive')
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
print(spa)