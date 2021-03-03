def array_advance(A):
    """
    Is it possible to advance from the start of the array to the last element given that the maximum you can advance
    from a position is based on the value of the array at the index you are currently present on?
    :param A:
    :return:
    """
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached < last_idx:
        print(i, furthest_reached, A[i] + i)
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx


A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))
