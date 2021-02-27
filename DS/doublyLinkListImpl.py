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

    def delete_node(self, key):
        curr = self.head
        while curr:
            if curr.data == key and curr == self.head:
                if curr.next is None:
                    print('Deleting the only node')
                    self.head = None
                    return
                else:
                    print('Deleting the head node')
                    curr = curr.next
                    curr.prev.next = None
                    self.head = curr
                    return
            if curr.data == key:
                if curr.next is None:
                    print('Deleting the last node')
                    curr.prev.next = None
                    curr.prev = None
                else:
                    print('Deleting the node somewhere in middle')
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr.next = None
                    curr.prev = None
            curr = curr.next

    def reverse_list(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.prev = next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur.data)
                cur = nxt

    def pairs_with_sum(self, sum_val):
        curr = self.head
        my_list = []
        str1 = ""
        while curr:
            to_find = sum_val - curr.data
            node = curr.next
            while node and node.data != to_find:
                node = node.next
            if curr and node:
                str1 = "(" + str(curr.data) + "," + str(node.data) + ")"
                my_list.append(str1)
            curr = curr.next
        return my_list

    def print_list1(self):
        cur = self.head
        while cur.next:
            cur = cur.next

        while cur:
            print(cur.data)
            cur = cur.prev
    def my_print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


print('-' * 30)
print('Append the DoublyLinkedList')
mydll = DoublyLinkedList()
mydll.append(88)
mydll.append(2)
mydll.append(3)
mydll.my_print()
print('-' * 30)
print('Prepend the DoublyLinkedList')
mydll_1 = DoublyLinkedList()
mydll_1.prepend(88)
mydll_1.prepend(2)
mydll_1.prepend(3)
mydll_1.my_print()
print('-' * 30)
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
print('-' * 30)
print('Delete the key')
mydll_4 = DoublyLinkedList()
mydll_4.append(1)
mydll_4.append(2)
mydll_4.append(3)
mydll_4.append(4)
mydll_4.append(5)
mydll_4.my_print()
mydll_4.delete_node(5)
mydll_4.my_print()
print('-' * 30)
print('Reverse the list')
mydll_5 = DoublyLinkedList()
mydll_5.append(1)
mydll_5.append(2)
mydll_5.append(3)
mydll_5.append(4)
mydll_5.append(5)
mydll_5.my_print()
mydll_5.reverse_list()
print('Reverse the list---')
mydll_5.my_print()
print('-' * 30)
print('Delete duplicates in the list')
mydll_6 = DoublyLinkedList()
mydll_6.append(1)
mydll_6.append(2)
mydll_6.append(2)
mydll_6.append(4)
mydll_6.append(5)
mydll_6.my_print()
mydll_6.remove_duplicates()
print('Delete duplicates in the list--')
mydll_6.my_print()
print('-' * 30)
print('Show sum list')
mydll_7 = DoublyLinkedList()
mydll_7.append(1)
mydll_7.append(2)
mydll_7.append(3)
mydll_7.append(4)
mydll_7.append(5)
mydll_7.my_print()
ll = mydll_7.pairs_with_sum(5)
print(ll)
mydll_7.print_list1()
