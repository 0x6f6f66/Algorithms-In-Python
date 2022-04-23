def countConstruct(targetString, wordBank, memo=None):
    if memo is None:
        memo = {}

    if targetString in memo:
        return memo[targetString]

    if targetString == '':
        return 1

    totalCount = 0

    for word in wordBank:
        if str.find(targetString, word) == 0:
            suffix = targetString[len(word):]
            numWaysForRest = countConstruct(suffix, wordBank, memo)
            totalCount += numWaysForRest

    memo[targetString] = totalCount
    return totalCount


if __name__ == '__main__':
    print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "f"]))
