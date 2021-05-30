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
        if self.root:
            self.root = self.root.delete(val)

    def pre_order(self, start, arr):
        if start:
            arr.append(start.val)
            arr = self.pre_order(start.leftChild, arr)
            arr = self.pre_order(start.rightChild, arr)
        return arr

    def post_order(self, start, arr):
        if start:
            arr = self.post_order(start.leftChild, arr)
            arr = self.post_order(start.rightChild, arr)
            arr.append(start.val)
        return arr

    def inorder_order(self, start, arr):
        if start:
            arr = self.inorder_order(start.leftChild, arr)
            arr.append(start.val)
            arr = self.inorder_order(start.rightChild, arr)
        return arr

# BST = BinarySearchTree(6)
# print(f"Root for BST is {BST.root.val}")