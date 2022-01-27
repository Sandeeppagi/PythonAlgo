def unbounded(arr, arr_val, weight, arr_len):
    # Base condition
    if arr_len == 0 or weight == 0:
        return 0

    # Choice Diagram
    if arr[arr_len - 1] <= weight:
        return max(arr_val[arr_len - 1] + unbounded(arr, arr_val, weight - arr[arr_len - 1], arr_len),
                   unbounded(arr, arr_val, weight, arr_len - 1))
    else:
        return unbounded(arr, arr_val, weight, arr_len - 1)


def unbounded_memo(arr, arr_val, weight, arr_len):
    table_memo = [[-1 for j in range(weight + 1)] for i in range(arr_len + 1)]
    # Base Condition
    if weight == 0 or arr_len == 0:
        return 0
    # Check value in table
    if table_memo[arr_len][weight] != -1:
        return table_memo[arr_len][weight]
    # Choice Diagram
    if arr[arr_len - 1] <= weight:
        table_memo[arr_len][weight] = max(
            arr_val[arr_len - 1] + unbounded_memo(arr, arr_val, weight - arr[arr_len - 1], arr_len),
            unbounded_memo(arr, arr_val, weight, arr_len - 1))
        return table_memo[arr_len][weight]
    else:
        table_memo[arr_len][weight] = unbounded_memo(arr, arr_val, weight, arr_len - 1)
        return table_memo[arr_len][weight]

def unbounded_topdown(arr, arr_val, weight, arr_len):
        table = [[0 for j in range(weight + 1)] for i in range(arr_len + 1)]
        for i in range(arr_len + 1):
            for j in range(weight + 1):
                if i == 0 or j == 0:
                    table[i][j] = 0
                if arr[i - 1] <= j:
                    table[i][j] = max(arr_val[i-1] + table[i][j-arr[i-1]], table[i-1][j])
                else:
                    table[i][j] = table[i-1][j]
        return table[arr_len][weight]

arr = [1, 3, 4, 5]
arr_val = [10, 40, 50, 70]
weight = 8
arr_len = len(arr)
print('unbounded', unbounded(arr, arr_val, weight, arr_len))
print('unbounded_memo', unbounded_memo(arr, arr_val, weight, arr_len))
print('unbounded_topdown', unbounded_topdown(arr, arr_val, weight, arr_len))
