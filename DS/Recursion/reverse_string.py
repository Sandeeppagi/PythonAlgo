def reverse_string_iterative(string):
    reverse = ''
    length = len(string) - 1
    while length >= 0:
        reverse += string[length]
        length -= 1
    return reverse


def reverse_string_recursive(string):
    if len(string) == 0:
        return string
    return reverse_string_recursive(string[1:]) + string[0]


print(reverse_string_iterative('Sandy'))
print(reverse_string_recursive('Sandy'))
