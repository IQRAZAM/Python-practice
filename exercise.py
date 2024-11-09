#Q1  making a simple calculator that perform operation on two numbers 
'''print("**********calculator*********")
a = 50 
b = 10
print("so the addition of a and b is ", a+b)
print("multiplication of a and b is ", a*b)
print("dividion of a and b is ",a/b)
print("subtraction of a and b is ",a-b)'''
##Q2 write a program ehich rint good morining and other such greetings according to time module given  
##Python time module allows to work with time in Python. It allows functionality like getting the current time, pausing the Program from executing, 
'''import time
# curr = time.time()   it will give seconds since 1970 epoh time then we will inout those seconds in ctime to et the string of time readable by humans 
curr = time.ctime(1729338086.6472495) #for giving current time 
print("so the current time is ",curr)
realTime = time.strftime("%H:%M:%S")
print("and the current time is ",realTime)
hour = int(time.strftime("%H"))
if (hour>0 and hour<=12) :
  print("good moring")
elif(hour>12 and hour<=16):
  print("good noon")
elif(hour>16 and hour<=20):
  print("good evening")
else:
  print("good night")''' 
##Q3 Making a "kon bane ga crore patti program in which there will be question and their correct answers and then user will get a specific amount of money and in the end this money will collectively e calculated and we will use a list for that now lets see!!!!"
questions = ["1.What is the largest planet in our solar system?","2.How many continents are there in the world?","3.What is the capital of France?","4.Which ocean is the largest in the world?","5.What is the smallest country in the world?","6.How many days are there in a leap year?"]
ans = ["jupiter",7,"paris","pacific ocean","vatican city",366]
count = 0
for index ,question in enumerate(questions):
    print(question)
    spa = input("what's your answer? ")
    if(spa.lower() == str(ans[index]).lower()):
        print("you are right")
        count = count +10
    else:
        print("its wrong")
print("so your final score is ",count)