
def check_palindrome(string):

    string_lower = string.lower()
    j = len(string)-1

    for i in range(len(string_lower)):
        if string_lower[i] != string_lower[j]:
            return False
        j -= 1
    return True


print(check_palindrome("Malayalam"))
