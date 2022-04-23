def main():
    file = open("passwordCrackResult.txt", "w")
    listOfCharacters = ["","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
                        #"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        #"T", "U", "V", "W", "X", "Y", "Z",
                        #"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+", "=", "*", "&", "!", "?", "/", "[",
                        #"]", "{", "}"]

    for f in listOfCharacters:
        for g in listOfCharacters:
            for h in listOfCharacters:
                for i in listOfCharacters:
                    for j in listOfCharacters:
                        for k in listOfCharacters:
                            file.writelines(k+j+i+h+g+f+"\n")
    file.close()



if __name__ == '__main__':
    main()
