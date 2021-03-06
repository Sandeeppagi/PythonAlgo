class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

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

    def insert_at_head(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return self.head

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

    def length(self):
        current_node = self.head
        counter = 0
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter

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

    def merge_sorted_list(self, ll):
        p = self.head
        q = ll.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not q:
            s.next = p
        if not p:
            s.next = q

        self.head = new_head
        return self.head

    def remove_duplicate(self):
        curr = self.head
        prev = None

        dup_values = dict()

        while curr:
            if curr.data in dup_values:
                prev.next = curr.next
                curr = None
            else:
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.next

    def nth_to_last_node_v1(self, n):
        remaining_len = self.len_recursive(self.head)
        curr = self.head

        while curr:
            if remaining_len == n:
                print(curr.data)
                return curr.data
            remaining_len -= 1
            curr = curr.next
        if curr is None:
            return

    def nth_to_last_node_v2(self, n):
        q = self.head
        p = self.head

        if n > 0:
            count = 0
            while q:
                count += 1
                if(count>=n):
                    break
                q = q.next
            if not q:
                print(str(n) + " is greater than the number of the nodes in list")
                return
            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None

    def count_occurences(self, data):
        curr = self.head
        count = 0
        while curr:
            if curr.data == data:
                count += 1
            curr = curr.next
        print(count)
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)


    def is_palindrome_v1(self):
        s = ""
        curr = self.head
        while curr:
            s += curr.data
            curr = curr.next
        return s == s[::-1]

    def is_palindrome_v2(self):
        stack = []
        curr = self.head

        while curr:
            stack.append(curr.data)
            curr = curr.next

        curr = self.head
        while curr:
            data = stack.pop()
            if data != curr.data:
                return False
            curr = curr.next
        return True

    def swap_tail_to_head(self):
        prev = None
        curr = self.head

        if not curr:
            print('List is empty')
        if not curr.next:
            print('List has only one element')

        while curr.next:
            prev = curr
            curr = curr.next
        head = self.head
        self.head = curr
        prev.next = head
        head.next, curr.next = curr.next, head.next

    def move_tail_to_head(self):
        prev = None
        curr = self.head

        if not curr:
            print('List is empty')
        if not curr.next:
            print('List has only one element')

        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        curr.next = self.head
        self.head = curr

    def sum_two_lists(self, llist):
        curr_1 = self.head
        curr_2 = llist.head
        ints_1 = []
        ints_2 = []

        while curr_1:
            ints_1.append(curr_1.data)
            curr_1 = curr_1.next

        while curr_2:
            ints_2.append(curr_2.data)
            curr_2 = curr_2.next

        str_1 = [str(item) for item in ints_1]
        str_2 = [str(item) for item in ints_2]

        number_1 = int("".join(str_1[::-1]))
        number_2 = int("".join(str_2[::-1]))

        result = str(number_1 + number_2)

        array = [int(x) for x in result[::-1]]

        new_list = LinkedList()
        for item in array:
            new_list.append(item)

        return new_list


# mylist = LinkedList()
#
# mylist.print_linked_list()
#
# mylist.prepend(0)
#
# mylist.append(1)
#
# mylist.append(2)
#
# mylist.append(3)
#
# mylist.append(4)
#
# mylist.prepend(-1)
#
# mylist.insert_node(55, 22)
#
# # mylist.delete_node(55)
#
# mylist.print_linked_list()
# mylist.delete_node_position(5)
#
# mylist.print_linked_list()
#
# mylist.swap_nodes(0, 2)
#
# mylist.print_linked_list()
# mylist.reverse_list()
# mylist.print_linked_list()
# mylist.reverse_list()
# mylist.print_linked_list()
# mylist.reverse_list_recursive()
# mylist.print_linked_list()
# print(mylist.len_recursive(mylist.head))
#
# print(mylist.len_iterative(mylist.head))
#
#
# sort_1 = LinkedList()
# sort_1.append(0)
# sort_1.append(3)
# sort_1.append(8)
# sort_1.append(19)
# sort_1.append(21)
#
# sort_2 = LinkedList()
# sort_2.append(2)
# sort_2.append(5)
# sort_2.append(9)
# sort_2.append(11)
# sort_2.append(20)
# print("-"*15)
# sort_1.print_linked_list()
# sort_2.print_linked_list()
# print("-"*15)
# print('Merging sorted list')
#
# sort_1.merge_sorted_list(sort_2)
# sort_1.print_linked_list()
# print("-"*15)
# print('Remove duplicates')
# dup_list = LinkedList()
# dup_list.append(0)
# dup_list.append(0)
# dup_list.append(0)
# dup_list.append(1)
# dup_list.append(3)
# dup_list.append(5)
# dup_list.append(1)
# dup_list.append(5)
# dup_list.append(6)
# dup_list.append(7)
# dup_list.print_linked_list()
# dup_list.remove_duplicate()
# dup_list.print_linked_list()
# print("-"*15)
# print("Getting Nth last node")
# dup_list.nth_to_last_node_v1(3)
# print(dup_list.nth_to_last_node_v2(3))
# print("-"*15)
# print("Counting occurrences")
# dup_list1 = LinkedList()
# dup_list1.append(0)
# dup_list1.append(0)
# dup_list1.append(0)
# dup_list1.append(1)
# dup_list1.append(3)
# dup_list1.append(5)
# dup_list1.append(1)
# dup_list1.append(5)
# dup_list1.append(6)
# dup_list1.append(7)
# dup_list1.print_linked_list()
# dup_list1.count_occurences(0)
# print(dup_list1.count_occurences_recursive(dup_list1.head, 5))
# print("-"*15)
# pal_list = LinkedList()
# pal_list.append('r')
# pal_list.append('a')
# pal_list.append('d')
# pal_list.append('a')
# pal_list.append('r')
# pal_list.print_linked_list()
# print(f"Is list Palindrome ? {pal_list.is_palindrome_v1()}")
# print(f"Is list Palindrome ? {pal_list.is_palindrome_v2()}")
# print("-"*15)
# print('Sawp head and tail')
# head_to_tail_list = LinkedList()
# head_to_tail_list.append('A')
# head_to_tail_list.append('B')
# head_to_tail_list.append('C')
# head_to_tail_list.append('D')
#
# head_to_tail_list.print_linked_list()
#
# head_to_tail_list.swap_tail_to_head()
# head_to_tail_list.print_linked_list()
#
# print("-"*15)
# print('Move head and tail')
# head_to_tail_list_move = LinkedList()
# head_to_tail_list_move.append('A')
# head_to_tail_list_move.append('B')
# head_to_tail_list_move.append('C')
# head_to_tail_list_move.append('D')
# head_to_tail_list_move.print_linked_list()
# head_to_tail_list_move.move_tail_to_head()
# head_to_tail_list_move.print_linked_list()
#
# print("-"*15)
# print('Sum Two Linked Lists')
#
# num_1 = LinkedList()
# num_2 = LinkedList()
#
# num_1.append(5)
# num_1.append(6)
# num_1.append(3)
#
# num_2.append(8)
# num_2.append(4)
# num_2.append(2)
# num_1.print_linked_list()
# num_2.print_linked_list()
# final_list = num_1.sum_two_lists(num_2)
# final_list.print_linked_list()
