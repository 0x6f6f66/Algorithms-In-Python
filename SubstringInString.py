import itertools
from collections import Counter

from typing import List

words = ["ta", "ta"]
s = "taaaaatata"

# https://davideliu.com/2021/01/26/concatenation-of-all-combinations-of-words/

# I DIDN'T WRITE THIS SOLUTION, TOOK IT FROM THE INTERNET TO UNDERSTAND THIS PROBLEM
def findSubstring(s: str, words: List[str]) -> List[int]:
    from collections import Counter
    # if s is empty or words is empty, there is nothing to do: return []
    if not s or not words:
        return []
    len_word = len(words[0])  # length of 1 word
    word_num = len(words)  # number of words
    n = len(s)  # length of input string s
    # if n < len_word, there are no matches: return []
    if n < len_word:
        return []
    # count the number of occurrences of each element in words
    words_counter = Counter(words)
    # store the result
    res = []
    # iterate over all different starting positions that generate different sequences of substrings
    # example: s="barrfooo", w=["bar", "foo"], len(w[0])=3
    # i=0: "bar", "rfo", "ooo" (r=0)
    # i=1: "arr", "foo" (r=1)
    # i=2: "rrf", "ooo" (r=2)
    # i=3: "rfo" (r=0)
    # i=4: "foo" (r=1)
    # ...
    # but we can see that the sequences defined by i=0 and i=3 differ only for the
    # first and the last element, all the other elements are common, same for i=1 and
    # i=4 and so on. Thus adjacent sequences with the same value of r=i%len(w[0]) contain
    # almost the same elements, hence they generate substrings that include similar 'words'.
    # To save time parts of the elements in 'words' that have matched can be retained.
    # We also have that r in [0,1,...,len(w[0])-1]=range(0, len_word)
    for i in range(0, len_word):
        cur_cnt = 0  # numbers of words matched in the current substring
        left = i  # left index of the current substring
        right = i  # right index of the current substring
        cur_counter = Counter()  # occurrences of words matched in the current substring
        # iterate over all words in the current sequence
        while right + len_word <= n:
            w = s[right:right + len_word]  # get a word
            right += len_word  # move the 'right' index to the next word
            # if the current word is not in 'words', the current substring can be discarded
            if w not in words_counter:
                left = right  # restart from the next word
                cur_counter.clear()  # clear the current words occurrences counter
                cur_cnt = 0  # clear the words matched counter
            else:
                cur_counter[w] += 1  # 'w' is in the current substring, increase its occurrence value by 1
                cur_cnt += 1  # 'w' is in the current substring, increase the number of words matched by 1
                # 'w' has occurred more time than its number of occurrences in 'words'
                # remove the minimum number of words from the beginning of the substring such to satisfy
                # the constraint cur_counter[w] <= words_counter[w]
                while cur_counter[w] > words_counter[w]:
                    # remove the first word of the substring (word 'left_w')
                    left_w = s[left:left + len_word]
                    left += len_word  # advance the 'left' index by the length of 1 word
                    cur_counter[left_w] -= 1  # remove 'left_w' from the occurrences counter
                    cur_cnt -= 1  # remove 1 word from the word matches counter
                # all elements in 'words' have been matched with the current substring: save its starting index
                if cur_cnt == word_num:
                    res.append(left)
    return res


if __name__ == '__main__':
    print(findSubstring(s=s, words=words))
