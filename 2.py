list_of_numbers = []

print()
print('Hint: input "Q" to quit.')


def input_loop():
    _run = True
    while _run:
        initial_user_input = input('Type number you want to add: ')

        if initial_user_input.isnumeric():
            list_of_numbers.append(int(initial_user_input))
            print(list_of_numbers)

        elif initial_user_input.lower() == 'q':
            print()
            print('Exited')
            break
        else:
            while _run:
                initial_user_input_in_loop = input('Error, incorrect input. Must be a number: ')

                if initial_user_input_in_loop.isnumeric():
                    list_of_numbers.append(int(initial_user_input_in_loop))
                    print(list_of_numbers)
                    break

                elif initial_user_input_in_loop.lower() == 'q':
                    print()
                    print("Exited")
                    _run = False
                    break


input_loop()
