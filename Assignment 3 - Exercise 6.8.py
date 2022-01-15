# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:57:21 2022

@author: richa
"""

import decimal

# create dictionary for all numbers less than 1000
numerical_words = {}

# loop through each number less than one thousand and 
# generate the string for the corresponding dictionary entry
for number in range(1, 1000):
    
    # set number_string to an empty string
    number_string = ""
    
    # set logical variable in_teens to False
    in_teens = False
    
    # build the strings for numbers in the hundreds
    if number // 900 == 1:
        number_string = "NINE HUNDRED "
    elif number // 800 == 1:
        number_string = "EIGHT HUNDRED "
    elif number // 700 == 1:
        number_string = "SEVEN HUNDRED "
    elif number // 600 == 1:
        number_string = "SIX HUNDRED "
    elif number // 500 == 1:
        number_string = "FIVE HUNDRED "
    elif number // 400 == 1:
        number_string = "FOUR HUNDRED "
    elif number // 300 == 1:
        number_string = "THREE HUNDRED "
    elif number // 200 == 1:
        number_string = "TWO HUNDRED "
    elif number // 100 == 1:
        number_string = "ONE HUNDRED "
        
    # build the tens place string
    if number % 100 // 90 == 1:
        number_string += "NINETY "
    elif number % 100 // 80 == 1:
        number_string += "EIGHTY "
    elif number % 100 // 70 == 1:
        number_string += "SEVENTY "
    elif number % 100 // 60 == 1:
        number_string += "SIXTY "
    elif number % 100 // 50 == 1:
        number_string += "FIFTY "
    elif number % 100 // 40 == 1:
        number_string += "FOURTY "
    elif number % 100 // 30 == 1:
        number_string += "THIRTY "
    elif number % 100 // 20 == 1:
        number_string += "TWENTY "
    else:
        if number % 100 == 19:
            number_string += "NINETEEN"
            in_teens = True
        elif number % 100 == 18:
            number_string += "EIGHTEEN"
            in_teens = True
        elif number % 100 == 17:
            number_string += "SEVENTEEN"
            in_teens = True
        elif number % 100 == 16:
            number_string += "SIXTEEN"
            in_teens = True
        elif number % 100 == 15:
            number_string += "FIFTEEN"
            in_teens = True
        elif number % 100 == 14:
            number_string += "FOURTEEN"
            in_teens = True
        elif number % 100 == 13:
            number_string += "THIRTEEN"
            in_teens = True
        elif number % 100 == 12:
            number_string += "TWELVE"
            in_teens = True
        elif number % 100 == 11:
            number_string += "ELEVEN"
            in_teens = True
        elif number % 100 == 10:
            number_string += "TEN"
            in_teens = True
    
    # if not in teens, check for single digit endings
    if not in_teens:
    
        if number % 10 == 9:
            number_string += "NINE"
        elif number % 10 == 8:
            number_string += "EIGHT"
        elif number % 10 == 7:
            number_string += "SEVEN"
        elif number % 10 == 6:
            number_string += "SIX"
        elif number % 10 == 5:
            number_string += "FIVE"
        elif number % 10 == 4:
            number_string += "FOUR"
        elif number % 10 == 3:
            number_string += "THREE"
        elif number % 10 == 2:
            number_string += "TWO"
        elif number % 10 == 1:
            number_string += "ONE"
        elif number % 10 == 0:
            number_string = number_string.rstrip()
        
    # create a new entry in the dictionary for the number
    # and its corresponding word
    numerical_words[number] = number_string
    
    
# request the user input a check amount
check_amount = decimal.Decimal(input("Input the numerical amount of the check: "))

# determine the integer part of the check amount
check_amount_int = int(check_amount)

# determine the decimal part of the check amount as a whole number
check_amount_dec = int((check_amount - int(check_amount)) * 100)

# using the dictionary, construct the check amount string
check_amount_string = numerical_words[check_amount_int] + f" AND {check_amount_dec:02d}/100"

# print the check amount string
print(check_amount_string)
    
    

