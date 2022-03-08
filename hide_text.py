from PIL import Image
import os, termcolor, sys


def encrypt(image_path, text_path):
    try:
        if image_path[-4:] != '.bmp':
            img = Image.open(image_path)
            image_path = image_path[:-4] + '.bmp'
            img.save(image_path)

        with open(image_path[:-4] + '.bmp', 'rb') as bmp_file:
            bmp = bmp_file.read()

        with open(text_path, 'rb') as to_hide_file:
            msg = to_hide_file.read()

        # append the length of the message to assist with decoding
        temp = msg.decode('utf-8')
        msg = bytearray(str(len(temp)) + '\n' + temp, 'utf-8')

        # color data begins at the byte at position 10
        start_offset = bmp[10]

        bmpa = bytearray(bmp)

        # convert the msg in bytes to bits
        bits = []
        for i in range(len(msg)):
            # a byte can at max be 8 digits long, i.e. 0b11111111 = 255
            # we start at the left most bit (position 7) and work down to 0
            for j in range(7, -1, -1):
                # create the logic array of bits for our data
                bits.append(nth_bit_present(msg[i], j))

        data_array = bits

        # ensure the image is large enough to contain the text
        assert len(data_array) < len(bmpa) + start_offset

        for i in range(len(data_array)):
            bmpa[i + start_offset] = set_final_bit(bmpa[i + start_offset],
                                                   data_array[i])

        with open(image_path.replace('.bmp', '_hidden.bmp'), 'wb') as out:
            out.write(bmpa)
        os.system('color')
        print(termcolor.colored('Cover image with secret message saved as original filename'
              ' with "_hidden.bmp" appended', "green"))

        return image_path
    except Exception as e:
        os.system('color')
        print(termcolor.colored(e, "red"))
        sys.exit()


def decrypt(image_path):
    try:
        with open(image_path, 'rb') as bmp_file:
            bmp = bmp_file.read()

        # color data begins at the byte at position 10
        start_offset = bmp[10]

        # deconstruct each byte and get its final bit
        bits = []
        for i in range(start_offset, len(bmp)):
            bits.append(nth_bit_present(bmp[i], 0))

        # combine our bit array into bytes
        out_bytes = []
        for i in range(0, len(bits), 8):
            if(len(bits) - i > 8):
                out_bytes.append(bits_to_byte(bits[i: i + 8]))

        # convert bytes to characters
        out = []
        for b in out_bytes:
            out.append(chr(b))

        output = ''.join(out)

        # strip out the first line containing the length of the message
        idx = output.find('\n')
        msg_len = int(output[:idx])

        # ignore data after the message is complete
        msg = output[idx + 1: idx + msg_len + 1]

        with open("shft.txt", "w") as text_file:
            text_file.write(msg)
        os.system('color')
        # print(termcolor.colored('Hidden message:', "green"))
        # print(termcolor.colored(msg,  "green"))
        print(termcolor.colored('Text Retrieved Form The Image To shft.txt"', "green"))
    except Exception as e:
        os.system('color')
        print(termcolor.colored(e, "red"))
        sys.exit()


def nth_bit_present(my_byte, n):
    return (my_byte & (1 << n)) != 0


def set_final_bit(my_byte, ends_in_one):
    new_byte = 0
    if ends_in_one:
        if(nth_bit_present(my_byte, 0)):
            new_byte = my_byte
        else:
            new_byte = my_byte + 1
    else:
        if(nth_bit_present(my_byte, 0)):
            new_byte = my_byte - 1
        else:
            new_byte = my_byte
    return new_byte


def bits_to_byte(bits):
    assert len(bits) == 8
    new_byte = 0
    for i in range(8):
        if bits[i]:
            new_byte |= 1 << 7 - i
        else:
            new_byte |= 0 << 7 - i
    return new_byte