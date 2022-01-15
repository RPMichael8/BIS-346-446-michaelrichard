# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 21:02:41 2022

@author: Richard Michael
"""

# Define the list of tuples
invoices = [(83, "Electric sander", 7, 57.98),
            (24, "Power saw", 18, 99.99),
            (7, "Sledge hammer", 11, 21.50),
            (77, "Hammer", 76, 11.99),
            (39, "Jig Saw", 3, 79.50)]

# a) Sort the tuples by the part description

# import the itemgetter function
from operator import itemgetter

# print the sorted tuple
print("Part A - Print the tuples sorted by part description")
print(sorted(invoices, key=itemgetter(1)))

# b) sort the tuples by price

# print the sorted tuple
print("Part B- Print the tuples sorted by price")
print(sorted(invoices, key=itemgetter(3)))

# c) map each invoice to a tuple containing part description and quantity
# then sort by quantity and display the results

# initialize an empty list
mapped_list = []

# map the invoices to tuples containing part description and quantity 
mapped_list = list(map(lambda x: tuple((x[1], x[2])), invoices))
    
# sort the result by quantity and print it
print("Part C - Print the mapped tuple of part description and quantity sorted by quantity")
print(sorted(mapped_list, key=itemgetter(1)))

# d) map each invoice to a tuple containing part description and the value
# of the invoice then sort by invoice value and display the results

# map the invoices to tuples containing part description and quantity 
mapped_list = list(map(lambda x: tuple((x[1], x[2] * x[3])), invoices))
    
# sort the result by quantity and print it
print("Part D - Print the mapped tuple of part description and value sorted by value")
print(sorted(mapped_list, key=itemgetter(1)))

# e) modify part d to filter the results to inovice value in the range of 
# $200 to $500

# map the invoices to tuples containing part description and quantity 
print("Part E - Print the mapped tuple of part description and value sorted by value and filtered to values between $200 and $500")
mapped_list = list(map(lambda x: tuple((x[1], x[2] * x[3])),
                       filter(lambda x: 200 <= x[2] * x[3] <= 500, invoices)))
    
# sort the result by quantity and print it
print(sorted(mapped_list, key=itemgetter(1)))

# f) calculate the total of all the invoices

# initialize a variable for total
total = 0

# loop through each tuple and sum the invoice totals
for invoice in invoices:
    
    total += invoice[2] * invoice[3]

# print the total    
print(f"Part F - The total of all invoices is ${total}")