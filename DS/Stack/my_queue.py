class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            if type(self.items[-1]) is not int:
                return self.items[-1].data
            else:
                return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def __str__(self):
        if not self.is_empty():
            if type(self.items[0]) is not int:
                for i in self.items:
                    print(i.data, end="")
                print()
            else:
                print(self.items)

# print('-'*30)
# print('Adding to Queue')
# q = Queue();
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.__str__()
# print('-'*30)
# print('Remove item from Queue')
# q.__str__()
# q.dequeue()
# q.__str__()
# q.dequeue()
# q.__str__()
# print('-'*30)
# print('Size of Queue')
# size = q.size()
# print(size)
# print('-'*30)
# print('Peek of Queue')
# q.__str__()
# peek = q.peek()
# print(peek)
