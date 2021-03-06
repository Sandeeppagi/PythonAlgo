import math

def find_number_close_to_square_root(target):
    if target == 0 or target == 1:
        return target

    square_root = int(math.sqrt(target))
    min_num = square_root * square_root
    max_num = (square_root + 1) * (square_root + 1)
    diff1 = int(target - min_num)
    diff2 = int(max_num - target)
    if diff1 > diff2:
        closest_number = int(math.sqrt(max_num))
    else:
        closest_number = int(math.sqrt(min_num))
    print(closest_number)

def integer_square_root(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

print(integer_square_root(300))
