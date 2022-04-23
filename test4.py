a, b, c = 0, 0, 0
nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(nums)):
    print()
    print(f"i: {i} | nums[i]: {nums[i]}")
    print(f"a: {a} | b: {b} | c: {c}")
    if nums[i] == 0:
        a += 1
        print(f"    incrementing a | a: {a}")
    if i == 0:
        c = 1
        print(f"    setting c to 1")
        b = nums[0]
        print(f"    setting b to nums[0] | nums[0]: {nums[0]}")

    else:
        if nums[i] == b:
            c += 1
            print(f"    incrementing c | c: {c}")

        elif nums[i] < b:
            b = nums[i]
            print(f"    setting b to nums[i] | nums[{i}]: {nums[i]}")
            c = 1
            print(f"    setting c to 1")

print(f"\nResult:\na: {a} | b: {b} | c: {c}")
