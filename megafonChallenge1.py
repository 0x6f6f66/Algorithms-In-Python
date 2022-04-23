"""
a = 1
b = 1
c = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'UP-LEFT', 'UP-RIGHT']
for i in range(15):
    a, b = b, a + b
    print(b, c[i % 6])
"""



l = {646: 4, 1045: 4, 1691: 3, 152: 3, 246: 3, 398: 3}
for i in l:
    print(i%l[i])
