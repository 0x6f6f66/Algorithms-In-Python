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

print()
print(monthConversions.get("Hev", "Not a valid Key"))
