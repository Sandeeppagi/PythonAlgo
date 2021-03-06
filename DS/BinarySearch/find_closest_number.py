def find_closest_number(A, target):
    size = len(A)
    if size == 0:
        print('Array is empty')
        return None
    if size == 1:
        return A[0]

    low = 0
    high = size - 1
    min_diff = float("inf")
    closest_number = None

    while low <= high:
        mid = (low + high) // 2

        if mid + 1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid -1] - target)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_number = A[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_number = A[mid + 1]

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            return A[mid]

    return closest_number


A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]
A3 = [2, 4, 6, 7, 8, 8, 9]
print('-'*30)
print('Closest number search')
print(f'Find the closest number to 11 in array {A1}: {find_closest_number(A1, 11)}')
print(f'Find the closest number to 4 in array {A2}: {find_closest_number(A2, 4)}')
print(f'Find the closest number to 5 in array {A3}: {find_closest_number(A3, 5)}')
