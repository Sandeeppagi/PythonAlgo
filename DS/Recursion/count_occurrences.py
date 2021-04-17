def count_occurrences(arr, key):
    if not arr:
        return 0
    if arr[0] == key:
        return 1 + count_occurrences(arr[1:], key)
    else:
        return count_occurrences(arr[1:], key)


array = [1, 2, 3, 5, 1, 3, 5, 7, 1, 2, 3, 10]
val = 5

print(f"Number of occurrences for number {val} in array is {count_occurrences(array, val)}")
