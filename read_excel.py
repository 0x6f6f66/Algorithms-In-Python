excel_file = open('/Users/alexgershberg/Desktop/part-00000-6cecb11b-d122-41aa-a1b1-2a7d728558be-c000.csv', "r")
for line in excel_file.readlines():
    print(line)

excel_file.close()