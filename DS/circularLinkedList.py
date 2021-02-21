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

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break

        print(f'Length of the circular linklist is {count}')
        return count

    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        print(mid, size)

        curr = self.head
        tail_list_1 = None
        head_list_2 = None
        tail_list_2 = None
        count = 0
        while curr:
            count += 1
            if count == mid:
                tail_list_1 = curr
                head_list_2 = curr.next
            if curr.next == self.head:
                tail_list_2 = curr
                break
            curr = curr.next
        print(self.head.data, tail_list_1.data, head_list_2.data, tail_list_2.data)
        tail_list_1.next = self.head
        tail_list_2.next = None
        list2 = CircularLinkedList()
        curr = head_list_2
        while curr:
            list2.append(curr.data)
            if curr.next is None:
                head_list_2.next = list2.head
                break
            curr = curr.next
        print(self.print_list(), list2.print_list())


mylist = CircularLinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.prepend(0)
mylist.print_list()
print('-' * 30)
mylist.print_list()
mylist.remove_item(1)
mylist.print_list()
print('-' * 30)
size = CircularLinkedList()
size.append(99)
size.append(991)
size.__len__()
mylist.append(99)
mylist.append(9)
mylist.print_list()
mylist.split_list()
