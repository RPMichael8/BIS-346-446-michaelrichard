# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:35:27 2022

@author: Richard Michael
"""

# declare sentence variable to hold the sentence from which to identify 
# duplicate words
sentence = "This is a very long and very wordy run on sentence which will allow \
                us to test out this script which will determine if there is \
                duplicate words and list those words if they are duplicate words"

# initialize a word_counts dictionary
word_counts = {}

# count the occurences of each unique word **Borrowed from example 6.2.7**
for word in sentence.split():
    if word.lower() in word_counts:
        word_counts[word.lower()] += 1
    else:
        word_counts[word.lower()] = 1
        
# initialize duplicates variable to hold the number of duplicate words
duplicates = 0

# loop through each entry in the dictionary to look for duplicate words
for word, count in word_counts.items():
    
    # if count is greater than 1, increment duplicates
    if count > 1:
        
        #increment duplicates
        duplicates = duplicates + 1
        
# print the result
print(f"There are {duplicates} duplicate words in the sentence!")