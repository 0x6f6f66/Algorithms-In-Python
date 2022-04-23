import time

def allConstruct(targetString, wordBank, memo=None):
    if memo is None:
        memo = {}

    if targetString in memo:
        return memo[targetString]

    if targetString == '':
        return [[]]

    results = []

    for word in wordBank:
        if str.find(targetString, word) == 0:
            suffix = targetString[len(word):]
            suffixWays = allConstruct(suffix, wordBank, memo)  # returns 2D array
            targetWays = list(map(lambda x: [word, *x], suffixWays))
            results.extend(targetWays)

    memo[targetString] = results
    return results


if __name__ == '__main__':
    print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    start = time.time()
    print(len(allConstruct("aaaaa", ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"])))
    print(f"end: {time.time() - start}")
