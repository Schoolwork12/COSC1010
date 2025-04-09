#
# Name Tony Dyer
# Date 4/9/2025
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def to_pig_latin(sentence): # defining the main function 
    words = sentence.split() #splitting what we need from the sentence
    pig_latin_words = []

    for word in words:
        if len(word) == 1:  # to check if there is only one letter
            pig_word = word + "AY"  # handle single-letter words like "I"
        else:
            pig_word = word[1:] + word[0] + "AY" # if not then continue on
        pig_latin_words.append(pig_word.upper()) # as usual plus user upper
                                                # because we like yelling!
    return " ".join(pig_latin_words) # join all the single words together

# run the program and get input + make it caps
input_sentence = input("Enter a sentence: ").upper()
pig_latin = to_pig_latin(input_sentence)
print("Pig Latin:", pig_latin) #1