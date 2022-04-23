
pal1 = "HALAH"
pal2 = "ANOTHER ONE BITES THE DUST TSUD EHT SETIB ENO REHTONA"
pal3 = "123456789987654321"
pal4 = "12341234"
test = "121"

list_of_palindromes = [pal1, pal2, pal3, pal4]


#My Solution
def isPalindrome(palindrome):
    if len(palindrome) != 1 & 0:
        if palindrome[0] == palindrome[-1]:
            return isPalindrome(palindrome[1:-1])
        else:
            return False
    return True


#My solution after Vova's tip to use [::-1]
def isPalindrome2(palindrome):
    return palindrome == palindrome[::-1] and len(palindrome) > 2


print(isPalindrome2(test))
