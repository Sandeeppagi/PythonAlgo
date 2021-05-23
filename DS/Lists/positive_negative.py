def pos_neg(lst):
    lst.sort()
    return lst


def rearrange(lst):
    left_most_ele = 0
    for curr in range(len(lst)):
        if lst[curr] < 0:
            if lst[curr] != lst[left_most_ele]:
                lst[curr], lst[left_most_ele] = lst[left_most_ele], lst[curr]
            left_most_ele += 1
    return lst


def rearrange_v2(lst):
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


arr = [10, -1, 20, 4, 5, -9, -6]
print(f'Array of numbers {pos_neg(arr)}')
print(f'Array of numbers {rearrange(arr)}')
print(f'Array of numbers {rearrange_v2(arr)}')
