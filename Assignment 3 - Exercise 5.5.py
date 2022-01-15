# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:58:08 2022

@author: Richard Michael
"""

# create alphabet string
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# a) first half of string using starting and ending indices
print(alphabet[0:13])

# b) first half of string using only ending index
print(alphabet[:13])

# c) second half of string using starting and ending indices
print(alphabet[13:26])

# d) second half of string using only starting index
print(alphabet[13:])

# e) every second letter of string starting with a
print(alphabet[::2])

# f) the entire string in reverse
print(alphabet[::-1])

# g) every third letter of string in reverse starting with z
print(alphabet[::-3])