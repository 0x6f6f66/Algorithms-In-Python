"""
https://structy.net/problems/premium/substitute-synonyms
"""


def substitute_synonyms(sentence, synonyms):
    sentence_as_list = sentence.split(' ')
    result = _substitute_synonyms(sentence_as_list, synonyms)
    return [' '.join(sent) for sent in result]


def _substitute_synonyms(sentence, synonyms):
    if len(sentence) == 0:
        return [[]]

    first = sentence[0]
    word_combinations = get_word_combinations(first, synonyms)
    final_combinations = []
    combinations = _substitute_synonyms(sentence[1:], synonyms)
    for combination in combinations:
        for word in word_combinations:
            final_combinations.append([word, *combination])

    return final_combinations


def get_word_combinations(word, synonyms):
    if word in synonyms:
        return synonyms[word]
    else:
        return [word]


if __name__ == '__main__':
    sentence = "follow the yellow brick road"
    synonyms = {
        "follow": ["chase", "pursue"],
        "yellow": ["gold", "amber", "lemon"],
    }

    print(substitute_synonyms(sentence, synonyms))
    # [
    #   'chase the gold brick road',
    #   'chase the amber brick road',
    #   'chase the lemon brick road',
    #   'pursue the gold brick road',
    #   'pursue the amber brick road',
    #   'pursue the lemon brick road'
    # ]
