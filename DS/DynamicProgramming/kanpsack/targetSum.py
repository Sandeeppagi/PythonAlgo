# Given a set of positive numbers (non zero) and a target sum ‘S’.
# Each number should be assigned either a ‘+’ or ‘-’ sign.
# We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

# Input: {1, 1, 2, 3}, S=1
# Output: 3
# Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

# Input: {1, 2, 7, 1}, S=9
# Output: 2
# Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}

def find_target_subsets(arr, target):
    arr_len = len(arr)
    arr_sum = sum(arr)

    # Check positive numbers only
    if any(i < 1 for i in arr):
        return -1
    if arr_sum < target or (arr_sum + target) % 2 == 1:
        return -1

    sum_to_find = (arr_sum + target) // 2
    print(sum_to_find)
    return core_logic(arr, arr_len, sum_to_find)

def core_logic(arr, arr_len, sum):
    table = [[0 for j in range(sum + 1)] for i in range(arr_len + 1)]
    for i in range(arr_len+1):
        table[i][0] = 1
    for j in range(1, sum+1):
        table[0][j] = 0

    for i in range(1, arr_len+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                table[i][j] = table[i-1][j-arr[i-1]] + table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    return table[arr_len][sum]

arr = [1, 4, 2, 7, 3]
target = 3
print(find_target_subsets(arr, target))


