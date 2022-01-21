# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:48:24 2022

@author: Richard Michael
"""

# import numpy
import numpy as np

# create a 3x3 array with all even integers from 2 through 18
a = np.arange(2, 19, 2).reshape(3,3)

# print the array
print(a)

# create a 3x3 array with all the integers from 9 down to 1
b = np.arange(9, 0, -1).reshape(3,3)

# print the array
print(b)

# multiply the arrays and display the result
print(a * b)