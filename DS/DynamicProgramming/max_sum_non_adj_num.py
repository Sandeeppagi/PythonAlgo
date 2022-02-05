def maxSubsetSumNoAdjacent(array):
    arr_len = len(array)
    if arr_len == 0:
        return 0
    if arr_len == 1:
        return array[0]
    max_sum = array[:]
    print(max_sum)
    max_sum[1] = max(array[0], array[1])
    for i in range(2, arr_len):
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + array[i])
    return max_sum[-1]


arr = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(arr))
