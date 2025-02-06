#
# Name Tony Dyer
# Date 2/5/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

#get input from the user
people = int(input("Enter the number of people attending the cookout: "))
hotdogs_perp = int(input("Enter the number of hot dogs each person will get: "))

#calculate total hot dogs and buns needed
totaldogs = people * hotdogs_perp
totalb = people + hotdogs_perp

#calculate the minimum number of packages needed
hotdogp = (totaldogs + 9) // 10  #rounding to next package
bunp = (totalb + 7) // 8  #rounding to next package

#calculate leftovers
leftoverdogs = (hotdogp * 10) - totaldogs
leftoverb = (bunp * 8) - totalb

#display results
print(f"Minimum number of packages of hot dogs required: {hotdogp}")
print(f"Minimum number of packages of hot dog buns required: {bunp}")
print(f"Number of hot dogs left over: {leftoverdogs}")
print(f"Number of hot dog buns left over: {leftoverb}")