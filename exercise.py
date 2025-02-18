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
'''import pypdf

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
pdf_files = ['OOP.pdf', 'dld.pdf', 'cover page.pdf']  # Replace with your PDF file names
output_pdf = 'merged_output.pdf'  # Name of the output file

# Merge the PDF files
merge_pdfs(pdf_files, output_pdf)

print(f"Merged PDF saved as '{output_pdf}'")'''
##write a program to to pronouncr list of names using wins32 API in python if you are given a list of names you should be able to pronounce the shoutout to name like that 
# from gtts import gTTS
# import os

# # List of names
# names = ["Alice", "Bob", "Charlie", "David","Alice", "Bob", "Charlie", "David"]

# # Loop through each name in the list
# for name in names:
#     # Create the shoutout message
#     shoutout_message = f"Shoutout to {name}!"
    
#     # Create a gTTS object
#     tts = gTTS(text=shoutout_message, lang='en', slow=False)
    
#     # Save the audio file
#     audio_file = f"shoutout_{name}.mp3"
#     tts.save(audio_file)
    
#     # Optionally, play the audio file
#     os.system(f"start {audio_file}")  # For Windows
#     # os.system(f"afplay {audio_file}")  # For macOS
#     # os.system(f"mpg321 {audio_file}")  # For Linux

# print("Shoutouts have been generated and played!")
###using another module as well 
'''import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# List of names
names = ["Alice", "Nayyab", "Sidra", "Insha", "Sara", "Ayush Battun", "Natalia", "Sheikh"]

# Function to speak a name
def speak_name(name):
    shoutout_message = f"Shoutout to {name}!"
    engine.say(shoutout_message)
    engine.runAndWait()  # Wait for the speech to finish

# Loop through each name in the list and speak it
for name in names:
    speak_name(name)

print("Shoutouts have been spoken!")'''
#Q11use the NEWSAPI and request module to fetc the daily news related to different topics make a cool appliaction an dfetch news as much as you wat and make sure to thin about the choices of user who gonna use this application
#newsapi key :8a694f9e6a564a6cadedba832a32ef7e
'''import requests

# Your API key
API_KEY = '8a694f9e6a564a6cadedba832a32ef7e'
BASE_URL = 'https://newsapi.org/v2/top-headlines'
# Define news categories
categories = {
    1: 'K-Pop',
    2: 'Hollywood',
    3: 'Bollywood',
    4: 'Music Industry',
    5: 'Pakistan',
    6: 'Modeling World',
    7: 'Technology',
    8: 'Sports',
    9: 'Business',
    10: 'Health',
    11: 'Environment',
    12: 'Education',
    13: 'Travel',
    14: 'Finance',
    15: 'Food and Nutrition',
    16: 'Fashion',
    17: 'Automotive',
    18: 'Gaming',
    19: 'Cryptocurrency',
    20: 'Mental Health'
}
def fetch_news(category):
    params = {
        'q': category,
        'apiKey': API_KEY,
        'language': 'en'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()['articles']       #The json() method parses the response body (which is typically in JSON format) and converts it into a Python dictionary (or list, depending on the structure of the JSON).
    else:
        print(f"Error fetching news: {response.status_code}")
        return []
def main():
    print("Select a news category:")
    for key, value in categories.items():
        print(f"{key}. {value}")

    choice = int(input("Enter your choice (1-20): "))
    
    if choice in categories:
        news_articles = fetch_news(categories[choice])
        if news_articles:
            for article in news_articles:
                print(f"Title: {article['title']}")
                print(f"Source: {article['source']['name']}")
                print(f"URL: {article['url']}\n")
        else:
            print("No articles found.")
    else:
        print("Invalid choice. Please select a number between 1 and 10.")

if __name__ == "__main__":
    main()'''
##write a python program which reminds you of drinking water every hour your programe can either beep or send desktop notifications for a specific operating system 
import time
from plyer import notification

def remind_me(interval):
    while True:
        time.sleep(interval)
        notification.notify(
            title="Drink Water Reminder",
            message="It's time to drink some water! Stay hydrated!",
            app_name="Water Reminder",
            timeout=10  # Notification will disappear after 10 seconds
        )

def main():
    print("Welcome to the Water Reminder App!")
    choice = input("Do you want to be reminded every hour or at a specific time? (hour/specific): ").strip().lower()
    
    if choice == "hour":
        interval = 3600  # 1 hour in seconds
        remind_me(interval)
    elif choice == "specific":
        specific_time = input("Enter the time in HH:MM format (e.g., 14:30): ").strip()
        current_time = time.strftime("%H:%M")
        while current_time != specific_time:
            time.sleep(10)  # Check every 10 seconds
            current_time = time.strftime("%H:%M")
        notification.notify(
            title="Drink Water Reminder",
            message="It's time to drink some water! Stay hydrated!",
            app_name="Water Reminder",
            timeout=10
        )
    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()