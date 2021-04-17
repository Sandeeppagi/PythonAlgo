def str_len(string):
    if not string:
        return 0
    return 1 + str_len(string[1:])


print(f"Length of string is {str_len('Sandy1234')}")
