# Stack Overflow
def binary_gap(N):
    return len(max(format(N, 'b').strip('0').split('1')))


if __name__ == '__main__':
    number = 257
    formatted = format(number, 'b')
    print(len(max(formatted.strip("0").split("1"))))


