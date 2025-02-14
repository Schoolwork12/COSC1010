#
# Name Tony Dyer
# Date 2/13/2025
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
TOTAL = 0
BUG_VAR = 0
# Get number of bugs collected each day using a for loop.
for day in range(1,6):
    print("Total number of bugs collected on day,", day  )
    BUG_VAR = int(input())
    TOTAL += BUG_VAR
# Display the total number of bugs collected.
    print("You collected a total of", TOTAL ,"bugs!")
