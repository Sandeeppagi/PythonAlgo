def unbounded(arr, arr_val, arr_sum, arr_len):
    # Base condition
    if arr_len == 0 or arr_sum == 0:
        return 0

    # Choice Diagram
    if arr[arr_len - 1] <= arr_sum:
        return max(arr_val[arr_len-1] + unbounded(arr, arr_val, arr_sum-arr[arr_len-1], arr_len), unbounded(arr, arr_val, arr_sum, arr_len-1))
    else:
        return unbounded(arr, arr_val, arr_sum, arr_len-1)

arr = [1, 3, 4, 5]
arr_val = [10, 40, 50, 70]
arr_sum = 8
arr_len = len(arr)
print(unbounded(arr, arr_val, arr_sum, arr_len))
