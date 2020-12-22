import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
        '''1 for red, 0 for black'''



class RedBlackTree:
    def __init__(self):
        self.root = None



    def preOrder(self):
        self._preOrder(self.root)
        print()

    def _preOrder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self._preOrder(root.left)
        self._preOrder(root.right)



    def inOrder(self):
        self._inOrder(self.root)
        print()

    def _inOrder(self, root):
        if root is None:
            return
        self._inOrder(root.left)
        print(root.data, end=" ")
        self._inOrder(root.right)



    def insert(self, value):
        node = Node(key)
