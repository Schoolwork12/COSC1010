#
# Name Tony Dyer
# Date 2/19/2025
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Const var
INCHES_PER_FOOT = 12

# user input 
def main():
    feet = int(input("Please input the amount of feet you wish to convert:  "))

# convert to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# the feet to inches function converts feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# call to the main function 
main()
    
    