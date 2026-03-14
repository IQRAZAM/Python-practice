# print("hello world ")
#######A Generator functon 
''' count():
    for i in range(5):
        yield i
for value in count():
    print(value)'''
##Question 1: Lambda & List Comprehension

# Write a Python function using lambda and map to square all numbers in a list.

# Example input: [1, 2, 3, 4]
# Expected output: [1, 4, 9, 16]
'''bers = [1,2,3,4]
squared = list(map(lambda x:x**2,numbers))
print(squared)'''


list = input("enter the rpices of the items ").split(",")
list = [int(num) for num in list]
print(list)

passed = [score for score in list if score>=50]
print(passed)
