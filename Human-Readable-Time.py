"""
https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
"""

def make_readable(seconds):
    hours = 0
    minutes = 0
    seconds % 60
    return f'{seconds}'
    pass

if __name__ == '__main__':
    seconds = 1000
    print(f'00:{(seconds - seconds % 60)//60}:{seconds % 60}')