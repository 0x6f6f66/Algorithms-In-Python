def countConstruct(target, wordBank):
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    for i in range(len(target) + 1):
        if table[i]:
            for word in wordBank:
                if target[i: i + len(word)] == word:
                    table[i + len(word)] += table[i]

    return table[-1]


if __name__ == '__main__':
    print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))