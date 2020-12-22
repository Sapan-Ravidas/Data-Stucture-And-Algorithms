
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1



class AVLtree:
    def __init__(self):
        self.root = None



    def get_height(self, root):
        if root is None:
            return 0
        else:
            return root.height



    def get_bfactor(self, root):
        if root is None:
            return 0
        else:
            return self.get_height(root.left) - self.get_height(root.right)



    def insert(self, val):
        self.root = self.insert_util(self.root, val)



    def insert_util(self, root, val):
        if root is None:
            return Node(val)

        elif val < root.data:
            root.left = self.insert_util(root.left, val)

        else:
            root.right = self.insert_util(root.right, val)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        b_factor = self.get_bfactor(root)

        if b_factor > 1 and val < root.left.data:
            return self.clockWise_Rotate(root)

        if b_factor < -1 and val > root.right.data:
            return self.anticlockWise_Rotate(root)

        if b_factor > 1 and val > root.left.data:
            root.left = self.anticlockWise_Rotate(root.left)
            return self.clockWise_Rotate(root)

        if b_factor < -1 and val < root.right.data:
            root.right = self.clockWise_Rotate(root.right)
            return self.anticlockWise_Rotate(root)

        return root





    def deletion(self, val):
        self.root = self.deletionUtil(self.root, val)



    def deletionUtil(self, root, val):
        if root is None:
            return root
        elif val < root.data:
            root.left = self.deletionUtil(root.left, val)
        elif val > root.data:
            root.right = self.deletionUtil(root.right, val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_minvalue(root.right)
            root.data = temp.data
            root.right = self.deletionUtil(root.right, temp.data)

        if root is None:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        b_factor = self.get_bfactor(root)

        if b_factor > 1 and self.get_bfactor(root.left) >= 0:
            return self.clockWise_Rotate(root)

        if b_factor < -1 and self.get_bfactor(root.right) <= 0:
            return self.anticlockWise_Rotate(root)

        if b_factor > 1 and self.get_bfactor(root.left) < 0:
            root.left = self.anticlockWise_Rotate(root.left)
            return self.clockWise_Rotate(root)

        if b_factor < 1 and self.get_bfactor(root.right) > 0:
            root.right = self.clockWise_Rotate(root.right)
            return self.anticlockWise_Rotate(root)

        return root





    def clockWise_Rotate(self, root):
        new_root = root.left
        x = new_root.right
        new_root.right = root
        root.left = x

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root




    def anticlockWise_Rotate(self, root):
        new_root = root.right
        y = new_root.left
        new_root.left = root
        root.right = y

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root





    def get_minvalue(self, root):
        if root is None or root.left is None:
            return root
        else:
            return self.get_minvalue(root.left)





    def inOrder(self):
        if self.root is None:
            return "Tree is Empty"
        else:
            return self.inOrderUtil(self.root)




    def inOrderUtil(self, root):
        if root is None:
            return
        self.inOrderUtil(root.left)
        print(root.data, end= " ")
        self.inOrderUtil(root.right)



    def preOrder(self):
        if self.root is None:
            return "Tree is Empty"
        else:
            return self.preOrderUtil(self.root)



    def preOrderUtil(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.preOrderUtil(root.left)
        self.preOrderUtil(root.right)



if __name__=="__main__":
    T = AVLtree()
    T.insert(13)
    T.insert(9)
    T.insert(15)
    T.insert(5)
    '''
    T.insert(3)
    T.insert(2)
    T.insert(1)
    '''
    T.inOrder()
    print()
    T.preOrder()
    print()

    T.deletion(9)
    print()
    T.inOrder()
    print()
    T.preOrder()
    print()
