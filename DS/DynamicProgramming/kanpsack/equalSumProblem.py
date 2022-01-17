# Using Recurssion
def equalSum(arr, sum, n):
    # Base Condition
    if sum == 0:
        return True
    if n == 0:
        return False

    # Choice Diagram
    if arr[n - 1] <= sum:
        return equalSum(arr, sum - arr[n - 1], n - 1) or equalSum(arr, sum, n - 1)
    else:
        return equalSum(arr, sum, n - 1)


def findHalf(arr):
    arr_len = len(arr)
    arr_sum = 0
    for i in range(arr_len):
        arr_sum += arr[i]
    print('Sum of arr is : ', arr_sum)
    if arr_sum % 2 == 1:
        return False
    else:
        return equalSum(arr, arr_sum // 2, arr_len)


arr = [1, 5, 6, 2, 4, 5, 7]
print(findHalf(arr))
arr_sum = sum(arr) // 2
print('Memo', arr_sum)
n = len(arr)
table_memo = [[-1 for j in range(arr_sum + 1)] for i in range(n + 1)]
# table_memo = [[-1 for j in range(val+1)] for i in range(n+1)]


def equalSumMemo(arr, sum, n):
    # Base case
    if sum == 0:
        return True
    if n == 0:
        return False

    if table_memo[n][sum] != -1:
        return arr[n][sum]

    if arr[n - 1] <= sum:
        table_memo[n][sum] = equalSumMemo(arr, sum - arr[n - 1], n - 1) or equalSum(arr, sum, n - 1)
        return table_memo[n][sum]
    else:
        table_memo[n][sum] = equalSumMemo(arr, sum, n - 1)


print(equalSumMemo(arr, arr_sum, n))


def equalSumTopDown(arr):
    arr_len = len(arr)
    arr_sum = sum(arr)

    if arr_sum % 2 != 0:
        return False
    arr_sum = arr_sum // 2

    # Create table
    table = [[0 for j in range(arr_sum + 1)] for i in range(arr_len + 1)]

    # Base condition
    for i in range(arr_len + 1):
        table[i][0] = True
    for j in range(1, arr_sum + 1):
        table[0][j] = False

    # Fill table
    for i in range(1, arr_len + 1):
        for j in range(1, arr_sum + 1):
            if arr[i - 1] <= j:
                table[i][j] = table[i - 1][j - arr[i-1]] or table[i-1][j]
            else:
                table[i][j] = table[i-1][j]

    return table[arr_len][arr_sum]


print(equalSumTopDown(arr))