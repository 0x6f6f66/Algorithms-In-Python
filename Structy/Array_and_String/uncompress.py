"""
https://structy.net/problems/premium/uncompress
"""

def uncompress(s):
    i = 0
    result = []

    for j in range(len(s)):
        letter = s[j]
        if letter.isalpha():
            num = int(s[i:j])
            result.append(letter * num)  # result += letter * num | is a O(n) operation in python, use mutable list
            i = j + 1

    return ''.join(result)


if __name__ == '__main__':
    print(uncompress("1a2b3c4e"))
    print(uncompress("2c3a1t"))  # -> 'ccaaat'
    print(uncompress("4s2b"))  # -> 'ssssbb'
    print(uncompress("2p1o5p"))  # -> 'ppoppppp'
    print(uncompress("3n12e2z"))  # -> 'nnneeeeeeeeeeeezz'
    print(uncompress("127y"))  # -> 'yyyyyyyyy...'
