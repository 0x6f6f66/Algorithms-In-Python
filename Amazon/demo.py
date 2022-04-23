import re


regularExpression = '(^b.*b$)|(^a.*a$)|(^[ab]$)'


tests = [
    "a",
    "b",
    "ab",
    "ba",
    "aba",
    "abba",
    "aa",
    "bb",
    "baab"
]

pattern = re.compile(regularExpression)

query = int(len(tests))
result = ['False'] * query

for i in range(query):
    someString = tests[i]

    if pattern.match(someString):
        result[i] = 'True'

print("\n".join(result))