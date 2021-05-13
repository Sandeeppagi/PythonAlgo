def min_heap(heap, index):
    left = (index * 2) + 1
    right = (index * 2) + 2
    min = index
    if len(heap) > left and heap[min] > heap[left]:
        min = left
    if len(heap) > right and heap[min] > heap[right]:
        min = right
    if min != index:
        heap[min], heap[index] = heap[index], heap[min]
        return min_heap(heap, min)
    return heap


def covert_to_min_heap(heap):
    for i in range((len(heap)) // 2, -1, -1):
        min_heap_arr = min_heap(heap, i)
    return min_heap_arr


maxHeap = [9, 4, 7, 1, -2, 6, 5]
print(covert_to_min_heap(maxHeap))
