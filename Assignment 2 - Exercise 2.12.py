# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 11:31:41 2022

@author: Richard Michael
"""

"""Assign the variables that will remain fixed for each calculation"""
# First assign 1000 to the principal (p)
p = 1000
# Next assign .07 to the rate of return (r)
r = 0.07

"""Calculate the amount of money you will have after 10 years"""
# Assign 10 to the number of years (n)
n = 10

# Using the compound interest formula, calculate amount (a) after 10 years
a = p * (1 + r)**n

# Print out the result
print(f"After {n} years you will have ${a:,.2f}.")

"""Calculate the amount of money you will have after 20 years"""
# Assign 20 to the number of years (n)
n = 20

# Using the compound interest formula, calculate amount (a) after 20 years
a = p * (1 + r)**n

# Print out the result
print(f"After {n} years you will have ${a:,.2f}.")

"""Calculate the amount of money you will have after 30 years"""
# Assign 30 to the number of years (n)
n = 30

# Using the compound interest formula, calculate amount (a) after 30 years
a = p * (1 + r)**n

# Print out the result
print(f"After {n} years you will have ${a:,.2f}.")