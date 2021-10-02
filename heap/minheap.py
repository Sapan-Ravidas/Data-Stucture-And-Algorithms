class MinHeap:
    def __init__(self):
        self.size = 0
        self.heap = []
    
    # min- heapify    
    def heapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)
            
    # build-heap
    def build_heap(self, arr):
        self.size = len(arr)
        self.heap = arr
        for i in range((self.size - 1) // 2, -1, -1):
            self.heapify(i)
            
    # extract-min
    def extract_min(self):
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[: -1]
        self.size -= 1
        
        self.heapify(0)
        return min_value
            
    # decrease_key
    def decrease_key(self, index, value):
        self.heap[index] = value
        while index > 0 and self.heap[(index - 1) // 2] > self.heap[index]:
            self.heap[index], self.heap[(index  -1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            index = (index - 1) // 2


if __name__ == '__main__':
    arr = [9, 6, 5, 0, 8, 2, 1, 3]
    H = MinHeap()
    H.build_heap(arr)
    print(H.heap)
    H.decrease_key(len(arr) - 1, -1)
    print(H.heap)


            