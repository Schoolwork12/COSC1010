#
# Name Tony Dyer
# Date 3/29/2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

#import the file needed
def load():
    try:   # This is to see if the file is actually there
        with open('8_ball_responses.txt', 'r') as Ball:
            return[line.strip() for line in Ball if line.strip()] # strip anything
    except FileNotFoundError:                                     # that needs to be stripped
        print ('Error: 8_ball_responses.txt not found!') # if the file isnt found
        return[]
    # try catch block just in case

def magic_8():  # main program start
    response = load()

    if not response:
        return # exit if for some reason the responses couldnt be loaded
    
    print("Magic 8 Ball -- Ask me a Yes/No question, and I will decide your fate!")
    while True:
        print()
        quest = input("Ask your question (or type 'quit' to exit):  ")
        if quest.lower() == 'quit':
            print("May your fate be undecided...")
            break
        print("Magic 8 Ball says:", random.choice(response))
        print()

#run the program
magic_8()