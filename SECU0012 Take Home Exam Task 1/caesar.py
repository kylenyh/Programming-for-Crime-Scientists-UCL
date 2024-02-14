
# encryption/decryption caesar cipher algorithm
while True:
    user_choice = input("Enter e/d:")  # variable that allows the user to input choice 
    if user_choice in ('e', 'd'):  # if the user chooses e or d, the program proceeds
        break
    else:
        print("Please enter 'e' for encrypt or 'd' for decrypt.")  # otherwise, a statement is printed 

while True:
    user_shift_input = input("Enter a shift value (0-25): ")  # variable that allows the user to enter a shift value
    if user_shift_input.isdigit():  # checks if the input is a valid integer
        user_shift = int(user_shift_input)  # converts the user shift value into an integer 
        
        if 0 <= user_shift <= 26:  # shift range must be between 0 to 26
            break
        else:
            print("Please enter a value between 0 and 26.")
            
    else:
        print("Please enter a valid integer.")  # otherwise, a statement is printed 

user_text = input("Enter a text:")  # variable that allows the user to enter a text 
result = ""  # result variable originally an empty string

for char in user_text:  # for every character in user_text
    if char.isalpha():  # checks every alphabet of the letter in user_text
        startLetterIndex = 65 + 32*char.islower()
        # variable helps identify the initial index for the alphabet if it's capital or small letter.
        # 65: Uppercase letter ‘A’ ASCII value.
        # 32: It helps establish a distinction between capital versus small case.
        shifted = ((ord(char.upper()) - startLetterIndex) + user_shift) % 26 + startLetterIndex
        # shifts the character by the key and wraps around if necessary
        result += chr(shifted)  # appends the shifted character to result 
    else:
        result += char
        # Non-alphabetic characters are unchanged

print(result)  # prints the result of encrypt/decrypt user choice

# Testing

# e.g. 1 - encrypting 'hello'
# shift - 4
# result of e.g. 1 - 'fcjjm'

# e.g. 2 - encrypting 'PaPER'
# shift - 8
# result of e.g. 2 - 'XcXMZ'

# e.g. 3 - decrypting 'AMERICA is GREAT'
# shift - 20
# result of e.g. 3 - 'UGYLCWU wg ALYUN'

# e.g. 4 - decrypting 'Calling parents'
# shift - 17
# result of e.g. 4 - 'Tlwwtyr alcpyed'

# e.g. 5 - encrypting 'h = 6.62607015×10^−34 JHz−1'
# shift - 23
# result of e.g. 5 - 'y = 6.62607015×10^−34 GEq−1'

# e.g. 6 - encrypting 'G = 6.6743 × 10-11 m3 kg-1 s-2'
# shift - 42
# result of e.g. 6 - 'W = 6.6743 × 10-11 w3 uq-1 c-2'

# e.g. 7 - decrypting 'What are conjugate momenta?'
# shift - 6
# result of e.g. 7 - 'Chat are conjugate momenta?'

# e.g. 8 - decrypting 'x = r cos THETA and y = r sin THETA'
# shift - 33
# result of e.g. 8 - 'y = s dpt AOLAH boe z = s tjo AOLAH'





