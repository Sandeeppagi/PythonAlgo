def print_binary_v1(number):
    if number == 0:
        return '0'
    else:
        my_binary = print_binary_v1(number // 2)
        if number > 0:
            my_binary = my_binary + str(number % 2)
        return my_binary


def print_binary_v2(testVariable):
    if testVariable <= 1:
        return str(testVariable)
    else:
        return print_binary_v2(testVariable // 2) + print_binary_v2(testVariable % 2)


num = 11
print(f"Binary representation of {num} is {print_binary_v1(num)}")
print(f"Binary representation of {num} is {print_binary_v2(num)}")
