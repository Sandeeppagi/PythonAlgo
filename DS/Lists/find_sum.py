def find_sum(lst, k):
    result = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == k:
                result.append(lst[i])
                result.append(lst[j])
                return result
    return result


def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == item:
            found = True
            index = mid
        else:
            if lst[mid] < item:
                first = mid + 1
            elif lst[mid] > item:
                last = mid - 1

    return index


def find_sum_binary_search(lst, k):
    lst.sort()
    for i in range(len(lst)):
        index = binary_search(lst, k - lst[i])
        if index != -1 and index != i:
            return [lst[i], k - lst[i]]


def find_sum_moving_index(lst, k):
    lst.sort()
    start = 0
    end = len(lst) - 1
    result = []
    while start != end:
        sum = lst[start] + lst[end]
        if sum < k:
            start += 1
        elif sum > k:
            end -= 1
        else:
            result.append(lst[start])
            result.append(lst[end])
            return result
    return result


lst = [1, 21, 3, 14, 5, 60, 7, 6]
k = 81

print(find_sum(lst, k))
print(find_sum_binary_search(lst, k))
print(find_sum_moving_index(lst, k))