def replace_array_v1(arr):
    if not arr:
        return []
    elif arr[0] < 0:
        arr[0] = 0
    return [arr[0]] + replace_array_v1(arr[1:])


def replace_array_v2(array, currentIndex):
    if currentIndex < len(array):
        if array[currentIndex] < 0:
            array[currentIndex] = 0
        replace_array_v2(array, currentIndex + 1)
    return


array = [1, -3, 5, 0, -10, -6, 12, 21]
index = 0
print(f"In array {array} replace negative numbers with zero {replace_array_v1(array)}")
print(f"In array {array} replace negative numbers with zero ", end="")
replace_array_v2(array, index)
print(f"{array}")
