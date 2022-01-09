# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 19:45:54 2022

@author: Richard Michael
"""

def fahrenheit(celsius):
    """Convert the provided Celsius temperature into Fahrenheit"""
    # return the fahrenheit equivalent
    return (9 / 5) * celsius + 32

"""Print a chart of all the Fahrenheit equivalents for each 
Celsius temperature from 0 to 100"""

# print a header for the output
print("Celsius\t\tFahrenheit")

# loop through C temperatures 0 through 100 and convert to F
for c in range(101):
    
    # print out the celsius value and the fahrenheit value 
    # calculated using the fahrenheit function
    print(f'{c:.1f} \t\t {fahrenheit(c):.1f}')