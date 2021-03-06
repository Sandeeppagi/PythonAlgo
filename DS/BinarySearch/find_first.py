def find_first(A, target):
    """
    Writing a function that takes an array of sorted integers and a key and returns the index of the first occurrence
    of that key from the array.
    For example, for the array:

    [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    with

    target = 108

    :param A:
    :param target:
    :return:
    """
    low = 0
    high = len(A) - 1

    if len(A) == 0:
        return A[0]
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        elif A[mid] == target:
            if mid == 0:
                return 0
            elif mid > 0 and A[mid-1] == target:
                high = mid - 1
            else:
                return mid
    return None

A = [-14, -10, 108, 108, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = find_first(A, target)
print(x)
