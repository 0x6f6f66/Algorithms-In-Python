"""
Combinations of letters:
 R  C
[0][1] T
[1][1] U
[2][1] B
[3][1] A

and compare to:
 R  C
[1][0] T
[1][1] U
[1][2] B
[1][3] A

and compare to:
 R  C
[3][2] T
[2][2] U
[1][2] B
[0][2] A

and compare to:
 R  C
[2][3] T
[2][2] U
[2][1] B
[2][0] A
"""

tablet = [
# C  #0   #1   #2   #3     # R
    ['S', 'T', 'A', 'B'],  # 0
    ['T', 'U', 'B', 'A'],  # 1
    ['A', 'B', 'U', 'T'],  # 2
    ['B', 'A', 'T', 'S']   # 3

]

tablet2 = [
    # 0  # 1
    ['A', 'H'],  # 0
    ['H', 'A']  # 1

]

tablet3 = [['K', 'N', 'I', 'T'],
          ['N', 'O', 'R', 'I'],
          ['I', 'R', '0', 'N'],
          ['T', 'I', 'N', 'K']]

"""
def is_sator_square(tablet):
    if tablet[0][1] == tablet[1][0] == tablet[3][2] == tablet[2][3] and\
       tablet[1][1] == tablet[1][1] == tablet[2][2] == tablet[2][2] and\
       tablet[2][1] == tablet[1][2] == tablet[1][2] == tablet[2][1] and\
       tablet[3][1] == tablet[1][3] == tablet[0][2] == tablet[2][0]:
        return True
    else:
        return False
"""

# We print Rows


def is_sator_square(tablet):
    if tablet[0:] == list(reversed(tablet))[::-1]:
        return True
    else:
        return False


for i in range(len(tablet)):
    print(tablet3[0:][i])
    print(list(reversed(tablet3))[::-1][i])
    print("end")

