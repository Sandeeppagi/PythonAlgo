from Stack.my_queue import Queue
from Stack.stack import Stack


class Node:
    """
    Creating Node class used in the tree
    """

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    """
    Binary tree class
    """

    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        """
        Print->Left->Right
        :return:
        """
        if start:
            traversal += (str(start.data) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7


    def inorder_print(self, start, traversal):
        """
        Left->Print->Right
        :param start:
        :param traversal:
        :return:
        """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7


    def postorder_print(self, start, traversal):
        """
        Left->Right->Print
        :param start:
        :param traversal:
        :return:
        """
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.data) + '-')
        return traversal

    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7

    def level_order_traversal(self, start, traversal):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        while queue.size() > 0:
            traversal += (str(queue.peek()) + '-')
            # queue.__str__()
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7


    def reverse_level_order_traversal(self, start, traversal):
        if start is None:
            return

        stack = Stack()
        queue = Queue()
        queue.enqueue(start)

        while queue.size() > 0:
            node = queue.dequeue();
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        for i in range(stack.size()):
            item = stack.pop()
            traversal += str(item.data) + "-"

        return traversal

    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7


    def tree_height(self, node):
        if node is None:
            return -1

        left_height = self.tree_height(node.left)
        right_height = self.tree_height(node.right)

        return 1 + max(left_height, right_height)

    def tree_size_v1(self, node):
        if node is None:
            return 0
        return 1 + self.tree_size_v1(node.left) + self.tree_size_v1(node.right)

    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7

    def tree_size_v2(self, node, size):
        if node:
            size = self.tree_size_v2(node.left, size)
            size = self.tree_size_v2(node.right, size)
            size += 1
        return size

    def tree_size_v3(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size


#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print('-' * 30)
print('Pre Ordered traversal')
print(tree.preorder_print(tree.root, ""))
print('-' * 30)
print('In Ordered traversal')
print(tree.inorder_print(tree.root, ""))
print('-' * 30)
print('Post Ordered traversal')
print(tree.postorder_print(tree.root, ""))
print('-' * 30)
print('Level Ordered traversal')
print(tree.level_order_traversal(tree.root, ""))
print('-' * 30)
print('Reversed Level Ordered traversal')
print(tree.reverse_level_order_traversal(tree.root, ""))
print('-' * 30)
print(f"Height of the tree {tree.tree_height(tree.root)}")
print('-' * 30)
print('Size of the tree V1')
print(tree.tree_size_v1(tree.root))
print('-' * 30)
print('Size of the tree V2')
print(tree.tree_size_v2(tree.root, 0))
print('-' * 30)
print('Size of the tree V3')
print(tree.tree_size_v3())
