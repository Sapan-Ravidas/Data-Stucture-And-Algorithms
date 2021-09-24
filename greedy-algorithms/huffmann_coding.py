import atexit, sys, io

buffer = io.StringIO()
sys.stdout = buffer

@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue())


class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None



class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0



    def build_heap(self, arr):
        self.heap = arr
        self.size = len(arr)
        for i in range((self.size - 1)//2, -1, -1):
            self.heapify(i)



    def heapify(self, i):
        l = (i + 1)* 2 - 1
        r = (i + 1)* 2
        if l < self.size and self.heap[l].freq < self.heap[i].freq:
            smallest = l
        else:
            smallest = i

        if r < self.size and self.heap[r].freq < self.heap[smallest].freq:
            smallest = r

        if i != smallest:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)



    def extract_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        x = self.heap.pop()
        self.size -= 1
        self.heapify(0)
        return x


    def insert(self, node):
        self.heap.append(node)
        i = self.size
        self.size += 1
        while i > 0 and self.heap[(i - 1)//2].freq > self.heap[i].freq:
            self.heap[(i - 1)//2], self.heap[i] = self.heap[i], self.heap[(i - 1)//2]
            i = (i - 1)//2




def get_code(root, temp, result, top):
    if root.left:
        temp[top] = 0
        get_code(root.left, temp, result, top + 1)

    if root.right:
        temp[top] = 1
        get_code(root.right, temp, result, top + 1)

    if root.left is None and root.right is None:
        s = "{}: {}".format(root.data, ''.join(map(str, temp[: top])))
        result.append(s)

    return result




def get_huffmann_code(data):
    H = MinHeap()
    arr = []
    n = 0
    for a, b in data:
        x = Node(a, b)
        arr.append(x)
        n += 1

    H.build_heap(arr)

    for _ in range(n-1):
        x = Node("/", 0)
        x.left = H.extract_min()
        x.right = H.extract_min()
        x.freq = x.left.freq + x.right.freq
        H.insert(x)

    temp = [0] * (n - 1)
    root = H.extract_min()
    result = []
    result = get_code(root, temp, result, 0)
    return result


if __name__=="__main__":
    freq = [40, 30, 20, 5, 3, 2]
    char = ['a', 'b', 'c', 'd', 'e', 'f']
    data = zip(char, freq)
    result = get_huffmann_code(data)
    for i in result:
        print(i)
