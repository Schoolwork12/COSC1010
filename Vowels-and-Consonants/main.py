#
# Name Tony Dyer
# Date 4/9/2025
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#main function
def main():
    user_str = input(" Enter a string of characters:   ")

    #report the vowels and consonants
    print("That sring has,", num_vowels(user_str), 'vowels and', \
        num_consonants(user_str), 'consonants!')

# the num_vowels function returns the number of
#vowels in the string passed as an argument
def num_vowels(s):
    #making a list containing the vowels
    vowels = ['a','e', 'i', 'o', 'u']
    # initialize an accumulator
    v_count = 0

    #count the vowels in s
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    # return the vowel count
    return v_count

# The num_consonants function returns the number of
# consonants in the string passed as an argument
def num_consonants(s):
    #make a list containing vowels again ;(
    vowels = ['a', 'e', 'i', 'o', 'u']

    #initialize accumulator
    c_count = 0

    #count the sonsonants in s
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1
    #return the consonant count
    return c_count

#call the main function 1
main()