def reverse_array(arr):
    if not arr:
        return []
    elif len(arr) == 1:
        return arr
    else:
        return [arr[len(arr) - 1]] + reverse_array(arr[:len(arr) - 1])


array = [4, 6, 3, 5, 7, 3, 1, 5]
print(f"Array {array} reversed is {reverse_array(array)}")
