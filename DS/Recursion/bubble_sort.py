def bubble_sort(array, length):
    if length <= 1:
        return

    bubble_sort(array, length - 1)

    last_element = array[length - 1]
    previous_index = length - 2

    while previous_index >= 0 and array[previous_index] > last_element:
        array[previous_index + 1] = array[previous_index]
        previous_index -= 1

    array[previous_index + 1] = last_element


arr = [0, 5, 4, 3, 2, 10]
print(f"Bubble sorting array {arr} produces output as {bubble_sort(arr, len(arr))}, {arr}")
