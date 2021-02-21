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
                    print()
                    break

    def remove_item(self, data):
        if not self.head:
            print('List is empty')
        else:
            curr = self.head
            to_remove_node = None
            previous_node = None
            while curr:
                if curr.data == data:
                    to_remove_node = curr
                if curr.next.data == data:
                    previous_node = curr
                if curr.next == self.head:
                    break
                curr = curr.next
            print(previous_node.data, to_remove_node.data)

            if to_remove_node == self.head:
                self.head = to_remove_node.next

            previous_node.next = to_remove_node.next
            to_remove_node.next = None


mylist = CircularLinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.prepend(0)
mylist.print_list()
print('-'*30)
mylist.print_list()
mylist.remove_item(1)
mylist.print_list()
