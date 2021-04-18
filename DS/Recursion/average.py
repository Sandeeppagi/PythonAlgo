def average_numbers_v1(array, current_index):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    if current_index < len(array):
        result = array[current_index] + average_numbers_v1(array, current_index + 1)
        divisor = len(array) - current_index
        if divisor == len(array):
            return result / divisor
        return result
    else:
        return 0


def average_numbers_v2(array, current_index=0):
    # Base Case
    if current_index == len(array) - 1:
        return array[current_index]

    # Recursive case1
    # When currentIndex is 0, divide sum computed so far by len(testVariable).
    if current_index == 0:
        return (array[current_index] + average_numbers_v2(array, current_index + 1)) / len(array)

    # Recursive case2
    # Compute sum
    return array[current_index] + average_numbers_v2(array, current_index + 1)


arr = [2, 2, 2, 2, 2, 10]
index = 0

print(average_numbers_v1(arr, index))
print(average_numbers_v2(arr, index))
