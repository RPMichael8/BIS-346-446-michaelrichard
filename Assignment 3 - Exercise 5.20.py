# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 17:58:01 2022

@author: Richard Michael
"""

def display_table(two_d_list):
    """Accepts a 2D list (two_d_list) and displays it in tabular format"""
    
    # display the header indices
    print("\t\t[0]\t\t[1]")
    
    # iterate for each i in the number of rows contained by the list
    for i in range(len(two_d_list)):
        
        # print the row index along with the first two indices of the list
        print(f"[{i}]\t\t{two_d_list[i][0]}\t\t{two_d_list[i][1]}")
        
        
# test the function
display_table([[1,2],[34,55],[523,5],[656,455],[57,23],[985,634]])