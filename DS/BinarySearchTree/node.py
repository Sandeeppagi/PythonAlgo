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
        if val < self.val:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
            else:
                print(f"Value not found at left {val}")
                return self
        elif val > self.val:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
            else:
                print(f"Value not found at right {val}")
                return self
        else:
            if self.rightChild is None and self.rightChild is None:
                self = None
                return None
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp
            elif self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.leftChild and self.rightChild:
                curr = self.rightChild
                while curr.leftChild:
                    curr = curr.leftChild
                self.val = curr.val
                self.rightChild = self.rightChild.delete(curr.val)
        return self


