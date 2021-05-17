def non_repeating(lst):
    for i in range(len(lst)):
        key = 1
        while key < len(lst):
            if i != key and lst[key] == lst[i]:
                break
            key += 1
        if key == len(lst):
            return lst[i]


my_list = [1, 2, 3, 4, 1]

print(non_repeating(my_list))
