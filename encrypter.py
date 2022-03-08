import os, random, termcolor, anim

def toCipher(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalnum():
            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97) 
        else:
            result = result + char
    return result


def encrypt(plainTextfile):
	text = b""
	try:
		with open(plainTextfile, "rb") as pt:
			text = pt.read()
		text = text.decode('utf-8')
		s = random.randint(0, 25)
		with open("shift.txt", "wb") as sh:
			sh.write(bytes(str(s), encoding='utf8'))

		cipher_text = toCipher(text, s)
		with open("cipher.txt", "wb") as ct:
			ct.write(bytes(cipher_text, encoding='utf8'))
		os.system('color')
		print(termcolor.colored("Your Text Is Encrypted to cipher.txt, Going For Steganography........", "green"))
	except Exception as e:
		os.system('color')
		print(termcolor.colored(e, "red"))


def deleteFiles(files=None):
	for f in files:
		try:
			os.remove(f)
		except Exception as e:
			pass