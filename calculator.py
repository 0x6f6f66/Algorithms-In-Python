num1 = float(input("Enter your first number: "))
operator = (input("Enter operator: "))
num2 = float(input("Enter your second number: "))


def calculator(num1, op, num2):
    if op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    else:
        return "Wrong Operator"


print()
print(calculator(num1, operator, num2))
print()
