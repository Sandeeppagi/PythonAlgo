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

    def add_after(self, key, data):
        curr = self.head
        while curr:
            if curr.data == key:
                break
            curr = curr.next
        if curr is None:
            print('Key not found')
        else:
            node = Node(data)
            node.next = curr.next
            node.prev = curr
            if curr.next:
                curr.next.prev = node
            curr.next = node

    def add_before(self, key, data):
        curr = self.head
        while curr:
            if curr.data == key:
                break
            curr = curr.next
        if curr is None:
            print('Key not found')
        else:
            node = Node(data)
            node.next = curr
            node.prev = curr.prev
            if curr.prev:
                curr.prev.next = node
            curr.prev = node
            if curr == self.head:
                self.head = node


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
print('-'*30)
print('Add after the key')
mydll_2 = DoublyLinkedList()
mydll_2.append(1)
mydll_2.add_after(1, 2)
mydll_2.my_print()
print('Add before the key')
mydll_3 = DoublyLinkedList()
mydll_3.append(1)
mydll_3.append(2)
mydll_3.add_before(2, 3)
mydll_3.my_print()