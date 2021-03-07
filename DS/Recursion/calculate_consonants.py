vowels = 'aeiou'

def calculate_consonant_iterative(my_str):
    count = 0
    for i in range(len(my_str)):
        if my_str[i].lower() not in vowels and my_str[i].isalpha():
            count += 1
    return count


def calculate_consonant_recursion(my_str, i, count):
    if len(my_str) > i:
        if my_str[i].lower() not in vowels and my_str[i].isalpha():
            return calculate_consonant_recursion(my_str, i + 1, count + 1)
        else:
            return calculate_consonant_recursion(my_str, i + 1, count)
    return count


def calculate_consonant_recursion_v2(my_str):
    if my_str == "":
        return 0
    if my_str[0].lower() not in vowels and my_str[0].isalpha():
        return 1 + calculate_consonant_recursion_v2(my_str[1:])
    else:
        return calculate_consonant_recursion_v2(my_str[1:])


print('-' * 30)
print('Calculate consonant: ')
my_str = 'Welcome 2 Facebook'
print(calculate_consonant_iterative(my_str))
print(calculate_consonant_recursion(my_str, 0, 0))
print(calculate_consonant_recursion_v2(my_str))
