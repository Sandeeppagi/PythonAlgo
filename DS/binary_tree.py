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

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.preorder_print(tree.root, ""))
print(tree.inorder_print(tree.root, ""))
print(tree.postorder_print(tree.root, ""))
