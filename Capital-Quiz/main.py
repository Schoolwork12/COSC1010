#
# Name Tony Dyer
# Date 4/15/2025
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

def main():
    #initialize the state_caps dictionary
    state_caps = state_cap_dictionary()

    # variables to keep count of the number
    # of correct and incorrect answers
    correct = 0
    incorrect = 0
    current_cont = 0 # will come in handy later

    #converting the dictionary to items to a list and shuffle
    items = list(state_caps.items())
    random.shuffle(items) #shuffles the list

    #quiz the user
    for state, capital in items:

        #quiz the user
        print('What is the capital of ', state, '? ''\n')
        response =  input()

        #is the user correct
        if response.lower() == capital.lower():
            correct += 1
            print()
            print('Correct!\n')
        else:  # if they are incorrect
            incorrect += 1
            print()
            print('Incorrect! The correct answer was,', capital, '\n')
        current_cont +=1 # adding 1 to current_cont

        # every 5 questions it will ask the user if they wish to continue
        # I was tired of looping through all 50 for program end

        if current_cont % 5 == 0:
            cont = input('Would you like to continue? (yes/no): \n').strip().lower()
            if cont not in ['yes','y']:
                 print('\nOkay, I will be ending the quiz early.')
                 break    # sanity saver      

    #display results
    print('Correct resposnes', correct)
    print('Incorrect responses', incorrect)


    # Initialize dictionary
def state_cap_dictionary():
            return{
                'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    # Local variables

    # Continue until user quits the game.

# Call the main function.
main()
