def recurr_func(arr, n, s1, arr_sum):
    if n == 0:
        return abs(arr_sum - 2*s1)
    return min(recurr_func(arr, n-1, s1+arr[n-1], arr_sum), recurr_func(arr, n-1, s1, arr_sum))

def minSumDiff(arr, n):
    arr_sum = sum(arr)
    return recurr_func(arr, n, 0, arr_sum)


arr = [1, 6, 11, 5]
n = len(arr)
print(minSumDiff(arr, n))

def minSumDiff_topdown(arr):
    arr_sum = sum(arr)
    arr_len = len(arr)
    mid = arr_sum // 2
    table = [[0 for j in range(arr_sum+1)] for i in range(arr_len+1)]
    print(table)
    # Initialize table
    for i in range(arr_len+1):
        table[i][0] = 1
    for j in range(1, arr_sum+1):
        table[0][j] = 0
    print(table)
    for i in range(1, arr_len+1):
        for j in range(1, arr_sum+1):
            if arr[i-1] <= j:
                table[i][j] = table[i-1][j-arr[i-1]] or table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    last_row = []
    print(table)
    for j in range(1, mid+1):
        if table[n][j] == 1:
            last_row.append(j)
    print(last_row)
    minval = float('inf')
    for i in range(len(last_row)):
        minval = min(minval, arr_sum-2*last_row[i])
    return minval
print(minSumDiff_topdown(arr))