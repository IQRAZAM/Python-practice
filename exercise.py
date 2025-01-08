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
#####Q5 make a snake water gun game , we will use 2 methods simply one simple if and else statements and one by using 2 dimesional matrix
'''import random 
def computer_choice():
    choices = ["snake","water","gun"]
    return random.choice(choices)
    #The random.choice() function is a built-in function from the random module. It takes a sequence (like a list or a tuple) as an argument and returns a randomly selected element from that sequence.
def user_choice():
    get_user_input = input("enter the choice you want : ('snake','water','gun')").lower()
    while get_user_input not in ["snake","water","gun"]:
        print("invalid choice plz choose from this ; ['snake','water','gun']")
        get_user_input = input("enter the choice you want : ('snake','water','gun')").lower()
    return  get_user_input 
def determie_winner(computer ,user):
    if computer == user :
        return "its a draw!!"
    elif (computer == "snake" and user == "gun") or (computer == "gun" and user == "water") or (computer =="water" and user == "snake"):
        return "user wins!!"
    else :
        return "computer wins !!"
def play_game():
    print("welcome to snake water gun game !")
    compChoice  = computer_choice()
    usChoice  = user_choice()
    print(f"Computer chose: {compChoice}")
    print(f"You chose: {usChoice}")
    result = determie_winner(compChoice,usChoice)
    print(result)
if __name__  == "__main__":
    play_game()'''
########Q7 write a libarary class with no. of books and books as two diferent varaibles ,write a program to create a libarary from libarary class ,and sow how can you print all books , add books and get the no. of books using different ,ethods show that your program doesn't persist the books after the program is stopped .
'''class Library:
    no_of_books = 5 
    Books = ["Amarbail","Mala","silent Patient","sulphite","Maseel"]
    def Print_books(self):
        print("So the list of the book in this library is as follows:")
        print(self.Books)
    def add_books(self):
        choice = input("write the name of the book you wanna add:")
        self.Books.append(choice)
        print("so the new liast after addition of your book is ")
        print(self.Books)
        self.no_of_books = self.no_of_books + 1 
    def check_books_count(self):
         if self.no_of_books == len(self.Books):
             print("your count is correct which is ", self.no_of_books )
         else:
             print("count is wrong and maybe there a probelm !")
print("WELCOME TO LIBRARY MANAGEMENT SYSTEM!!!")
reader = Library()
reader.Print_books()
reader.add_books()
reader.check_books_count()'''
#####we have to write a program in which we need to clear the clutter in a folder by using OS model in python also use OS module to change the names of the files in that folder 
'''import os 
#make a directory
directory_name = "Exercise_dir"
try:
      os.mkdir(directory_name)
      print(f"dircetory {directory_name} created ")
except FileExistsError:
      print(f"directory {directory_name} alreday exists")
 #now we will create 20 files 
for i in range(1 , 21):
      file_name = f"file_{i}.txt"
      file_path = os.path.join(directory_name , file_name)
      with open (file_path , 'w') as file:
           file.write(f"this is the file no. {i}")
           print(f"file '{file_name}' is being cteated in directory '{directory_name}'.")
      new_file_name = f"new_file_{i}.txt"
      new_file_path = os.path.join(directory_name , new_file_name)
      os.rename(file_path,new_file_path)
      print(f"file '{file_name}' is being changed to'{new_file_name}'.")
      os.remove(new_file_path)

print("all files are created successfully ")
print("and then renamed successfully ")
#now we wil chamge the name of the files by using same above loop 
#now finally deleting the whole dir
os.removedirs(directory_name)'''
#write a program to merge pdf using pyPDF module in python should be able to merge multiple pdf files into one file 
import pypdf

def merge_pdfs(pdf_list, output_filename):
    # Create a PDF writer object
    pdf_writer = pypdf.PdfWriter()

    # Loop through the list of PDF files
    for pdf in pdf_list:
        # Open each PDF file
        with open(pdf, 'rb') as file:
            pdf_reader = pypdf.PdfReader(file)  # Create a PDF reader object
            # Add each page to the writer object
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])

    # Write the merged PDF to a new file
    with open(output_filename, 'wb') as output_file:
        pdf_writer.write(output_file)

# List of PDF files to merge
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']  # Replace with your PDF file names
output_pdf = 'merged_output.pdf'  # Name of the output file

# Merge the PDF files
merge_pdfs(pdf_files, output_pdf)

print(f"Merged PDF saved as '{output_pdf}'")


     
