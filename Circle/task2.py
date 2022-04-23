# doesn't work

def solution(s):
    if len(s) == 1 or s == '':
        return s

    for i in range(len(s) + 1):
        prefix = s[0:i]

        if isPalindrome(prefix):
            print(f"after cutting: {s}")
            s = s[len(prefix):i+1]

    return s


def isPalindrome(s):
    return s == s[::-1] and len(s) >= 2


if __name__ == '__main__':
    s = 'aaaaaaab'
    print(solution(s))