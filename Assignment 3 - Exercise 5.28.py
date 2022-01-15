# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:08:47 2022

@author: Richard Michael
"""

# create list of student responses
responses = [1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,3,2,5]

# create a 5 element list containing the frequencies of each rating
response_frequency = [0,0,0,0,0]

# loop through each element in responses and populate the response frequency list
for response in responses:
    
    # populate the proper element of the list with the response count
    response_frequency[response - 1] += 1

# announce the displaying of the number of responses
print("The following list summarizes the frequency of each response:")

# loop through each element of response frequency and display the frequency
# of each response
for frequency in range(len(response_frequency)):
    
    # print the frequency of the specific response
    print(f"{frequency + 1}: {response_frequency[frequency]}")

# import the statistics module
import statistics

# display the requested statistical values
print("\nThe following are statistical quantities generated from student responses:")
print("Min: ", min(*responses))
print("Max: ", max(*responses))
print("Range: ", max(*responses) - min(*responses))
print("Mean: ", statistics.mean(responses))
print("Median: ", statistics.median(responses))
print("Mode: ", statistics.mode(responses))
print("Var: ", statistics.variance(responses))
print("Std. Dev.: ", statistics.stdev(responses))