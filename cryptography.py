import random

values = [
    'a', 'b', 'c',
    'd', 'e', 'f',
    'g', 'h', 'i',
    'j', 'k', 'l',
    'm', 'n', 'o',
    'p', 'q', 'r',
    's', 't', 'u',
    'v', 'w', 'x',
    'y', 'z', '0',
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '!', '?', '/'
]

key = "oof"

for i in range(100):
    key = key + random.choice(values)

print(key)