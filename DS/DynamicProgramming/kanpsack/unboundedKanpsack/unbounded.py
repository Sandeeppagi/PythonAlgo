def unbounded(arr, arr_val, arr_sum, arr_len):
    # Base condition
    if arr_len == 0 or arr_sum == 0:
        return 0

    # Choice Diagram
    if arr[arr_len - 1] <= arr_sum:
        return max(arr_val[arr_len - 1] + unbounded(arr, arr_val, arr_sum - arr[arr_len - 1], arr_len),
                   unbounded(arr, arr_val, arr_sum, arr_len - 1))
    else:
        return unbounded(arr, arr_val, arr_sum, arr_len - 1)


def unbounded_memo(arr, arr_val, arr_sum, arr_len):
    table_memo = [[-1 for j in range(arr_sum + 1)] for i in range(arr_len + 1)]
    # Base Condition
    if arr_sum == 0 or arr_len == 0:
        return 0
    # Check value in table
    if table_memo[arr_len][arr_sum] != -1:
        return table_memo[arr_len][arr_sum]
    # Choice Diagram
    if arr[arr_len - 1] <= arr_sum:
        table_memo[arr_len][arr_sum] = max(
            arr_val[arr_len - 1] + unbounded_memo(arr, arr_val, arr_sum - arr[arr_len - 1], arr_len),
            unbounded_memo(arr, arr_val, arr_sum, arr_len - 1))
        return table_memo[arr_len][arr_sum]
    else:
        table_memo[arr_len][arr_sum] = unbounded_memo(arr, arr_val, arr_sum, arr_len - 1)
        return table_memo[arr_len][arr_sum]


arr = [1, 3, 4, 5]
arr_val = [10, 40, 50, 70]
arr_sum = 8
arr_len = len(arr)
print('unbounded', unbounded(arr, arr_val, arr_sum, arr_len))
print('unbounded_memo', unbounded_memo(arr, arr_val, arr_sum, arr_len))
