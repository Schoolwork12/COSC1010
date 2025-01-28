#
# Name
# Date
# Sales Prediction Programming Project
# COSC 1010
#

# Variables to hold the sales total and the profit
userval = float(input("Please input your projected sales! $ "))
profit = 0.23
# Get the amount of projected sales.       I'll be honest, these comments are really confusing for me in how im supposed to
                                         # write this code 
# Calculate the projected profit.
totalP = profit * userval
# Print the projected profit.
print('Your projected profit is $',format(totalP,',.2f'))