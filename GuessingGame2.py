secret_word = "minecraft"
user_response = ""
terminate = "Q"
number_guesses = 0
guess_limit = 10
out_of_guesses = False

print()
print("Guess the hidden word.")
print("You have " + str(guess_limit) + " tries.")
print("Press Q at any time to quit.")
print()


while user_response != secret_word and not out_of_guesses:
    user_response = input("Enter your guess: ")
    if number_guesses < guess_limit and not user_response == terminate.lower():
        print()
        print("You guessed wrong, try again.")
        number_guesses += 1
        print("You have " + str(guess_limit - number_guesses) + " tries left!")
        print()

    if user_response == terminate.lower():
        print()
        print("You quit.")
        print()
        break

    else:
        out_of_guesses = True


if out_of_guesses and not user_response == terminate.lower():
    print("You lost!")
    print()

elif user_response == secret_word:
    print()
    print("Congratulations, you guessed the word.")
    print()