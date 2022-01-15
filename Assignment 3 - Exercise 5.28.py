# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:08:47 2022

@author: Richard Michael
"""

# create list of student responses
responses = [1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,3,2,5]

# import the statistics module
import statistics

# display the requested statistical values
print("The following are statistical quantities generated from student responses:")
print("Min: ", min(*responses))
print("Max: ", max(*responses))
print("Range: ", max(*responses) - min(*responses))
print("Mean: ", statistics.mean(responses))
print("Median: ", statistics.median(responses))
print("Mode: ", statistics.mode(responses))
print("Var: ", statistics.variance(responses))
print("Std. Dev.: ", statistics.stdev(responses))