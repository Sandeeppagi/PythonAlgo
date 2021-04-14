def first_index(arr, testVariable, currentIndex):
    if currentIndex < len(arr):
        if arr[currentIndex] == testVariable:
            return currentIndex
    else:
        return -1
    return first_index(arr, testVariable, currentIndex + 1)


arr = [2, 4, 1, 6, 3, 9]
num = 11
print(f"Index of number {num} is at {first_index(arr, num, 0)}")
