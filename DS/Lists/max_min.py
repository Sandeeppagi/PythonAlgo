def max_min(lst):
    lst.sort()
    start = 0
    end = len(lst) - 1
    result = []
    while start <= end:
        if start != end:
            result.append(lst[end])
            result.append(lst[start])
        elif start == end:
            result.append(lst[start])
        start += 1
        end -= 1
    return result


def max_min_v2(lst):
    result = []
    for i in range(len(lst) // 2):
        result.append(lst[-(i + 1)])
        result.append(lst[i])
    if len(lst) % 2 == 1:
        result.append(lst[len(lst) // 2])
    return result


lst = [1, 2, 3, 4, 5]

print(f'max min list is {max_min(lst)}')
print(f'max min list is {max_min_v2(lst)}')
