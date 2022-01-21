# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:55:33 2022

@author: Richard Michael
"""

# import numpy
import numpy as np

# create 2x3 array containing the first 6 powers of 2
original = np.array([2 ** x for x in range(6)]).reshape(2,3)

# flatten the array with flatten
flattened = original.flatten()

# print flattened
print(flattened)

# flatten the array with ravel
raveled = original.ravel()

# print raveled
print(raveled)

# print the original array
print(original)