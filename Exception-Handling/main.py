#
# Name Tony Dyer
# Date 3/18/2025
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
try:
   with open('numbers.txt', 'r') as num_file:
# accumulators

    total = 0
    amountofnumb = 0

# read and process each line
    for line in num_file:
        number = int(line.strip())  # convert line to integer + strip if needed
        total += number  # add number to total
        amountofnumb += 1  # count the number of entries

# close the file
    num_file.close()

# calculate and display the average
    if amountofnumb > 0:  # prevent division by zero just in case!
        average = total / amountofnumb
        print(f"Average: {average}")
    else:
        print("The file is empty, cannot calculate an average.")
except (IOError, ValueError):
    print("There was a problem opening and reading data in your file!")
    print("This could be due to a missing file, a file read error or invalid data.")