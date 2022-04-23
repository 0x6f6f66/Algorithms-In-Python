# My Solution
def multi_table(number):
    result = ""
    for multiple in range(1, 11):
        if multiple != 10:
            result += (str(multiple) + " * " + str(number) + " = " + str(multiple * number) + "\n")
        else:
            result += (str(multiple) + " * " + str(number) + " = " + str(multiple * number))
    return result


# Top Solution
def multi_table1(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))


print(multi_table1(4))






