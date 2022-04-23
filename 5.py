lucky_numbers = [54, 14, 49, 4, 13, 56, 29, 1, 5, 0, 1, 2, 1, 1, 1, 13]
friends = ["Alexey", "Nikita", "Arina", "Julian", "Seugnchan", "Julian"]
friends2 = friends.copy()
lucky_numbers.sort()
inp = input("Enter number you wish to count: ")
a = lucky_numbers.count(int(inp))
print(a)
