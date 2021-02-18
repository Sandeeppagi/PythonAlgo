class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_node(self, previous_node, data):
        if not self.is_empty():
            current_node = self.head
            while current_node is not None:
                if previous_node == current_node.data:
                    new_node = Node(data)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    break
                current_node = current_node.next
            print('Node not present')

    def delete_node(self, to_delete):
        if not self.is_empty():
            current_node = self.head
            if to_delete == current_node.data:
                self.head = current_node.next
                current_node = None
                return
            prev = None
            while current_node and current_node.data != to_delete:
                prev = current_node
                current_node = current_node.next

            if current_node is None:
                print('data not found')
                return
            prev.next = current_node.next
            current_node = None
        else:
            print('List is empty')

    def delete_node_position(self, position):
        if not self.is_empty():
            current_node = self.head
            if position == 0:
                self.head = current_node.next
                current_node.next = None
                return
            counter = 0
            previous = None
            while current_node and counter != position:
                previous = current_node
                current_node = current_node.next
                counter += 1
            if current_node is None:
                print('position not found')
                return
            previous.next = current_node.next
            current_node.next = None
        else:
            print('List is empty')

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def print_linked_list(self):
        if not self.is_empty():
            node = self.head
            mystr = ''
            while node is not None:
                if node.next is not None:
                    mystr += str(node.data) + ' -> '
                else:
                    mystr += str(node.data)
                node = node.next
            print(mystr)
        else:
            print('List is empty')

    def len_recursive(self, current_node):
        if current_node is None:
            return 0
        return 1 + self.len_recursive(current_node.next)

    def len_iterative(self, current_node):
        counter = 0
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_list(self):

        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_list_recursive(self):
        def _reverse_list_recursive(curr, prev):
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

            return _reverse_list_recursive(curr, prev)

        self.head = _reverse_list_recursive(self.head, None)

mylist = LinkedList()

mylist.print_linked_list()

mylist.prepend(0)

mylist.append(1)

mylist.append(2)

mylist.append(3)

mylist.append(4)

mylist.prepend(-1)

mylist.insert_node(55, 22)

# mylist.delete_node(55)

mylist.print_linked_list()
mylist.delete_node_position(5)

mylist.print_linked_list()

mylist.swap_nodes(0, 2)

mylist.print_linked_list()
mylist.reverse_list()
mylist.print_linked_list()
mylist.reverse_list()
mylist.print_linked_list()
mylist.reverse_list_recursive()
mylist.print_linked_list()
print(mylist.len_recursive(mylist.head))

print(mylist.len_iterative(mylist.head))

