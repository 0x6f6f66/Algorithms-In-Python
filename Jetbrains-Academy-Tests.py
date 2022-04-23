"""
# Could be useful for later
a = 4
b = 400

for x in range(0, 100+1, 2):
    print("=================")
    print(f"{x}")
    print()
    print(f"{x} % {a}: {x % a}")
    print(f"{x} % {b}: {x % b}")
    print(f"{x} % {a} or {b}: {x % a or b}")
    print(f"{x} % ({a} or {b}): {x % (a or b)}")
    print(f"{x} % {a} or {x} % {b}: {x % a or x % b}")
    print(f"({x} % {a}) and ({x} % {b}): {(x % a) and (x % b)}")

    print("[]===TEST===[]")
    print(f"X: {x}")
    print("Leap") if not (x % 4 and x % 400) else print("Ordinary")
    print("=================")
    print()

print(f"{a} or {b}: {a or b}")

# print("Leap") if input % 4 or 400 or not 100 else print("Ordinary")



x = int(input())
print("Leap") if not (x % 4 or x % 400) else print("Ordinary")





for a in range (0, 100):
    b = 5
    print(f"{a} % {b} : {a % b} : {True}") if a % b else print(f"{a} % {b} : {a % b} : {False}")


"""

"""
0 is False, any other integer is True.
We have 3 statements. 

0 - FALSE
1 - TRUE
2 - TRUE
3 - TRUE

NOT 0 - TRUE
NOT 1 - FALSE
NOT 2 - FALSE
NOT 3 - FALSE
"""

"""


for x in range(0, 1000+1, 1):
    print(x)
    print(f"{x} % 4 |{x % 4}| :  True") if x % 4 else print(f"{x} % 4 |{x % 4}| :  False")
    print(f"{x} % 4 == 0 |{x % 4}| :  True") if x % 4 == 0 else print(f"{x} % 4 == 0 |{x % 4}| :  False")
    print()



Statement_1 = not 0 # DIV BY 4
Statement_2 = not 0 # DIV BY 400
Statement_3 = not 0 # DIV BY 100
print((Statement_1 and not Statement_3) or Statement_2)



for x in range(0, 1001, 1):
    Statement_1 = not x % 4 # DIV BY 4
    Statement_2 = not x % 400 # DIV BY 400
    Statement_3 = not x % 100  # DIV BY 100
    print(f"YEAR {x} : LEAP") if (Statement_1 and not Statement_3) or Statement_2 else print(f"YEAR {x} : NOT LEAP")
"""

"""
# THIS IS DONE
x = int(input())
print("Leap") if (not x % 4 and x % 100) or not x % 400 else print("Ordinary")
"""

"""
a = [1, 2, 3]
b = a
# what is the value of b? 1, 2, 3

a[1] = 10
# and here? 1, 10, 3

b[0] = 20
# what about now? 20, 10, 3

a = [5, 6]
# it is the last time, we promise. The value of b? 20, 10, 3

# Final answer: 20, 10, 3
"""

"""
sentence = "First ladies rule the State and state the rule: ladies first"
words = []

# first attempt
for word in sentence.split():
    if word[-1] == "s":
        words.append(word)
print("_".join(words))

# one liner
print("_".join(word for word in sentence.split() if word[-1] == "s"))
"""

"""
squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}

inp = int(input())
if inp in squares:
    print(squares.get(inp))
    squares.pop(inp)
else:
    print("There is no such key")
print(squares)
"""

"""
0 — 15,527: 0% tax

15,528 — 42,707: 15% tax

42,708 — 132,406: 25% tax

132,407 and more: 28% tax
"""

if __name__ == '__main__':
    name = 'Helen'
    print([name])
