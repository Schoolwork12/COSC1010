#
# Name Tony Dyer
# Date 2/19/2025
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# define the coversion
CONVERSION_FACTOR = 0.6214

# main function that gets a distance in kilometers and calls
# the show miles function to convert it
def main():
    kilometers = float(input("Enter a distance in kilometers:  "))
    
    # display the distance converted to miles
    show_miles(kilometers)

# the show miles function converts the parameter km form
# kilometers to miles and displays the result
def show_miles(km):

    # calc miles
    miles = km * CONVERSION_FACTOR

    # display the miles
    print(km, 'kilometers equals', miles, 'miles.')
# calls the main function
main()