# For some reason capitalizes only first word, even though i'm splitting it into phrases.

# Fix

# Apparently, spaces are non-alphabetic characters, therefore we have to specify '. ' with a space
# for it to cut it in the right place, and have an alphabetic character as a first letter of a string.

string = "hello. good's to have you here. hi."
print('. '.join(x.capitalize() for x in string.split('. ')))
