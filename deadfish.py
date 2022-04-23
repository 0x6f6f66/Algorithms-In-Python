"""
parse("iiisdoso")  ==>  [8, 64]

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
"""


def parse(data):
    val = 0
    result = []
    for d in data:
        if d == 'i':
            val += 1
        elif d == 'd':
            val -= 1
        elif d == 's':
            val **= 2
        elif d == 'o':
            result.append(val)
    return result


if __name__ == '__main__':
    print(parse("iiisdoso"))
