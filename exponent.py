def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

print(raise_to_power(input1, input2))
print(input1 ** input2)
