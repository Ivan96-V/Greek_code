

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    # Create empty string to be added when for loop goes through every letter in the input from user

    cypher_text = ''

    # Create a for loop to pass for every letter in the input from user
    for letter in original_text:
        # create variable shift_position that is the list with the alphabet in its index on every letter in the loop +
        # Shif_amount that means how many times roll index in the list
        shift_position = alphabet.index(letter) + shift_amount

        shift_position %= len(alphabet)

        # now the empty str is plus, equals in the alphabet list on the index of the shift position
        cypher_text += alphabet[shift_position]

    # print out of loop to get result after pass every single letter on the text by user
    print(cypher_text)


def decrypt(original_text, shift_amount):
    cipher_text = ''

    for letter in original_text:
        shift_position = alphabet.index(letter) - shift_amount

        shift_position = shift_position % len(alphabet)

        cipher_text += alphabet[shift_position]
    print(cipher_text)


def caesar(original_text, shift_amount, encode_or_decode):

    # Create empty str in order to letters be added after for loop runs
    results = ''

    # This if conditional means when we are running our code and want to decode an already encode word it can shift
    # backward
    if encode_or_decode == 'decode':
        shift_amount *= -1

    # For loop created it in order to the word input by user can loop on every lette and there can be added to
    # empty str
    for letter in original_text:

        # This conditional is generated in order to program can run if user use spaces, symbols or number
        # instead of words
        if letter not in alphabet:
            results += letter

        # Condition ELSE running if there is no issue with typying
        else:

            # The list with alphabet is index on the letter that is looping on the user input and this is plus
            # how many shift will move the letter
            shift_position = alphabet.index(letter) + shift_amount

            # Use module in order to if user ask to encode letter Z this loop can go back to the beginning and retrieve
            # right index letter on list
            shift_position %= len(alphabet)

            # This is the var with empty str that is added with every shift position on the alphabet list
            results += alphabet[shift_position]

    # Print outside the loop in order to all letter be added on empty str after the looping
    print(f'Here is the {encode_or_decode}d results: {results}\n')


# Create var with True conditional in order to start and ends the game
restart = True

# Starts while looping to starts or ends the program
while restart:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input('Type message you want:\n').lower()
    shift = int(input("Type the shift number:\n"))

    # run function first before any conditional to encode or decode
    caesar(text, shift, direction)

    # Create this input asking if user want to run program again or not
    ask = input("Type 'yes' if you want to got again. Otherwise, type 'no':\n").lower()

    # Create conditional in order if user want to end program
    if ask == 'no':

        # Switching var 'restart' to False in order to finish program with a goodbye message
        restart = False
        print('Thanks for using caesar program, remember here I am when you need me :)')
