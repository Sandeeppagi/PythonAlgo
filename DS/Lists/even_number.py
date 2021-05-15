def remove_even(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result


def remove_even_v2(lst):
    return [number for number in lst if number % 2 != 0]


my_list = [1, 2, 4, 5, 10, 6, 3]

print(f"Odd number in the list are {remove_even(my_list)}")
print(f"Odd number in the list are {remove_even_v2(my_list)}")
