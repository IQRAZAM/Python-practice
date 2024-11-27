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
'''questions = ["1.What is the largest planet in our solar system?","2.How many continents are there in the world?","3.What is the capital of France?","4.Which ocean is the largest in the world?","5.What is the smallest country in the world?","6.How many days are there in a leap year?"]
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
print("so your final score is ",count)'''
#Q4 encrpt and decrypt game
# write a python program to trasnalet a message into secret code and rules should be 
# if the word cobtains atlest 3 words remove the first letter and append it at the end else simple reverse the string 
# decoding: if the word cotains less than 3 characters reverse it else remove three random characters from end and start now renmove the last letter and append it to the beginning 
# your program should ask whether you want to code or decode 
# (i think so we should take a word reverse it simply and add 3 random letters at start and three random characters at the end it would be fun )
'''import random
import string 
def encrypt():
    str0 = input("Write a string that you want to encypt :")
    str1 = str0[::-1]
    random_letters = ''.join(random.choices(string.ascii_letters, k = 3))
    final_string = random_letters + str1 + random_letters
    print(final_string)
def decrypt():
    str0 = input("Write a string that you want to decrypt: ")
    str1 = str0[::-1]
    print("Decrypted string:", str1)

print("Hey there ! Do you want to play an encrypt decrypt FUN GAME????")
ans = input()
if(ans == "no"):
    exit()
else:
    while(ans=="yes"):
        print("what operation you want to perform tell us :")
        print("1.encrypt")
        print("2.Decrypt")
        print("3.Exit game")
        choice = input("choose 1 , 2 or 3 according to your choice :")
        match choice:
            case "1" :
                encrypt()
            case "2" :
                decrypt()
            case "3" :
                exit()
            case _ :
                exit()'''
#########another way to solve ex#4 (from balckbox)
'''import random
import string

def encrypt():
    str0 = input("Write a string that you want to encrypt: ")
    words = str0.split()  # Split the input into words
    encrypted_words = []

    for word in words:
        if len(word) >= 3:
            reversed_word = word[::-1]  # Reverse the word first
            random_letters = ''.join(random.choices(string.ascii_letters, k=3))
            # Add random letters to the start and end of the reversed word
            encrypted_word = random_letters + reversed_word + random_letters
            encrypted_words.append(encrypted_word)
        else:
            # Just reverse the word if it's 3 or fewer characters
            encrypted_words.append(word[::-1])

    final_string = ' '.join(encrypted_words)  # Join the encrypted words back into a string
    print("Encrypted string:", final_string)

def decrypt():
    str0 = input("Write a string that you want to decrypt: ")
    words = str0.split()  # Split the input into words
    decrypted_words = []

    for word in words:
        if len(word) >= 3:
            # Remove the first and last 3 characters
            decrypted_word = word[3:-3]  # Remove the random letters
            decrypted_words.append(decrypted_word[::-1])  # Reverse it back to original
        else:
            # Just reverse the word back if it was 3 or fewer characters
            decrypted_words.append(word[::-1])

    final_string = ' '.join(decrypted_words)  # Join the decrypted words back into a string
    print("Decrypted string:", final_string)

print("Hey there! Do you want to play an encrypt-decrypt FUN GAME????")
ans = input("Type 'yes' to continue or 'no' to exit: ").strip().lower()
if ans == "no":
    exit()
else:
    while ans == "yes":
        print("What operation do you want to perform?")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit game")
        choice = input("Choose 1, 2, or 3 according to your choice: ").strip()
        match choice:
            case "1":
                encrypt()
            case "2":
                decrypt()
            case "3":
                exit()
            case _:
                print("Invalid choice. Exiting the game.")
                exit()'''
