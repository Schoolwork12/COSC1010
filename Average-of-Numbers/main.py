#
# Name Tony Dyer
# Date 3/10/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# open the file
num_file = open('numbers.txt', 'r')

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