num1 = 1.1
num2 = 3.0

print(str(type(num1)) + " " + str(type(num2)))

if isinstance(num1, (int, float)) and isinstance(num2, (int,float)):

    print("Done")
else:
    print("Error")