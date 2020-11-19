class Tree:
    def __init__(self):
        self.root = None



    def newNode(self, data):
        self.data = data
        self.left = None
        self.right = None



    def inOrder(self):
        if self.root is None:
            return "Tree is Empty"
        else:
            return inOrderUtil(self.root)



    def inOrderUtil(self, root):
        if root is None:
            return
        self.inOrderUtil(root.left)
        print(root.data, end= " ")
        self.inOrderUtil(root.right)
