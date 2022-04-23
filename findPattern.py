def findPattern(text, pattern):
    i = 0
    j = 0

    while True:
        if j == len(pattern):
            return i - len(pattern)

        if i == len(text):
            return -1

        tChar = text[i]
        pChar = pattern[j]

        if tChar == pChar:
            j += 1
        else:
            j = 0
        i += 1


if __name__ == '__main__':
    print(findPattern("ABABA", "BB")) # -> -1
    print(findPattern("ABBA", "BB")) # -> 1
    print(findPattern("AAAAZZZA", "ZZZ")) # -> 4
    print(findPattern("aqqqa", "qqq"))
    print(findPattern("ZZzzqwertyZZzzqwerty", "qwerty"))



    """
    A B B A
          i
    1,
    
    
    
    B B
      j
    """