def function():
    n = input("Input number: ")
    if not n.isnumeric():
        print("Invalid input, input must be a single whole number.")
    else:
        for i in range(int(n)):
            print(i+1)


function()
