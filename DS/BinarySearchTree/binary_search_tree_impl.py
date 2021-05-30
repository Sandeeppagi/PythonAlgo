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

    def search_rec(self, val):
        if self.root:
            if self.root.val == val:
                return True
            return self.root.search_rec(val)
        else:
            return False

    def search(self, val):
        if self.root:
            if self.root.val == val:
                return True
            return self.root.search(val)
        else:
            return False

    def delete(self, val):
        if self.root is not None:
            self.root = self.root.delete(val)


# BST = BinarySearchTree(6)
# print(f"Root for BST is {BST.root.val}")