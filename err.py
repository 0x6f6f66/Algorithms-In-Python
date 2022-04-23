
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as er:
    print(er)
except ValueError:
    print('Invalid input.')