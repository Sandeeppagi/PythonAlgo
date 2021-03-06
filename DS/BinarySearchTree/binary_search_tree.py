class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert_node_v1(self, value):
        node = Node(value)
        curr = self.root

        while curr:
            if curr.data < value:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = node
                    break
            else:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = node
                    break

    def insert_node_v2(self, start, value):
        if start.data < value:
            if start.right:
                self.insert_node_v2(start.right, value)
            else:
                start.right = Node(value)
                return
        else:
            if start.left:
                self.insert_node_v2(start.left, value)
            else:
                start.left = Node(value)
                return

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    #               8
    #           /       \
    #          3          10
    #         /  \      /   \
    #        1    6     9   11

    def is_bst_satisfied(self):
        return self.helper_is_bst(self.root, True)

    def helper_is_bst(self, curr, is_bst):
        if curr.left:
            if curr.left.data < curr.data:
                is_bst = self.helper_is_bst(curr.left, is_bst)
            else:
                is_bst = False
        if curr.right:
            if curr.right.data > curr.data:
                is_bst = self.helper_is_bst(curr.right, is_bst)
            else:
                is_bst = False
        return is_bst

    def is_bst_satisfied_v2(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.data
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(self.root)



print("-" * 30)
print('Insert nodes in BST without recursion')
bst = BinarySearchTree(8)
bst.insert_node_v1(3)
bst.insert_node_v1(10)
bst.insert_node_v1(1)
bst.insert_node_v1(6)
bst.insert_node_v1(9)
bst.insert_node_v1(11)
#               8
#           /       \
#          3          10
#         /  \      /   \
#        1    6     9   11
print(bst.preorder_print(bst.root, ""))
print("-" * 30)
print('Insert nodes in BST with recursion')
bst_v1 = BinarySearchTree(8)
bst_v1.insert_node_v2(bst_v1.root, 3)
bst_v1.insert_node_v2(bst_v1.root, 10)
bst_v1.insert_node_v2(bst_v1.root, 1)
bst_v1.insert_node_v2(bst_v1.root, 6)
bst_v1.insert_node_v2(bst_v1.root, 9)
bst_v1.insert_node_v2(bst_v1.root, 11)
#               8
#           /       \
#          3          10
#         /  \      /   \
#        1    6     9   11
print(bst.preorder_print(bst.root, ""))
print("-" * 30)
print('Check if tree is BST')
print(bst_v1.preorder_print(bst_v1.root, ""))
print(f'Tree is BinarySearchTree: {bst.is_bst_satisfied()}')
bst_v2 = BinarySearchTree(8)
bst_v2.root.left = Node(3)
bst_v2.root.right = Node(10)
bst_v2.root.left.left = Node(1)
bst_v2.root.left.right = Node(2)
bst_v2.root.right.left = Node(9)
bst_v2.root.right.right = Node(11)
#               8
#           /       \
#          3          10
#         /  \      /   \
#        1    2     9   11
print(bst_v2.preorder_print(bst_v2.root, ""))
print(f'Tree is BinarySearchTree: {bst_v2.is_bst_satisfied()}')
print("-" * 30)
print('Check if tree is BST version 2')
print(f'Tree is BinarySearchTree: {bst.is_bst_satisfied_v2()}')
print(f'Tree is BinarySearchTree: {bst_v2.is_bst_satisfied_v2()}')
