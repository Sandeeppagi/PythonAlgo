class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
            node.prev = None
            return
        if self.head is not None:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(data)
            curr.next.prev = curr

    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
            node.prev = None
            return
        if self.head is not None:
            curr = self.head
            curr.prev = node
            node.next = curr
            node.prev = None
            self.head = node
            return

    def my_print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

print('-'*30)
print('Append the DoublyLinkedList')
mydll = DoublyLinkedList()
mydll.append(88)
mydll.append(2)
mydll.append(3)
mydll.my_print()
print('-'*30)
print('Prepend the DoublyLinkedList')
mydll_1 = DoublyLinkedList()
mydll_1.prepend(88)
mydll_1.prepend(2)
mydll_1.prepend(3)
mydll_1.my_print()
