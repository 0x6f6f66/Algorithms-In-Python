MORSE_CODE = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}

key_list = list(MORSE_CODE.keys())
value_list = list(MORSE_CODE.values())


def codeMorse(string):
    result = ""
    string_up = str(string).upper()
    string_array = list(string_up)
    for s in string_array:
        # for each upper case letter in string
        # we take letter and add it as a key for MORSE_CODE dictionary
        if s != ' ':  # if the key is not a '', we add it to a string
            position_of_key = key_list.index(s)
            result += value_list[position_of_key] + " "
        else:  # if the key is space, we make a space
            result += "  "
    return result


# print(code_morse(input("Enter Letters: ")))

# value_list = list(MORSE_CODE.values())
# create a list of values, which combined with .index()
# and a value return an index position of that value
# in a dictionary. For example, if we give it value of letter "A", which is
# '.-' we receive integer 0, because it has the first position in a dictionary
# and first dict position is marked at 0.

# key_list = list(MORSE_CODE.keys())
# same with list of keys, we can get position of a letter in a dictionary
# using .index and a letter we wish to get position for.

# position = value_list.index('.-')
# for simplification purposes the integer value of the position in value_list is assigned with name 'position'
# this will give us the position of a requested value '.-' which in this case will be 0

# print(key_list[position])
# we retrieve key name for position 0 which will give us A.

# Theoretically, it is possible to write the entire code in one single line.
# print(list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index('.-')])

"""
This was the first iteration of the code, thought i would keep it in as a reflection.

def decode_morse(string):
    # 1) Take . and - as string input, compare it with dictionary value to get a key.
    # 2) Stitch keys together to a variable 'result' and output uppercase characters in a string.
    result = ''
    for s in string.split(" "):
        if s == '':
            result += " "
        else:
            result += (list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(s)])
    return result
"""


# print(decode_morse("'....' '.' '-.--' ' ' '.---' '..-' '-..' '.'"))


# string = ".... . -.--   .--- ..- -.. ."  # take a morse code string to be converted to text

# print(string_array) # take a value s for each separate morse code letter, which is a combination of symbols


def decodeMorse(string):
    result = ""
    num_of_spaces = 0
    string_array = string.split(" ")
    for s in string_array:
        if s != '':
            result += (list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(s)])
        else:
            num_of_spaces += 1
            if num_of_spaces == 2:
                result += " "
                num_of_spaces = 0
    return result


input1 = str(input("Input what you want to convert to Morse: "))
print(codeMorse(input1))
input2 = input("Input Morse to convert to text: ")
print(decodeMorse(input2))
