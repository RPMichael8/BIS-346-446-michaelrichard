# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:50:28 2022

@author: Richard Michael
"""

# initialize max number to 0
max_num = 0
second_num = 0

# loop 10 times to prompt the user to enter a number and save
# the number if it larger than the last
for n in range(10):
    
    # prompt the user to input a number
    input_num = float(input("Please enter a number: "))
    
    # if the inputted number is greater than or equal to the 
    # previous maximum number, then reassign the inputted
    # number to the maximum number and previous maximum number to
    # the second largest number
    if input_num >= max_num:
        second_num = max_num
        max_num = input_num
    # else if the inputted number is greater than or equal to the
    # previous second largest number, reassign the inputted
    # number to the second largest number
    elif input_num >= second_num:
        second_num = input_num
        
# print the largest two numbers
print(f"The largest number entered was {max_num}")
print(f"The second largest number entered was {second_num}")
    