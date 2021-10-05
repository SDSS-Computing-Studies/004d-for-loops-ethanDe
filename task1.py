#!python3 

"""
##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop instead of a while loop.
(2 points)

inputs:
int number

outputs:
multiples of that number

example:
Enter number:4
4 8 12 16 20 24 28 32 36 40 44 48
"""

mult = int(input("Enter an integer: "))
print(mult, mult*2, mult*3, mult*4, mult*5, mult*6, mult*7, mult*8, mult*9, mult*10, mult*11, mult*12)