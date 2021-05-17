def find_second_maximum_v1(lst):
    lst.sort()
    if len(lst) >= 2:
        return lst[-2]


def find_second_maximum_v2(lst):
    first_max = second_max = float('-inf')
    for i in range(len(lst)):
        if first_max < lst[i]:
            first_max = lst[i]
    for i in range(len(lst)):
        if lst[i] != first_max and second_max < lst[i]:
            second_max = lst[i]
    return second_max


def find_second_maximum_v3(lst):
    first_max = second_max = float('-inf')
    for i in range(len(lst)):
        if first_max < lst[i]:
            second_max = first_max
            first_max = lst[i]
        elif second_max < lst[i] != first_max:
            second_max = lst[i]
    if second_max == float('-inf'):
        return 'No second max'
    else:
        return second_max


print(find_second_maximum_v1([9, 1, 2, 0]))
print(find_second_maximum_v2([9, 1, 2, 0]))
print(find_second_maximum_v3([9, 1, 2, 0]))
