def palindrome(string):
    if len(string) <= 1:
        return True
    length = len(string)
    if string[0] == string[length - 1]:
        return palindrome(string[1:length - 1])
    return False


print(palindrome('maddam'))
