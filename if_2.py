def max_num(a, b, c):
    if a > b:
        return a
    if b > c:
        return b
    if c > a:
        return c


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
print("Biggest number is: " + str(max_num(a, b, c)))
