string = "aeiouy"


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in string:
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter phrase you want to translate: ")))
