class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolate_up(len(self.heap) - 1)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def __percolate_up(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.__percolate_up(parent)

    def remove_max(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__max_heapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None

    def __max_heapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.__max_heapify(largest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__max_heapify(i)

    def find_k_largest(self, my_arr, k):
        self.build_heap(my_arr)
        k_largest = [self.remove_max() for i in range(k)]
        return k_largest


heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)
heap.remove_max()
print(f"Max element in heap is : {heap.get_max()}")
my_arr = [1, 100, 20, 32, 21, 2, 6, 11]


heap.build_heap(my_arr)
print(f"Max element in heap is : {heap.get_max()}")

lst = [9, 4, 7, 1, -2, 6, 5]
k = 3

print(f"Printing the largest k elements in list : {heap.find_k_largest(lst, 3)}")