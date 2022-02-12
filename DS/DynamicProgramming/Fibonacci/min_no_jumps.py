def min_no_jumps(arr):
    n = len(arr)
    jumps = [float("inf") for i in arr]
    jumps[0] = 0
    for i in range(1, n):
        for j in range(0, i):
            # Can we jump 'x' number of steps? calculate the no of steps to jump from current index to next index
            # i.e. i - j, Then Check the number of steps available to jump at index j i.e. arr[j]
            if arr[j] >= i - j:
                # Find minimum jumps at each index, it takes one jump from index to index i
                # We know we can jump as we are in the if loop. So number jumps would jump[j] + 1
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[-1]


print(min_no_jumps([2, 1, 1, 1, 4]))
print(min_no_jumps([0, 1, 1, 1, 4]))
