#
# Name Tony Dyer
# Date 3/18/2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# import of the random lib
import random

max_Digi = 7 # max number of digits 
Start = 0 # start of the random number range
Ending = 9 # end of the random number range

# main function
def main():

    print("The winning Lottery Numbers are!")

    # create list
    numbers = [0] * 7

# populate list with rand numbers
    for index in range(max_Digi):
        numbers[index] = random.randint(Start,Ending)

    # display the rand numbers
    for index in range (max_Digi):
        print(numbers[index], end='')
    print()

    # silly ending statement (Very important I assure you!)
    print("If you've won please tell untrustworthy individuals!")

 # call the main function
main()