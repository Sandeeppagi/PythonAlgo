def solve(arr, i, j):
    if i >= j:
        return 0
    min_val = 2 ** 32
    for k in range(i, j):
        temp = solve(arr, i, k) + solve(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        if temp < min_val:
            min_val = temp
    return min_val


arr = [40, 20, 30, 10, 30]
n = len(arr)
print(solve(arr, 1, n - 1))
