import sys

ciphertext = sys.argv[2].upper()
keytext = sys.argv[3].upper()

def vigenere(text, key, encode):
    alphabet = list(map(chr, range(65, 91)))
    new = ""
    for i in range(0, len(text)):
        mychar = text[i]
        shift = alphabet.index(key[i % len(key)])
        if encode != True : shift *= -1
        newindex = (alphabet.index(mychar) + shift) % 26
        new = new + alphabet[newindex]
    print(new)

if sys.argv[1] == "encode":
    vigenere(ciphertext, keytext, True)
if sys.argv[1] == "decode":
    vigenere(ciphertext, keytext, True)
