# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:22:25 2022

@author: Richard Michael
"""

def summarize_letters(string): 
    """Takes a string and summarizes frequency of each letter
    in string and returns a list of tuples containing results"""
    
    # make all of the characters in string lowercase
    string = string.lower()
    
    # create blank list of tuples variable
    list_of_tuples = []
    
    # loop through the letters of string to create the list of tuples
    for letter in string:
        
        # if character is not a letter (outside appropriate ascii range), 
        # skip the iteration of the loop
        if not (97 <= ord(letter) <= 122):
            
            continue
        
        # create a variable used to determine if the letter is in the list
        in_list = False
        
        # loop through each tuple and check for the letter
        for letter_tuple in list_of_tuples:
            
            # if the letter is in the tuple, set in_list to true
            if letter_tuple[0] == letter:
                
                #set in_list to true
                in_list = True
        
        # if the letter is not in the list, add the tuple to the list
        if not in_list:
        
            # add the tuple to the list
            list_of_tuples.append(tuple((letter, string.count(letter))))  
            
    # return the list of tuples
    return list_of_tuples
 
    
# string from which you want to generate a list of letters
# test strings
string = "abcdefghijklmnopqrstuvwxyz"
#string = "abcdeffghijk lmnopqrs tuvwx,yz"
#string = "Richard Michael"

# list of tuples showing count of letter occurences
list_of_tuples = summarize_letters(string)

# print the list of tuples   
print(list_of_tuples)

# if the list contains all of the letters of the alphabet state it
if len(list_of_tuples) == 26:
    
    print("Wow! This string contains all of the letters of the alphabet!")
  
# else, report that the string is missing some of the letters of the alphabet
else:
    
    print("This string is missing some of the letters of the alphabet.")

    