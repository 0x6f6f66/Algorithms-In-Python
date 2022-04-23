def canConstruct(targetString, wordbank, memo=None):
    if memo is None:
        memo = {}

    if targetString in memo.keys():
        return memo[targetString]

    if targetString == '':
        return True

    for word in wordbank:
        if str.find(targetString, word) == 0:
            suffix = targetString[len(word):]
            if canConstruct(suffix, wordbank, memo):
                memo[targetString] = True
                return True

    memo[targetString] = False
    return False


if __name__ == '__main__':
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
