#
# Name Tony Dyer
# Date 2/13/2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#initial values
TOTAL = 0
DEBT = 0
BUDGET = 0
CONT = 'y'

#doing a while loop just in case they need to add more to the loop
while CONT == 'y':

    #getting the budget specified
    BUDGET = int(input("Please input your budget for the month:  "))

    #getting the amount spent this month
    DEBT = int(input("Now input your total expenditure for the month:  "))

    #calcing the total amount to see if it is greater or less than the budget
    TOTAL = BUDGET - DEBT

    # testing to see if the TOTAL value is lower than 0 aka you went over budget
    # and printing the result
    if TOTAL < 0:
        print(" You silly goose, you should have budgeted better! You're over budget by,", TOTAL)

        #printing if youre under budget
    else:
        print(" Good job you've got an additional,", TOTAL ,"this month!")

        # Just a little something to either continue the loop or break out of it
    CONT = input("Do you wish to continue? Please type and enter 'y' if you'd like to.  ")