MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C',
              '-..': 'D', '.': 'E', '..-.': 'F',
              '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L',
              '--': 'M', '-.': 'N', '---': 'O',
              '.--.': 'P', '--.-': 'Q', '.-.': 'R',
              '...': 'S', '-': 'T', '..-': 'U',
              '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0',
              '.----': '1', '..---': '2', '...--': '3',
              '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9',
              '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/',
              '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=',
              '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@',
              '...---...': 'SOS'}


# take MORSE_CODE input
# convert it into words


def decode_Morse1(morse_code):
    num_of_spaces1 = 0
    result1 = ""
    for i in morse_code.split(" "):
        if i != '':
            result1 += MORSE_CODE[i]
        else:
            num_of_spaces1 += 1
            if num_of_spaces1 == 2:
                num_of_spaces1 = 0
                result1 += ' '
    return result1


# print(decode_Morse(".- .- .-   .- .- .-   -... -... -..."))

def decodeMorse2(morse_code):
    spl = morse_code.split(" ")
    is_start = False
    # is_end = False
    result = ""
    num_of_spaces = 0
    print(spl)
    for _ in spl:

        if _ == '' and is_start is False:
            result += ""
        elif _ != '':
            is_start = True
            result += MORSE_CODE[_]
        # elif num_of_spaces > 2:
        # is_end = True
        if _ == '' and is_start is True:
            # if is_end is False:
            num_of_spaces += 1
            if num_of_spaces == 2:
                num_of_spaces = 0
                result += ' '
    return result


def decodeMorse(morse_code):
    result = ""
    for word in morse_code.strip().split("   "):
        for i in word.split(' '):
            print(i)


example = ".-   .- .-"
split = example.split("   ")
for word in split:
    print("word: " + word)

    for i in word.split(" "):
        print("i: " + i)


def decodeMorseEX(morse_code):
    return ' '.join(''.join(MORSE_CODE[i] for i in word.split(' ')) for word in morse_code.strip().split("   "))



# if sample_string.find(".") == 0 or sample_string.find("-") == 0:
#    print("True")
# else:
#    print("False")

#   if sample_string[0] == ' ':
#       print('character is empty')
#   else:
#      print('character is not empty')
