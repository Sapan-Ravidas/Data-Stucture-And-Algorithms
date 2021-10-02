import heapq

class Node:
    def __init__(self, freq, name=' '):
        self.name = name
        self.frequency = freq
        self.left = None
        self.right = None
        
    def __repr__(self):
        return f"Node({self.name}, {self.frequency})"

    def __lt__(self, other):
        return self.frequency < other.frequency
    
    def __eq__(self, other):
        return self.frequency == other.frequency


class HuffmannTree:
    def __init__(self):
        self.root = None

    # print code value for each character
    def printCodes(self):
        self._printCodes(self.root, '')
    
    def _printCodes(self, root, code):
        if root is None:
            return
        if root.left:
            self._printCodes(root.left, code + '0')
        if root.right:
            self._printCodes(root.right, code + '1')
        if root.left is None and root.right is None:
            print(f"{root} -> {code}")
            
    # decode a given code to string eg. 001100 to its actual string value
    def decode(self, code):
        def get_char(node, string):
            if node is None:
                return
            if node.left is None and node.right is None:
                string[0] += node.name
                return self.root
            else:
                return node
        
        current = self.root
        string = ['']
        for s in code:
            if s == '0':
                current = get_char(current.left, string)
            else:
                current = get_char(current.right, string)
        
        print(string)
        

def huffmann_coding(freq):
    heapq.heapify(freq)
    T = HuffmannTree()
    
    try:
        while freq:
            left = heapq.heappop(freq)
            right = heapq.heappop(freq)
            temp = Node(left.frequency + right.frequency)
            temp.left = left
            temp.right = right
            T.root = temp
            
            heapq.heappush(freq, temp)
    except :
        pass 
    
    T.printCodes()
    T.decode('101111100')


if __name__ == '__main__':
    freq = [
        Node(name='a', freq=40),
        Node(name='b', freq=30),
        Node(name='c', freq=20),
        Node(name='d', freq=5),
        Node(name='e', freq=3),
        Node(name='f', freq=2),
    ]
    
    huffmann_coding(freq)