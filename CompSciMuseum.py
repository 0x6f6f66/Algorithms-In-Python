changeit = True
passes = 0
list_ = [5, 4, 2, 8, 6, 9, 3, 5, 7, 1]

print("List before:", list_)

while changeit == True:
    changeit = False
    passes += 1

    for i in range(len(list_) - 1):
        if list_[i] > list_[i + 1]:
            changeit = True
            list_[i], list_[i + 1] = list_[i + 1], list_[i]

print("List after:", list_, "\ntook", passes, "passes")