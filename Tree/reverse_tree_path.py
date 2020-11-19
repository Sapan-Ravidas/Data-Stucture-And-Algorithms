class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class Tree:
    def __init__(self):
        self.root = None



    def create_tree(self, arr, i, n):
        root = None
        if i < n:
            if self.root is None:
                self.root = Node(arr[i])
                root = self.root
            else:
                root = Node(arr[i])

            root.left = self.create_tree(arr, 2*i+1, n)
            root.right = self.create_tree(arr, 2*i+2 , n)

        return root




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




    def reversePath(self, node):
        map = dict()
        next_pos = [0]
        self.reversePath_(self.root, node, 0, next_pos, map)



    def reversePath_(self, root, node, level, next_pos, map):

        if root is None:
            return

        if root.data == node:
            map[level] = root.data
            root.data = map[next_pos[0]]
            next_pos[0] += 1
            return root

        map[level] = root.data; print(root.data)
        left = self.reversePath_(root.left, node, level+1, next_pos, map)

        if left is None:
            right = self.reversePath_(root.right, node, level+1, next_pos, map)

        if left or right:
            root.data = map[next_pos[0]]
            next_pos[0] += 1
            if left:
                return left
            else:
                return right

        return





'''
if __name__=="__main__":
    T = Tree()
    arr = [7, 6, 5, 4, 3, 2, 1]
    T.create_tree(arr, 0, len(arr))
    T.inOrder(); print()
    T.reversePath(2)
    T.inOrder(); print()
'''
