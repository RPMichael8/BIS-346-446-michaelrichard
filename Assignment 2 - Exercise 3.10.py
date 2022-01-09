# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 13:27:46 2022

@author: Richard Michael
"""

"""Assign the variables that will remain fixed for each calculation"""
# first assign 1000 to the principal (p)
p = 1000
# next assign .07 to the rate of return (r)
r = 0.07

"""Loop through each year from 1 to 30 and determine the amount of 
money at the end of each year"""
# loop for each year (n) in range 1 to 30
for n in range(1, 31):
    
    # calculate the amount for the year
    a = p * (1 + r)**n
    
    # print the amount for the year
    print(f"After {n} years you will have ${a:,.2f}.")