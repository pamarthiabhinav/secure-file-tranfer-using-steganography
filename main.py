import sys, argparse, termcolor, os, time, anim
from colorama import Fore, Back, Style
import encrypter as enc
import decrypter as dec
import hide_text as steg
import smtp as stp

from pathlib import Path
command_filename = Path(__file__).name

E_ALLOWED_FILES = ['.txt', '.bmp', '.jpg', '.png']
D_ALLOWED_FILES = ['.txt', '.bmp']

def show_steg_command_example():
	e = 'Example:\n\tencode: python '+ command_filename +' -o enc -s plain.txt -i image.jpg\n\tdecode: python '+ command_filename +' -o dec -s cipher.txt -i image_hidden.bmp\n'
	print(e)
	# sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument('-o','--option',
					default='dec',
                    # const='enc',
                    # nargs='?',
                    choices=['enc', 'dec'],
                    help='encrypt & decrypt The Files', required=True)
parser.add_argument('-s','--source', help='input plain/cipher text file name', required=True)
parser.add_argument('-i','--image', help='input Steganized/Non-Steganized image file name', required=True)
parser.add_argument('-e', '--example', help=show_steg_command_example())
# parser.add_argument('-e','--example', help='Get The Example Usage Command', action=example)

# parser.add_argument('-ot','--optext', help='output file name, You Want To Save The Encrypted File')
# parser.add_argument('-oi','--opimg', help='output file name, You Want To Save The Steganographed Image')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == "__main__":
	args = parser.parse_args()
	# print(args)
	source = args.source
	image = args.image
	# print(source)
	if args.option == 'enc':
		if source[-4:] in E_ALLOWED_FILES:
			anim.main()
			enc.encrypt(source)
			if image[-4:] in E_ALLOWED_FILES:
				anim.main()
				img = steg.encrypt(image, "shift.txt")
				enc.deleteFiles(['shift.txt', img])
				ans = input('Would you like to mail the secured files(Y/n): ') 
				if ans.lower() in ['yes', 'y']:
					stp.main(img.replace('.bmp', '_hidden.bmp'))
			else:
				os.system('color')
				print(termcolor.colored(f"Warning: We Encourage Only {E_ALLOWED_FILES[1:]} Files", "red"))
		else:
			os.system('color')
			h = termcolor.colored("Warning: We Encourage Only Text Files", "red")
			print(h)
	else:
		if source[-4:] in D_ALLOWED_FILES:
			if image[-4:] in D_ALLOWED_FILES:
				anim.main()
				steg.decrypt(image)
				anim.main()
				dec.decrypt(source, "shft.txt")
				enc.deleteFiles(['shft.txt'])
			else:
				os.system('color')
				print(termcolor.colored(f"Warning: We Encourage Only {D_ALLOWED_FILES[1:]} Files", "red"))
		else:
			os.system('color')
			h = termcolor.colored("Warning: We Encourage Only Text Files", "red")
			print(h)