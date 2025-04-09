#
# Name Tony Dyer
# Date 1/28/2025
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations
uservar = float(input("How much did you buy this for?   ")) # I would add an error catch and write 
# Constants for the state and county tax rates              # something silly but I dont know how currently
statesalesT = 0.05
countysalesT = 0.025
# Get the amount of the purchase.

# Calculate the state sales tax.
totaltS = uservar * statesalesT  
# Calculate the county sales tax.
totaltC = uservar * countysalesT
# Calculate the total tax.
totalT = totaltS + totaltC
# Calculate the total of the sale.
overall = uservar + totalT
# Print information about the sale.
print('The State Tax for this is $', format(totaltS,'.2f')) # I had to look up how to format things since I was
print('The Total County Tax  is $',format(totaltC, '.2f'))  # grossed out by the .5408 I was getting in some outputs
print('The total sale for this is $', format(overall,'.2f' )) # if you want the resource I got it from https://www.youtube.com/watch?v=FrvBwdAU2dQ