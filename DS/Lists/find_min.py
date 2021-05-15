def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        index_lst1 = 0
        index_lst2 = 0
        index = 0
        while index_lst1 < len(left) and index_lst2 < len(right):
            if left[index_lst1] < right[index_lst2]:
                lst[index] = left[index_lst1]
                index_lst1 += 1
            elif right[index_lst2] < left[index_lst1]:
                lst[index] = right[index_lst2]
                index_lst2 += 1
            index += 1
        while index_lst1 < len(left):
            lst[index] = left[index_lst1]
            index_lst1 += 1
            index += 1
        while index_lst2 < len(right):
            lst[index] = right[index_lst2]
            index_lst2 += 1
            index += 1


def find_minimum(lst):
    if len(lst) <= 0:
        return None
    merge_sort(lst)
    return lst[0]


print(find_minimum([9, 2, 3, 6]))
