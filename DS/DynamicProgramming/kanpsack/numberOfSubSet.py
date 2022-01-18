def numberOfSubset(arr, sum, n):
    # Base Case
    if sum == 0:
        return 1
    if n == 0:
        return 0

    # Choice Diagram
    if arr[n - 1] <= sum:
        return numberOfSubset(arr, sum - arr[n - 1], n - 1) + numberOfSubset(arr, sum, n - 1)
    else:
        return numberOfSubset(arr, sum, n - 1)


arr = [2, 3, 7, 8, 10]
n = len(arr)
sum = 10
print(numberOfSubset(arr, sum, n))

table_memo = [[-1 for j in range(sum + 1)] for i in range(n + 1)]


def numberOfSubset_memo(arr, sum, n):
    # Base condition
    if sum == 0:
        return 1
    if n == 0:
        return 0
    if table_memo[n][sum] != -1:
        return table_memo[n][sum]

    if arr[n - 1] <= sum:
        table_memo[n][sum] = numberOfSubset_memo(arr, sum - arr[n - 1], n - 1) + numberOfSubset_memo(arr, sum, n - 1)
        return table_memo[n][sum]
    else:
        table_memo[n][sum] = numberOfSubset_memo(arr, sum, n - 1)
        return table_memo[n][sum]
    return table_memo[n][sum]


print(numberOfSubset_memo(arr, sum, n))


def numberOfSubset_topdown(arr, sum, n):
    table = [[0 for j in range(sum + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        table[i][0] = 1
    for j in range(1, sum + 1):
        table[0][j] = 0
    print(table)

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                table[i][j] = table[i - 1][j - arr[i - 1]] + table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j]
    return table[n][sum]


print(numberOfSubset_topdown(arr, 10, n))
