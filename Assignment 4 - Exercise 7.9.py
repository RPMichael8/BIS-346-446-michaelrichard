# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:46:47 2022

@author: Richard Michael
"""

# import numpy
import numpy as np

# create array containing 1-15 and reshape it into a 3x5 array
a = np.arange(1,16).reshape(3,5)

# print a
print(a)

# a) select row 2
print(a[2])

# b) select column 4
print(a[:,4])

# c) select rows 0 and 1
print(a[[0,1]])

# d) select columns 2-4
print(a[:,2:5])

# e) select the element that is in row 1 and column 4
print(a[1,4])

# f) select all elements from rows 1 and 2 that are in columns 0, 2, and 4
print(a[1:3,[0,2,4]])