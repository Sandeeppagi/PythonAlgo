class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def insert(self, val):
        current = self
        parent = None
        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild
        if val < parent.val:
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)

    def insert_rec(self, val):
        curr = self
        if val < curr.val:
            if curr.leftChild:
                curr = curr.leftChild
                curr.insert_rec(val)
            else:
                curr.leftChild = Node(val)
        else:
            if curr.rightChild:
                curr = curr.rightChild
                curr.insert_rec(val)
            else:
                curr.rightChild = Node(val)

    def search(self, val):
        curr = self
        while curr:
            if val < curr.val:
                curr = curr.leftChild
            elif val > curr.val:
                curr = curr.rightChild
            else:
                return True
        return False

    def search_rec(self, val):
        curr = self
        if val < curr.val:
            if curr.leftChild:
                curr = curr.leftChild
                curr.search_rec(val)
            else:
                return False
        elif val > curr.val:
            if curr.rightChild:
                curr = curr.rightChild
                curr.search_rec(val)
            else:
                return False
        else:
            return True
        return False

    def delete(self, val):
        # if current node's val is less than that of root node,
        # then only search in left subtree otherwise right subtree
        if val < self.val:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        elif val > self.val:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        else:
            # deleting node with no children
            if self.leftChild is None and self.rightChild is None:
                self = None
                return None
            # deleting node with right child
            elif self.leftChild is None:
                tmp = self.rightChild
                self = None
                return tmp
            # deleting node with left child
            elif self.rightChild is None:
                tmp = self.leftChild
                self = None
                return tmp
            # deleting node with two children
            else:
                # first get the inorder successor
                current = self.rightChild
                # loop down to find the leftmost leaf
                while current.leftChild is not None:
                    current = current.leftChild
                self.val = current.val
                self.rightChild = self.rightChild.delete(current.val)

        return self
