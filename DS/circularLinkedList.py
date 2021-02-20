class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        if not self.head:
            return print('Circular list is empty')
        else:
            curr = self.head
            while curr:
                print(f"{curr.data} -> ", end="")
                curr = curr.next
                if curr == self.head:
                    break


mylist = CircularLinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.prepend(0)
mylist.print_list()
