"""
1.1 pg. 90
"""
import time


def isUnique(s):
    letters = []
    for let in s:
        if let.lower() not in letters:
            letters.append(let.lower())
        else:
            return False
    return True


def isUnique2(s):
    char_set = [False for _ in range(0, 129)]
    for letter in s:
        char = ord(letter)
        if char_set[char]:
            return False
        char_set[char] = True
    return True


if __name__ == '__main__':
    for _ in range(100):
        averages1 = []
        averages2 = []
        count = 10000
        for i in range(0, count):
            start1 = time.time()
            res1 = isUnique('qwertyuiopasdfghjklzxcvbnm')
            final1 = start1 - time.time()
            #print(f"1 : {res1} | {final1}")
            averages1.append(final1)

            start2 = time.time()
            res2 = isUnique2('qwertyuiopasdfghjklzxcvbnm')
            final2 = start2 - time.time()
            #print(f"1 : {res2} | {final2}")
            averages2.append(final2)

        print(f"av1  = {sum(averages1)/count}")
        print(f"av2  = {sum(averages2)/count}")
        print("[[============================]]")


    #print(isUnique("tyaa"))
    #print(isUnique("tyAa"))
    #print(isUnique("133a"))
    #print(isUnique("A31bvca"))
