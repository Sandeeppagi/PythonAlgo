def binary_search_recursive(A, target):
    min = 0
    max = len(A) - 1
    return binary_search_recursive_helper(A, min, max, target)


def binary_search_recursive_helper(A, min, max, target):
    if min > max:
        return False
    else:
        mid = (min + max) // 2
        if A[mid] > target:
            return binary_search_recursive_helper(A, min, mid - 1, target)
        elif A[mid] < target:
            return binary_search_recursive_helper(A, mid + 1, max, target)
        elif A[mid] == target:
            return True

def binary_search_iterative(A, target):
    min = 0
    max = len(A) - 1
    while min > max:
        mid = (min + max) // 2
        if A[mid] == target:
            return True
        elif A[mid] > target:
            max = mid - 1
        elif A[mid] < target:
            min = mid + 1
    return False


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('-'*30)
target = 9
print(f'Array has {target} using recursion: {binary_search_recursive(A, target)}')
print(f'Array has {target} using iteration: {binary_search_recursive(A, target)}')
print('-'*30)
target = 11
print(f'Array has {target} using recursion: {binary_search_recursive(A, target)}')
print(f'Array has {target} using iteration: {binary_search_recursive(A, target)}')
