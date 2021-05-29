from DS.BinarySearchTree.node import Node


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert_rec(val)
        else:
            self.root = Node(val)
            return True


BST = BinarySearchTree(6)
print(f"Root for BST is {BST.root.val}")