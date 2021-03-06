def find_index_cyclic_shift(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid

    return low


A = [1, 2, 3, 4, 5, 6, 7]
B = [2, 3, 4, 5, 6, 7, 1]
C = [3, 4, 5, 6, 7, 1, 2]
D = [4, 5, 6, 7, 1, 2, 3]
E = [5, 6, 7, 1, 2, 3, 4]
F = [6, 7, 1, 2, 3, 4, 5]
G = [7, 1, 2, 3, 4, 5, 6]
H = [2, 1]

print(find_index_cyclic_shift(A))
print(find_index_cyclic_shift(B))
print(find_index_cyclic_shift(C))
print(find_index_cyclic_shift(D))
print(find_index_cyclic_shift(E))
print(find_index_cyclic_shift(F))
print(find_index_cyclic_shift(G))
print(find_index_cyclic_shift(H))


