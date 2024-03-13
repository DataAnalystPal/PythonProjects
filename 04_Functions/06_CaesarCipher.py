# Project: Caesar Cipher
# Caesar Cipher is a way of encoding text that was in practice during the times of Julius Caesar
# Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet
# Concepts Utilized: list, list index method, function, while loop, control flow

# heading when the program starts
print("This is a Caesar Cipher Program, Welcome")

# create list of alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# create caesar funtion to encrypt or decrypt the text
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# create a while loop to execute the program if user types 'yes'
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the 'shift' number: "))
    # if user enters a shift number greater than 26
    shift = shift % 26

    # call the function
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    # restart if the user presses 'yes'
    restart = input("Type 'yes' if you want to go again. Else, Type 'no: ")
    if restart == "no":
        should_end = True
        print("Goodbye")