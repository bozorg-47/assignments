def is_palindrome(palindrome):
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False
print(is_palindrome("radar"))
print(is_palindrome("python"))

