# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:20:00 2022

@author: Richard Michael
"""

"""Simulate the classic race between the tortoise and the hare"""

# import the random module
import random

# define a variable that can be used for the race end spot
RACE_END = 70

def tortoise_move():
    """Returns the number of moves the tortoise should make per round"""
    
    # generate a random number to determine the toroise's move
    tortoise_random = random.randrange(1, 11)
    
    # return the number of moves based off the random number
    if tortoise_random <= 5:    # fast plod
        return 3
    elif tortoise_random <= 7:  # slip
        return -6
    else:                       # slow plod
        return 1
    
def hare_move():
    """Returns the number of moves the hare should make per round"""
    
    # generate a random number to determine the hare's move
    hare_random = random.randrange(1, 11)
    
    # return the number of moves based off the random number
    if hare_random <= 2:        # sleep
        return 0
    elif hare_random <= 4:      # big hop
        return 9
    elif hare_random <= 5:      # big slip
        return -12
    elif hare_random <= 8:      # small hop
        return 1
    elif hare_random <= 10:     # small slip
        return -2
    
def print_positions(hare_position, tortoise_position):
    """Prints the position of the hare and tortoise on the course"""
    
    # loop through each space and decide what to print on the line
    for space in range(1, RACE_END + 1):
        
        # if the space is not equal to either racer's position,
        # simply print a blank space
        if space != hare_position and space != tortoise_position:
            print(" ", end = "")
        # if the space is equal to both racer's positons,
        # print "OUCH!!!"
        elif space == hare_position and space == tortoise_position:
            print("OUCH!!!", end = "")
        # if the space is equal to the hare's position,
        # print "H"
        elif space == hare_position:
            print("H", end = "")
        # if the space is eqaul to the tortoise's position,
        # print "H"
        elif space == tortoise_position:
            print("T", end = "")
        
    # print a newline to move to the next line
    print("", end = "\n")


# begin both racers at position 1
hare_position = 1
tortoise_position = 1

# begin the race
print("BANG !!!!!\nAND THEY'RE OFF !!!!!")

# while neither racer is at or past position 70, continue looping
# to simulate the race
while 1:
    
    # update the positions of the racers ensuring that neither
    # position is less than the starting space (1)
    hare_position = max(1, hare_position + hare_move())
    tortoise_position = max(1, tortoise_position + tortoise_move())

    # perform final adjustment to make sure neither racer has
    # exceeded the end of the 70 spaces
    hare_position = min(RACE_END, hare_position)
    tortoise_position = min(RACE_END, tortoise_position)
    
    # call the function to print the position
    print_positions(hare_position, tortoise_position)
    
    # once a racer has reached the finish line, end the race
    if hare_position == RACE_END or tortoise_position == RACE_END:
        break
    
# announce the winner
if hare_position == RACE_END and tortoise_position == RACE_END:
    print("It's a tie")
elif hare_position == RACE_END:
    print("Hare wins. Yuch.")
else:
    print("TORTOISE WINS!!! YAY!!!")
    
    
    
    