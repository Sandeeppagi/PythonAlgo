def merge_lists(lst1, lst2):
    sorted_list = []
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    index_lst1 = 0
    index_lst2 = 0
    while index_lst1 < len(lst1) and index_lst2 < len(lst2):
        if lst1[index_lst1] < lst2[index_lst2]:
            sorted_list.append(lst1[index_lst1])
            index_lst1 += 1
        elif lst2[index_lst2] < lst1[index_lst1]:
            sorted_list.append(lst2[index_lst2])
            index_lst2 += 1
        else:
            sorted_list.append(lst2[index_lst2])
            index_lst1 += 1
            index_lst2 += 1
    while index_lst1 < len(lst1):
        sorted_list.append(lst1[index_lst1])
        index_lst1 += 1
    while index_lst2 < len(lst2):
        sorted_list.append(lst2[index_lst2])
        index_lst2 += 1
    return sorted_list


def in_place_merge(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    index_lst1 = 0
    index_lst2 = 0
    while index_lst1 < len(lst1):
        if lst1[index_lst1] > lst2[index_lst2]:
            lst1.insert(index_lst1, lst2[index_lst2])
            index_lst1 += 1
            index_lst2 += 1
        else:
            index_lst1 += 1

    if index_lst2 < len(lst2):
        lst1.extend(lst2[index_lst2:])
    return lst1


list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

print(f"Merge two sorted list {merge_lists(list1, list2)}")
print(f"Merge two sorted list {in_place_merge(list1, list2)}")
