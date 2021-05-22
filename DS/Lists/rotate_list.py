def right_rotate(lst, k):
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    print(lst[-3:])
    print(lst[:-3])
    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], abs(3)))
