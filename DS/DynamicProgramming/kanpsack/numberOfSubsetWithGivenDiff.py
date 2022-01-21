def no_subset_for_diff(arr, arr_len, diff):
    # Reduce it into problem which we already solve
    # condition in this problem is s1 - s2 = diff, and we know that s1 + s2 = sum(arr)
    # adding both equations -> 2*s1 = sum(arr) + diff
    # so, s1 = (sum(arr) + diff)//2
    sum_to_find = (sum(arr) + diff) // 2
    print('Sum to find is ', sum_to_find)
    table = [[0 for j in range(sum_to_find + 1)] for i in range(arr_len + 1)]
    print('Table check: ', table)

    # Initialise the table
    for i in range(arr_len + 1):
        table[i][0] = 1
    for j in range(1, sum_to_find+1):
        table[0][j] = 0
    print('Table check: ', table)

    for i in range(1, arr_len + 1):
        for j in range(1, sum_to_find + 1):
            if arr[i-1] <= j:
                table[i][j] = table[i-1][j-arr[i-1]] + table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    return table[arr_len][sum_to_find]


arr = [1, 4, 2, 7, 3]
n = len(arr)
diff = 3
print(no_subset_for_diff(arr, n, diff))
