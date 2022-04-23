"""
https://structy.net/problems/premium/lexical-order
"""


# My Solution using helper function
def lexical_order1(word_1, word_2, alphabet):
    p1 = 0
    p2 = 0
    while p1 != len(word_1):
        if p2 == len(word_2):
            return False

        letter_1 = word_1[p1]
        letter_2 = word_2[p2]
        result = compare_letters(letter_1, letter_2, alphabet)
        if result == True:
            return True
        elif result == False:
            return False

        p1 += 1
        p2 += 1

    return True


def compare_letters(l1, l2, alphabet):
    l1_index = alphabet.index(l1)
    l2_index = alphabet.index(l2)

    if l1_index == l2_index:
        return None

    if l1_index < l2_index:
        return True

    if l2_index < l1_index:
        return False


# Structy Solution
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


"""
if first word is earlier, return True
if second word is earlier, return False


apple
^
dock
^


a vs d
"""


if __name__ == '__main__':
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(lexical_order("backs", "backdoor", alphabet))  # -> False

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(lexical_order("apple", "dock", alphabet))  # -> True

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(lexical_order("apple", "ample", alphabet))  # -> False

    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(lexical_order("zoo", "dinner", alphabet))  # -> True

    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(lexical_order("leaper", "leap", alphabet))  # -> False

