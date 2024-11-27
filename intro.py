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
marks = [2,47,6,32,81,123,24,18,1]
for index,mark in enumerate(marks):
    print(mark)
    if(index==5):
        print("awesommemeee brrooo!!!!")
fruits=["banaan","apple","orange","mango","grapes"]
for index,fruit in enumerate(fruits,start =1):
    print(fruit)
    if(index==2):
        print("favouriteee oneeee!!!!")
#########we creste virtual environments in python if diffreent packages diffreent people are using create any kind of conflicts so to avoid them we use virtual envirionment 
#so the packages of my version have nothin to do with the packages of opython i using in my computer doing notmal work with them