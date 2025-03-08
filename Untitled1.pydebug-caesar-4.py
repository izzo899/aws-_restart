# Double the given alphabet
def getDoubleAlphabet(alphabet):
    return alphabet + alphabet  # ✅ No issue here

# Get a message to encrypt
def getMessage():
    return input("Please enter a message to encrypt: ")  # ✅ No issue here

# Get a cipher key (ensuring valid input)
def getCipherKey():
    while True:  # ✅ Ensures user enters a valid integer
        try:
            shiftAmount = int(input("Please enter a key (whole number from 1-25): "))
            if 1 <= shiftAmount <= 25:
                return shiftAmount  # ✅ Returns integer
            else:
                print("Invalid input! Enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()  # ✅ Converts to uppercase before encryption
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        if position != -1:  # ✅ Shift only valid alphabetic characters
            newPosition = position + cipherKey
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter  # ✅ Keeps spaces & punctuation unchanged
    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * cipherKey  # ✅ Correctly negating cipherKey
    return encryptMessage(message, decryptKey, alphabet)  # ✅ Now using decryptKey

# Main program logic
def runCaesarCipherProgram():
    print("Starting Caesar Cipher Program...")  # ✅ Debugging print

    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')

    print("About to ask for message...")  # ✅ Debugging print
    myMessage = getMessage()
    print(f'Original Message: {myMessage}')
    print(f"Message Type: {type(myMessage)}")  # ✅ Debugging print

    myCipherKey = getCipherKey()
    print(f'Cipher Key: {myCipherKey}')  # ✅ Prints the key
    print(f"Cipher Key Type: {type(myCipherKey)}")  # ✅ Debugging print

    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')

    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')  # ✅ Fixed incorrect variable

# Run the program
runCaesarCipherProgram()
