'''
 This program reads valid input file
 and deciphers the words according to key(if given)
 by moving alphabet up by the given key
'''

def main():
    # prompt for input file 
    input_file = input("Enter the input file name: ")
    # open file if valid
    try:
        coded_file = open(input_file, "r")
        # read file line by line
        data = [line for line in (line.strip() for line in coded_file) if line] # remove blank lines
        for line in data:
            line.strip()
            # exception when key is missing
            try:
                word, key = line.split(" ")
                decoded_word = ""
                for letter in word:
                    # get index of current letter
                    # get new letter from new index
                    # need %26 because 26 letters in alphabet
                    # need +97 and -97 to avoid non-alphabet characters 
                    # that Python has in alphabet listing
                    new_index = (97 + (ord(letter.lower())-97+int(key))%26)
                    new_letter = chr(new_index)
                    decoded_word += new_letter
                print(decoded_word.upper())
            except:
                print("Missing key!")
                
        '''
        #~~~~~~~~~~~~~For Simpler Method~~~~~~~~~~~~~
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for line in data:
            line.strip()    
            try:
                word, key = line.split(" ")
                decoded_word = ""
                for letter in word:
                    letter_index = alphabet.index(letter)
                    new_index = (letter_index + int(key)) % 26
                    new_letter = alphabet[new_index]
                    decoded_word += new_letter
                print(decoded_word.upper())
            except:
                print("Missing key!")
        '''
        coded_file.close() 
        
    # if input file invalid
    except:
        print("Input file not valid. Are you not comrade?")
        
main()