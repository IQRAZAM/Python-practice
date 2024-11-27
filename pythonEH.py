###running some scripts from book python for hackers 
# i  = 5 
# print(i)
# i = i+1
# print(i)
# s = '''this is  a multiline string.
# thsi is secomd line '''
# print(s)
# #########finding area and perimeter
# length = 78
# breadth = 6
# print("so the area of rectangle is",length * breadth)
# print("while the perimeter is ", 2 * (length + breadth))
##########using doc _string in python 
# def square(n):
#     '''Take a number n and return the square of n.'''
#     print( n**2)

# print(square.__doc__)
# square(4)
# import sys
# if len(sys.argv)==2:
#     filename = sys.argv[1]
#     print("[+]Reading vunerablities from " + filename)  
#      #this will run if we write python pythonEH.py(puthon file name ) text.txt(text file name from where you want to read script)

# import sys
# import os
# if len(sys.argv)==2:
#     filename = sys.argv[1]
#     if not os.path.isfile(filename):
#         print("[+]This "+ filename + "does not exist")
#         exit(0)
#     if not os.access(filename , os.R_OK):
#         print("file " + filename + "accessed denied ")
#         exit(0)
#     print("[+]Reading vunerablities from " + filename)  
     