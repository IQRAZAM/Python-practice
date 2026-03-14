# count = 0 
# while(count<15):
#     count = count+1 
#     print("bewafa nikli haye tu ")
# print("list iteration")
# I = ["geeks","for","geeks"]
# for i in I:
#     print(i)
#iteration over a string 
# print("string ioteraction")
# s = "Geeks"
# for i in s:
#     print(i)
# list = ["kasam","tere","pyar","ki"]
# for index in range(len(list)):
#     print (list[index])
#####continue break
# letter = "geeksfor geeks"
# for in letter:
#     if (letter == 'e' or letter == 's'):
        
#         continue
#     print("current letter",letter)
#     var = 10
#qwrite a python program to count the numbers of even and odd numbers from a series of numbers e.g we got numbers = (2,5,7,4,2,1,5) then our program should tell us that how many there are even and how many odd numbers
# Given series of numbers
'''numbers = (2, 5, 7, 4, 2, 1, 5)

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Iterate through the numbers and count even and odd
for number in numbers:
    if number % 2 == 0:
        even_count += 1  # Increment even counter
    else:
        odd_count += 1   # Increment odd counter

# Display the results
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)'''
#Q2write a python program that prints each item and its corresponding type from following list :datalist = (1452,11.23,1+2j,True,'wsorce',(0,-1),[5,12])
# Given list of data
'''datalist = (1452, 11.23, 1 + 2j, True, 'wsorce', (0, -1), [5, 12])

# Iterate through each item in the datalist
for item in datalist:
    # Print the item and its type
    print(f"Item: {item}, Type: {type(item)}")'''
#q3write a python program that print all numbers from 0 to 6 except 3 and 6 and use continue statemnet
# Loop through numbers from 0 to 6
'''for number in range(7):
    # Use continue to skip 3 and 6
    if number == 3 or number == 6:
        continue
    # Print the number
    print(number)'''
#q4 write a python program to get the fibonacci series from 0 tot 50
# Function to generate Fibonacci series up to a maximum value
'''def fibonacci_series(max_value):
    fib_series = []
    a, b = 0, 1  # Starting values for the Fibonacci series
    while a <= max_value:
        fib_series.append(a)
        a, b = b, a + b  # Update values for the next Fibonacci number
    return fib_series

# Generate and print the Fibonacci series from 0 to 50
result = fibonacci_series(50)
print("Fibonacci series from 0 to 50:", result)'''
#q5 write a python program which iterates the integers from 1 to 50 foe multiples of 3 print "fizz" instead of numbers and for multiple of 5 print "buz " for numbers which are muliples of 5 and 3 both print "fizzBuzz"
# Iterate through numbers from 1 to 50
'''for number in range(1, 51):
    # Check for multiples of both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("fizzBuzz")
    # Check for multiples of 3
    elif number % 3 == 0:
        print("fizz")
    # Check for multiples of 5
    elif number % 5 == 0:
        print("buz")
    else:
        print(number)  # Print the number itself if it's not a multiple of 3 or 5'''
#q6write a python program which takes two digits m(row) and n(columns) as input and generate two deimensional array the element value in th ith row and jth column of an array should be i*j i = 0 , 1, .........,m-1 like that
# Function to generate a 2D array
'''def generate_2d_array(m, n):
    # Create a 2D array using list comprehension
    array = [[i * j for j in range(n)] for i in range(m)]
    return array

# Take user input for number of rows (m) and columns (n)
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# Generate the 2D array
result_array = generate_2d_array(m, n)

# Print the resulting 2D array
print("Generated 2D Array:")
for row in result_array:
    print(row)'''
#q6 write a pyhton prgram that excepts a sequence of lines (blank line to terminate ) as input and prints the line as out put (all characters in lowercase )
'''def main():
    print("Enter lines of text (blank line to terminate):")
    lines = []
    
    while True:
        line = input()  # Accept input from the user
        if line == "":  # Check for a blank line
            break  # Exit the loop if a blank line is entered
        lines.append(line.lower())  # Append the line in lowercase to the list
    
    print("\nOutput:")
    for line in lines:
        print(line)  # Print each line in lowercase

if __name__ == "__main__":
    main()'''
#q7 write apython program which accepts a sequence of commas separeted by 4 digit binary numbers as its input and and print the numbers that are divisible by 5 in a comma separeted sequence sample 1001,1010,1011,1000,1111,1100
'''def main():
    # Accept input from the user
    binary_numbers = input("Enter a sequence of comma-separated 4-digit binary numbers: ")
    
    # Split the input string into a list of binary numbers
    binary_list = binary_numbers.split(',')
    
    # Initialize a list to hold numbers divisible by 5
    divisible_by_5 = []
    
    # Iterate through the list of binary numbers
    for binary in binary_list:
        # Convert binary string to decimal
        decimal_number = int(binary, 2)
        
        # Check if the decimal number is divisible by 5
        if decimal_number % 5 == 0:
            divisible_by_5.append(binary)  # Append the original binary number to the list
    
    # Print the result as a comma-separated string
    if divisible_by_5:
        print("Numbers divisible by 5:", ','.join(divisible_by_5))
    else:
        print("No numbers divisible by 5 found.")

if __name__ == "__main__":
    main()'''
#q8 write a python program that accepts string and calculate the number of digits and letters e.g we got 36 people in our party out put no. of digits
'''def count_digits_and_letters(input_string):
    digits_count = 0
    letters_count = 0
    
    for char in input_string:
        if char.isdigit():  # Check if the character is a digit
            digits_count += 1
        elif char.isalpha():  # Check if the character is a letter
            letters_count += 1
            
    return digits_count, letters_count

def main():
    # Accept input from the user
    input_string = input("Enter a string: ")
    
    # Calculate the number of digits and letters
    digits_count, letters_count = count_digits_and_letters(input_string)
    
    # Print the results
    print(f"Number of digits: {digits_count}")
    print(f"Number of letters: {letters_count}")

if __name__ == "__main__":
    main()'''
# Q8 write a python program to chec the validity of the password entered by user
# At least one letter between [a-z].
# At least one letter between [A-Z].
# At least one number between [0-9].
# At least one special character.
# Minimum length of 6 characters.
# Maximum length of 16 characters.
'''import re

def is_valid_password(password):
    # Check length
    if len(password) < 6 or len(password) > 16:
        return False
    
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    
    # Check for at least one digit
    if not re.search(r"[0-9]", password):
        return False
    
    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    
    return True

def main():
    # Accept password input from the user
    password = input("Enter a password: ")
    
    # Validate the password
    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid. Please ensure it meets the criteria.")

if __name__ == "__main__":
    main()'''
    