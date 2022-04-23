"""
1.4 pg. 91
"""


def palindrome_permutation2(s):
    countOdd = 0
    table = [0 for _ in range(0, ord('z') - ord('a') + 1)]
    for letter in s:
        x = getCharNumericValue(letter)
        if x != -1:
            table[x] += 1
            if table[x] % 2 == 1:
                countOdd += 1
            else:
                countOdd -= 1
        else:
            return "Non alpha char"
    print(table, countOdd)
    return countOdd <= 1


def getCharNumericValue(c):
    a = ord('a')
    z = ord('z')
    val = ord(c)
    if a <= val <= z:
        return val - a
    else:
        return -1


def palindrome_permutation(s):
    table = assembleTable(s)
    return checkMaxOneOdd(table)


def assembleTable(s):
    table = {}

    for let in s.lower():
        if let == ' ':
            continue

        if let not in table:
            table[let] = 0

        table[let] += 1

    return table


def checkMaxOneOdd(table):
    foundOdd = False
    for let in table:
        if table[let] % 2 == 1:
            if foundOdd:
                return False
            foundOdd = True
    return True


if __name__ == '__main__':
    print(palindrome_permutation2("aa"))
    print(palindrome_permutation2("aabbaa"))
    print(palindrome_permutation2("abc"))
    print(palindrome_permutation2("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
                                  "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
                                  "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
                                  "abcac"))




