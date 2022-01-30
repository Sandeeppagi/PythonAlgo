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


table = [[-1]*(n+1) for i in range(n+1)]
def solve_memo(arr, i, j):
    if i >= j:
        return 0
    if table[i][j] != -1:
        return table[i][j]
    min_val = 2 ** 32
    for k in range(i, j):
        temp = solve_memo(arr, i, k) + solve_memo(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
        min_val = min(min_val, temp)
        table[i][j] = min_val
    return table[i][j]

print(solve_memo(arr, 1, n - 1))