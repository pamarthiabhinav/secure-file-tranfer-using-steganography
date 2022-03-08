import os, random, termcolor

def toPlain(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalnum():
            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97) 
        else:
            result += char
    return result


def decrypt(cipherFile, keyFile):
    text = b""
    with open(cipherFile, "rb") as pt:
        text = pt.read()
    text = text.decode("utf-8")

    # s = random.randint(0, 25)
    s = bytes()
    with open(keyFile, "rb") as sh:
        s = sh.read()
    s = int(s)
    # print(s)
    cipher_text = toPlain(str(text), 26-s)
    with open("plainText.txt", "wb") as pt:
        pt.write(bytes(cipher_text, encoding='utf8'))
    os.system('color')
    print(termcolor.colored('===========================================', "green"))
    print(termcolor.colored('Cipher Text Is Decrypted And Saved In "plainText.txt"', "green"))