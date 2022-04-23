
classes_file = open('classes.txt', "r")
#name = input('Enter your name: ')
#hero = input('Enter your class: ')

#classes_file.write("\n" + name + " " + "-" + " " + hero)
db = []
for line in classes_file.readlines():
    db.append(line)
print(db)
print(db[0].split())

splitdb = []
for i in db[0].split():
    print(i)
    splitdb.append(i)
print(splitdb)

classes_file.close()

"""
r - read
w - write
a - append at the end of the file
r+ - read and write
"""
