# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_number_binary(A):
    """
    Given an array of nn distinct integers sorted in ascending order, write a function that returns a fixed point in
    the array. If there is not a fixed point, return None.
    A fixed point in an array A is an index i such that A[i]
    is equal to i. :param A: :return:
    """
    min = 0
    max = len(A) - 1

    while min <= max:
        mid = (min + max) // 2
        if A[mid] < mid:
            min = mid + 1
        elif A[mid] > mid:
            max = mid -1
        else:
            return A[mid]
    return None

# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None


# Fixed point is 3:
A1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]
print('-'*30)
print("Linear Approach")
print(f'{A1}: {find_fixed_point_linear(A1)}')
print(f'{A2}: {find_fixed_point_linear(A2)}')
print(f'{A3}: {find_fixed_point_linear(A3)}')
print('-'*30)
print("Binary Search Approach")
print(f'{A1}: {find_fixed_number_binary(A1)}')
print(f'{A2}: {find_fixed_number_binary(A2)}')
print(f'{A3}: {find_fixed_number_binary(A3)}')
