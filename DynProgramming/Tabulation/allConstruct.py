def allConstruct(target, wordBank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        if table[i]:
            for word in wordBank:
                if target[i: i + len(word)] == word:
                    for tbl in table[i]:
                        table[i + len(word)].append([*tbl, word])

    return table[-1]


if __name__ == '__main__':
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(allConstruct("aaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))
    print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
