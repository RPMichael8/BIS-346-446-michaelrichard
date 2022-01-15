# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 09:17:10 2022

@author: Richard Michael
"""

# import random in order to use randrange for the die roll
import random

# define a list containing each space on a monopoly board
monopoly_spaces = ["Go",
                   "Mediterranean Avenue",
                   "Community Chest",
                   "Baltic Avenue",
                   "Income Tax",
                   "Reading Railroad",
                   "Oriental Avenue",
                   "Chance",
                   "Vermont Avenue",
                   "Connecticut Avenue",
                   "Jail / Just Visiting",
                   "St. Charles Place",
                   "Electric Company",
                   "States Avenue",
                   "Virginia Avenue",
                   "Pennsylvania Railroad",
                   "St. James Place",
                   "Community Chest",
                   "Tennessee Avenue",
                   "New York Avenue",
                   "Free Parking",
                   "Kentucky Avenue",
                   "Chance",
                   "Indiana Avenue",
                   "Illinois Avenue",
                   "B. & O. Railroad",
                   "Atlantic Avenue",
                   "Ventnor Avenue",
                   "Water Works",
                   "Marvin Gardens",
                   "Go To Jail",
                   "Pacific Avenue",
                   "North Carolina Avenue",
                   "Community Chest",
                   "Pennsylvania Avenue",
                   "Short Line",
                   "Chance",
                   "Park Place",
                   "Luxury Tax",
                   "Boardwalk"]

# initialize variable player to hold player position starting at 0
player = 0

# initialize a variable that states what move number the player is on
move = 1

# repeat loop while player has not landed on Boardwalk (player = 39)
while player != 39:
    
    # print a header which states the move number
    print(f"-------------------------MOVE #{move}-------------------------")
    
    # roll die 1
    die1 = random.randrange(1,7)
    
    # roll die 2
    die2 = random.randrange(1,7)
    
    # print the results of the die rolls
    print(f"Die 1: {die1}\tDie 2: {die2}")
    
    # calculate the move distance
    move_distance = die1 + die2
    
    # calculate the player's new position
    player += move_distance
    
    # if the move distance is greater than 39, adjust it so 
    # it is within the confines of the game board
    if player > 39:
        
        # subtract 40 from the player position
        player = player - 40
        
    # display the move distance and the space they land on
    print(f"Player moves {move_distance} spaces and lands on {monopoly_spaces[player]}.")
    
    # increment the move counter
    move += 1
    
    
# when the script exits the while loop, the game is over - announce this
print("\nGame over! Congratulations, you won!")
        