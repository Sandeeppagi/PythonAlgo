def sum_of_digit(string):
    if not string:
        return 0
    return int(string[0]) + sum_of_digit(string[1:])


print(f"Sum of digit is {sum_of_digit('12345')}")
