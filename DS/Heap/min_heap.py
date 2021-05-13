class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolate_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def __percolate_up(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.__percolate_up(parent)

    def __min_heapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        min = index
        if len(self.heap) > left and self.heap[min] > self.heap[left]:
            min = left
        if len(self.heap) > right and self.heap[min] > self.heap[right]:
            min = right
        if min != index:
            self.heap[min], self.heap[index] = self.heap[index], self.heap[min]
            self.__min_heapify(min)

    def remove_min(self):
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__min_heapify(0)
            return min
        elif len(self.heap) == 1:
            min = self.heap[0]
            del self.heap[0]
            return min
        else:
            return None

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(self.heap) - 1, -1, -1):
            self.__percolate_up(i)


heap = MinHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.get_min())
print(heap.remove_min())
print(heap.get_min())
heap.insert(-100)
print(heap.get_min())
