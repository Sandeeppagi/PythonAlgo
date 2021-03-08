s = "Was it a cat I saw?"

s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
print(s == s[::-1])


def is_palindrome(my_str):
    i = 0
    j = len(my_str) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


print('-' * 30)
print(is_palindrome(s))
