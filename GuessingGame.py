
secret_word = "minecraft"
user_response = ""
terminate = "Q"
number_guesses = 0
guess_limit = 10

print()
print("Guess the hidden word.")
print("You have " + str(guess_limit) + " tries.")
print("Press Q at any time to quit.")
print()


while True:
    user_response = input("Enter your guess: ")
    print()
    if user_response != secret_word:
        print("You guessed wrong, try again.")
        number_guesses += 1
        print("You have " + str(guess_limit - number_guesses) + " tries left!")
        print()

    if user_response == terminate.lower():
        print("You quit.")
        print()
        break

    if number_guesses == guess_limit:
        print("You lost!")
        print()
        break

    if user_response == secret_word:
        print("Congratulations, you guessed the word.")
        print()
        break
