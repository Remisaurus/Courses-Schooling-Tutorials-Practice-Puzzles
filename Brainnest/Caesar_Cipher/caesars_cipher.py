class Alphabet(): # contains alphabet (all caps)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def cipher(): # will call all neccessary functions to en or decrypt a user input message.
    def en_or_de(): # function that will make the user input an e or d (for encrypt or decrypt)
        e_or_d = input('\nwould you like to encrypt(e) or decrypt(d)?')
        if e_or_d == 'e' or e_or_d == 'd':
            return e_or_d
        else:
            print('respond with just a: "e" or "d" (lower case) please.')
            en_or_de()
    def ask_for_key(): # function that will get input between 0 and 26
        key = input('\nwhat key would you like to use? (1-25)')
        try:
            if 0 < int(key) <= 25:
                return int(key)
            else:
                print('That number is out of range, input value between 1-25 please.')
                ask_for_key()
        except ValueError:
            print('please respond with a valid value between 1 and 25.')
            ask_for_key()
    def ask_for_message(): # function that asks for a message to (de)cipher. 
        print('\nnote that only alphabetical characters (a-z) will be ciphered.\nresults after ciphering will be all capital letters.')
        message = input('input the message to cipher:')
        return message
    crypted_message = en_and_de_crypt(en_or_de(), ask_for_key(), ask_for_message())
    print(f'\nthe message de/en crypted will be: {crypted_message}\n')
    return crypted_message
    
def en_and_de_crypt(e_or_d, key, message): # en-/de-crypts all alphabetical characters (a-z) in the message
    crypted_message_list = []
    message = message.upper()
    if e_or_d == 'd':
        key = key * -1
    for character in message:
        if character in Alphabet.alphabet:
            if Alphabet.alphabet.index(character) + key > 25:
                used_key = Alphabet.alphabet.index(character) + key - 26
            elif Alphabet.alphabet.index(character) + key < -26:
                used_key = Alphabet.alphabet.index(character) + key + 26
            else:
                used_key = Alphabet.alphabet.index(character) + key
            crypted_message_list.append(Alphabet.alphabet[used_key])
        else:
            crypted_message_list.append(character)
    return ''.join(crypted_message_list)

cipher() #starts a ciphering go.
        
            

        