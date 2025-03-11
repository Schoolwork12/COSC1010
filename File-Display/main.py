#
# Name Tony Dyer
# Date 3/10/2025
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# open the file
num_file = open('numbers.txt', 'r')
# read/display the files contents
for line in num_file:
    number = int(line)
    print(number)
#close the file
num_file.close()
