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


arr = [1, 5, 6, 2, 4]
print(findHalf(arr))
