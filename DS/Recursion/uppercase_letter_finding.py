def uppercase_iterative(my_str):
    for i in range(len(my_str)):
        if my_str[i].isupper():
            return my_str[i]
    return "No uppercase found"


def uppercase_recursion_v1(my_str, idx):
    if len(my_str) < 1:
        return 'String is empty'
    if idx < len(my_str):
        if my_str[idx].isupper():
            return my_str[idx]
        else:
            return uppercase_recursion_v1(my_str, idx + 1)
    else:
        return "No uppercase found"


def uppercase_recursion_v2(my_str, idx):
    if len(my_str) < 1:
        return 'String is empty'
    if my_str[idx].isupper():
        return my_str[idx]
    if idx == len(my_str) - 1:
        return "No uppercase found"
    return uppercase_recursion_v2(my_str, idx + 1)


print('-' * 30)
print('Iterative method')
print(uppercase_iterative("pythonFornow"))
print(uppercase_iterative("sandy"))

print('-' * 30)
print('Recursive method v1')
print(uppercase_recursion_v1("pythonFornow", 0))
print(uppercase_recursion_v1("sandy", 0))

print('-' * 30)
print('Recursive method v2')
print(uppercase_recursion_v2("pythonFornow", 0))
print(uppercase_recursion_v2("sandy", 0))
