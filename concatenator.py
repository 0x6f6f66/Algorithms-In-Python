# My own attempt
numlist = []
reslist = []

def square(num):
        while num > 0:
            numlist.insert(0, num % 10)
            num = (num - (num % 10)) // 10

        for i, value in enumerate(numlist):
            result = numlist[i] ** 2
            reslist.append(str(result))

        return int(''.join(x for x in reslist))
numlist.clear()
reslist.clear()

print(square(7951))


# Good example of a very efficient function:
# ' '.join(x.capitalize() for x in list)
# print(' '.join(x.capitalize() for x in str(phrase))

# Solution:
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))