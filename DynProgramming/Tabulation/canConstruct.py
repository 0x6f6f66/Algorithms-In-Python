def canConstruct(target, wordBank):
    table = [False for _ in range(len(target) + 1)]
    table[0] = True

    for i in range(len(table)):
        if table[i]:
            for word in wordBank:
                if target[i: i + len(word)] == word:
                    table[i + len(word)] = True

    return table[-1]


if __name__ == '__main__':
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
