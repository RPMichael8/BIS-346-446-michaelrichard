# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 13:16:52 2022

@author: Richard Michael
"""

# ask the user what their problem is
response = input("What is your problem?")

# ask the user if if they have had it before
response = input("Have you had this problem before (yes or no)?")

# respond appropriately based on whether they have previously had the problem
if response.lower() == "yes":
    print("Well, you have it again.")
elif response.lower() == "no":
    print("Well, you have it now.")

# answer to opinion question
"""I think this conversation would convince the user that the entity
at the other end is exhibiting intelligent behavior. Not only does
the script force the computer to ask two consecutive questions which
will make sense regardless of the users input to the first question
but it also displays intelligence by responsing appropriately to 
the users answer to the second question."""