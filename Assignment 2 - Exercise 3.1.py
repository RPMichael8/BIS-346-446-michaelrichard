# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:30:26 2022

@author: Richard Michael
"""

# fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes

# process 10 students
for student in range(10):
    
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    # while the result is not 1 and not 2 keep looping to ask user for input
    while result != 1 and result != 2:
        # get one exam result
        result = int(input('Invalid Entry! Enter result (1=pass, 2=fail): '))

    # if entered result is 1, then increment the number of passes
    if result == 1:
        passes = passes + 1
        
# knowing there are ten students, calculate the number of failures
failures = 10 - passes

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')