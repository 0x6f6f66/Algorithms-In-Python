"""
MEDIUM : https://leetcode.com/problems/integer-to-roman/
"""


def intToRoman(num):
    M = ['', 'M', 'MM', 'MMM']
    C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    m = num//1000
    c = (num % 1000)//100
    x = (num % 100)//10
    i = (num % 10)

    return M[m] + C[c] + X[x] + I[i]


if __name__ == '__main__':
    print(intToRoman(2345))

