"""
https://www.codewars.com/kata/5a731b36e19d14400f000c19/train/python
"""


def decode_pass(pass_list, bits):
    binary_values = bits.split()
    result = ''
    for value in binary_values:
        int_value = int(value, 2)
        ascii_char = chr(int_value)
        result += ascii_char
    if result in pass_list:
        return result
    else:
        return False


if __name__ == '__main__':
    print(decode_pass(['password123', 'admin', 'admin1'],
                '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))
    print(decode_pass(['password321', 'admin', 'admin1'],
                '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))
    print(decode_pass(['password456', 'pass1', 'test12'],
                '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))

