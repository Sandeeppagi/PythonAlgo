def calulate_length_iterative(my_str):
    length = 0
    for i in range(len(my_str)):
        length += 1
    return length


def calulate_length_recursion(my_str, idx, count):
    if len(my_str) > idx:
        count += 1
    else:
        return count
    return calulate_length_recursion(my_str, idx + 1, count)


def calulate_length_recursion_v2(my_str):
    if my_str == "":
        return 0
    return 1 + calulate_length_recursion_v2(my_str[1:])


print('-' * 30)
print('Calculate length of string: ')
print(f'Length of string : {calulate_length_iterative("sandy")}')
print(f'Length of string : {calulate_length_recursion("sandy", 0, 0)}')
print(f'Length of string : {calulate_length_recursion_v2("sandy")}')
