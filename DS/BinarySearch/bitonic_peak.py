def bitonic_peak(A):
    if len(A) < 3:
        return None
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        mid_left = A[mid - 1] if mid - 1 > 0 else float('-inf')
        mid_right = A[mid + 1] if mid + 1 < len(A) else float('inf')

        if mid_left < A[mid] < mid_right:
            low = mid + 1
        elif mid_right < A[mid] < mid_left:
            high = mid - 1
        elif mid_left < A[mid] > mid_right:
            return A[mid]
    return None

# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(bitonic_peak(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(bitonic_peak(A))
A = [1, 2, 3, 4, 5]
print(bitonic_peak(A))
A = [5, 4, 3, 2, 1]
print(bitonic_peak(A))


