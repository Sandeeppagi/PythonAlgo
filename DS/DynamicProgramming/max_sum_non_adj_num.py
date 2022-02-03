def solve(arr):
    arr_len = len(arr)
    if arr_len == 0:
        return 0
    if arr_len == 1:
        return arr[0]
    max_sum = arr[:]
    print(max_sum)
    max_sum[1] = max(arr[0], arr[1])
    for i in range(2, arr_len):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + arr[i])
    return arr[-1]


arr = [75, 105, 120, 75, 90, 135]
print(solve(arr))
