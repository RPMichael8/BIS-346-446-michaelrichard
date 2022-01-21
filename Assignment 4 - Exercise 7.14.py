# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:03:40 2022

@author: Richard Michael
"""

# import numpy
import numpy as np

# create the two 2D arrays
array1 = np.array([[0,1],[2,3]])
array2 = np.array([[4,5],[6,7]])

# a) create 4x2 array3 with array1 stacked on top of array2 and print
array3 = np.vstack((array1, array2))
print(array3)

# b) create 2x4 array4 with array2 to the right of array1 and print
array4 = np.hstack((array1, array2))
print(array4)

# c) use vertical stacking with array4 to create 4x4 array5 and print
array5 = np.vstack((array4, array4))
print(array5)

# d) use horizontal stacking with array 3 to create 4x4 array 6 and print
array6 = np.hstack((array3, array3))
print(array6)