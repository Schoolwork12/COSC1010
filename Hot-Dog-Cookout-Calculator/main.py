#
# Name Tony Dyer
# Date 2/7/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# const
HOT_DOGS_PER_PACKAGE = 10
BUNS_PERPACKAGE = 8

# local vars
numAttending = 0    # Number of people attending
numPerPerson = 0    # num of hotdogs and buns per person
total = 0   # the total number of hot dogs and buns needed
minDogs = 0     # min number of packages of hot dogs
minBuns = 0     # min number of packages for hot dog buns
dogsLeft = 0    # number of hot dogs left over from a package
bunsLeft = 0    # number of hot dog buns left over from a package

# get the number of people attending
numAttending = int(input("Enter the number of people attending the cookout:  "))

# get the number of hot dogs per person
numPerPerson = int(input(" Enter the number of hotdogs per person:  "))

# calc total the number of hotdogs and buns needed
total = numAttending * numPerPerson

# calc the min number of packages of hot dogs needed
minDogs = total // HOT_DOGS_PER_PACKAGE 

# determin if the number of people attending is large enough to req more than one package of hotdogs
if minDogs > 0:
    #calc the number of hotdogs left over from a package inf any
    dogsLeft = total % HOT_DOGS_PER_PACKAGE

    # if there will be left overs add additional package of hot dogs
    if dogsLeft != 0:
        minDogs += 1

# set the min number of packages of hot dogs to one because the number of people attending is small enough to only need one package        
else:
    minDogs = 1


# determine if the number of leftover hot dogs if any
dogsLeft = (HOT_DOGS_PER_PACKAGE * minDogs) - total


###### for Buns

# calc the min number of packages of hot dog buns needed
minBuns = total // BUNS_PERPACKAGE 

# determin if the number of people attending is large enough to req more than one package of buns
if minBuns > 0:
    #calc the number of buns left over from a package inf any
    bunsLeft = total % BUNS_PERPACKAGE

    # if there will be left overs add additional package of buns
    if bunsLeft != 0:
        minBuns += 1

# set the min number of packages of buns to one because the number of people attending is small enough to only need one package        
else:
    minBuns = 1


# determine if the number of leftover buns if any
bunsLeft = (BUNS_PERPACKAGE * minBuns) - total

# display the min packages of hot dogs needed
print('Minimum number of packages of hot dogs needed : ', minDogs)

# display the min packages of buns needed
print('Minimum number of packages of hot dog buns needed: ', minBuns)

# display the number of left over hot dogs
print('Hot dogs left over: ', dogsLeft)

# display the number of left over hot dog buns
print('Hot dog buns left over: ', bunsLeft)
