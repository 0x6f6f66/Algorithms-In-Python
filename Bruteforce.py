import itertools
import time
import datetime

password = input("Enter password: ")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
#chars = "01"
#chars = "0123456789"

p_length = 1
result = ''
iterations = 0
begin = time.time()
while result != password:

    charset = []

    for i in range(p_length):
        charset.append(chars)

    gen = itertools.product(*charset)
    result = ' '

    while result:
        try:
            result = ''.join(next(gen))
            iterations += 1
            if result == password:
                end = time.time()
                print(f"FOUND PASSWORD: {result}")
                print(f"Iterations: {iterations}")
                print(f"Time took: {datetime.timedelta(seconds=(end - begin))}")
                break
        except:
            break

        print(result)

    p_length += 1
