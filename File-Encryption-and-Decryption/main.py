#
# Name Tony Dyer
# Date 7/21/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#I dont know if you wanted two seperate project files or not
#but just in case I encased it into one file


def encrypt_file(input_file, output_file, codes):

# try catch just in case something silly happens
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            text = infile.read()

            # starting of the encryption and grabing the encoding
            #characters and the replacing the current text
            # with the provided encryption key called codes

            encrypted_text = ''.join(codes.get(char, char) for char in text)
            outfile.write(encrypted_text)

            # writing the encryption to the screen as well
            print("\n=== Encrypted Content ===\n")
            print(encrypted_text + "\n")

            # end of the encryption

        print(f"\n File encrypted successfully and saved to '{output_file}'!\n")

# incase someone was silly and put an invalid file that cant be found
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")

        # incase the encryption messes up for some reason
    except Exception as e:
        print(f"An error occurred during encryption: {e}")


 # start of the decryption program
def decrypt_file(input_file, codes):

    # try catch incase something goes wrong
    try:

        # reversing the encoded text with the correct letters/numbers/characters
        reverse_codes = {v: k for k, v in codes.items()}
        with open(input_file, 'r') as infile:
            encrypted_text = infile.read()

            #reversing the encoded characters with the correct ones
            decrypted_text = ''.join(reverse_codes.get(char, char) for char in encrypted_text)

            #printing the decrypted text to the screen
            print("\n=== Decrypted Content ===\n")
            print(decrypted_text + "\n")

        #end of the decryption program

        # just in case something silly happens 
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

# this was a pain to write out + this is the encryption key
codes = {
    'A': '1',  'a': '2',  'B': '3',  'b': '4',  'C': '5',  'c': '6',
    'D': '7',  'd': '8',  'E': '9',  'e': '0',  'F': 'A',  'f': 'B',
    'G': 'C',  'g': 'D',  'H': 'E',  'h': 'F',  'I': 'G',  'i': 'H',
    'J': 'I',  'j': 'J',  'K': 'K',  'k': 'L',  'L': 'M',  'l': 'N',
    'M': 'O',  'm': 'P',  'N': 'Q',  'n': 'R',  'O': 'S',  'o': 'T',
    'P': 'U',  'p': 'V',  'Q': 'W',  'q': 'X',  'R': 'Y',  'r': 'Z',
    'S': 'a',  's': 'b',  'T': 'c',  't': 'd',  'U': 'e',  'u': 'f',
    'V': 'g',  'v': 'h',  'W': 'i',  'w': 'j',  'X': 'k',  'x': 'l',
    'Y': 'm',  'y': 'n',  'Z': 'o',  'z': 'p',  '0': 'q',  '1': 'r',
    '1': 'r',  '2': 's',  '3': 't',  '4': 'u',  '5': 'v',  '6': 'w',
    '7': 'x',  '8': 'y',  '9': 'z', ',' : '!',  '.': '#',  '-': '$',
    ' ': '&'
}

def main():  # main program for a nice little interface 
    while True:
        print("=== File Encryptor/Decryptor ===")
        print("1. Encrypt a file")
        print("2. Decrypt a file and print it")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            input_file = input("Enter the name of the file to encrypt (e.g., text.txt): ").strip()
            output_file = input("Enter the name of the encrypted output file (e.g., encrypted.txt): ").strip()
            encrypt_file(input_file, output_file, codes)

        elif choice == '2':
            input_file = input("Enter the name of the file to decrypt (e.g., encrypted.txt): ").strip()
            decrypt_file(input_file, codes)

        elif choice == '3':
            print("Exiting program. Cya later nerd!")
            break

        else:
            print("Invalid choice silly fella. Please select 1, 2, or 3.\n")

if __name__ == "__main__": # calling the main program
    main()