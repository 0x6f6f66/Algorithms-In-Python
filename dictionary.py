monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
student = {
    'age': '21',
    'name': 'Alex',
    'occupation': 'Student'
}
together = [
    student,
    monthConversions
]

monthConversions.update({'Hev': 'Hevlar'})

for _ in together:
    for key, value in _.items():
        print(key, value)

print(str(len(student)) + " " + str(len(monthConversions)))


"""
nd = {}
    for d in monthConversions:
        for k, v in d.items():
            try:
                nd[k].append(v)
            except KeyError:
                nd[k] = [v]
    # for value in monthConversions[0]:
    #    print
    #    (value)
print(nd.items())
"""

# print(monthConversions[2]['occupation'])
