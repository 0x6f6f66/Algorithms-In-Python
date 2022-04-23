"""
https://structy.net/problems/premium/detect-dictionary
"""


def detect_dictionary(dictionary, alphabet):
    for i in range(0, len(dictionary) - 1):
        word = dictionary[i]
        next_word = dictionary[i + 1]
        if lexical_order(word, next_word, alphabet) == False:
            return False
    return True


def lexical_order(word_1, word_2, alphabet):
    max_length = max(len(word_1), len(word_2))
    for i in range(0, max_length):
        value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf')
        value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')
        if value_1 < value_2:
            return True
        if value_2 < value_1:
            return False
    return True


if __name__ == '__main__':
    dictionary = ["zoo", "tick", "tack", "door"]
    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(detect_dictionary(dictionary, alphabet))  # -> True

    dictionary = ["zoo", "tack", "tick", "door"]
    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(detect_dictionary(dictionary, alphabet)) # -> False

    dictionary = ["zoos", "zoo", "tick", "tack", "door"]
    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(detect_dictionary(dictionary, alphabet)) # -> False

    dictionary = ["miles", "milestone", "proper", "process", "goal"]
    alphabet = "mnoijpqrshkltabcdefguvwzxy"
    print(detect_dictionary(dictionary, alphabet))  # -> True



