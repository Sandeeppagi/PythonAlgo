arr = [2, 3, 7, 8, 10]
n = len(arr)
val = 25


def isSubsetSum_recurr(arr, val, n):
    if val == 0:
        return True
    if n == 0:
        return False

    if arr[n - 1] <= val:
        return isSubsetSum_recurr(arr, val - arr[n - 1], n - 1) or isSubsetSum_recurr(arr, val, n - 1)
    else:
        return isSubsetSum_recurr(arr, val, n - 1)


for i in range(35):
    print('Subset present for val : ', i, ' ', isSubsetSum_recurr(arr, i, n))

table_memo = [[-1 for j in range(val + 1)] for i in range(n + 1)]


# table_memo = [[-1 for j in range(val + 1)] for i in range(n + 1)]


def isSubsetSum_memo(arr, val, n):
    if val == 0:
        return True
    if n == 0:
        return False
    if table_memo[n][val] != -1:
        return table_memo[n][val]
    if arr[n - 1] <= val:
        table_memo[n][val] = isSubsetSum_memo(arr, val - arr[n - 1], n - 1) or isSubsetSum_memo(arr, val, n - 1)
        return table_memo[n][val]
    else:
        table_memo[n][val] = isSubsetSum_memo(arr, val, n - 1)
        return table_memo[n][val]


print('Subset present for val : ', val, ' ', isSubsetSum_memo(arr, val, n))


def isSubsetSum_Topdown(arr, val, n):
    table_top_down = [[0 for j in range(val + 1)] for i in range(n + 1)]
    # print(table_top_down)
    # Base condidtion
    for i in range(n + 1):
        table_top_down[i][0] = True
    for j in range(1, val + 1):
        table_top_down[0][j] = False

    # print(table_top_down)
    for i in range(1, n + 1):
        for j in range(1, val + 1):
            if arr[i-1] <= j:
                table_top_down[i][j] = table_top_down[i-1][j - arr[i-1]] or table_top_down[i-1][j]
            else:
                table_top_down[i][j] = table_top_down[i-1][j]

    return table_top_down[n][val]


# arr = [2, 3, 7, 8, 10]
# n = len(arr)
# val = 25
print('-' * 50)
for i in range(35):
    print('Subset present for val : ', i, ' ', isSubsetSum_Topdown(arr, i, n))
