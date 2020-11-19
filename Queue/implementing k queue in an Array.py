

class KQueue:
    def __init__(self, n, k):
        self.Arr = [0] * n
        self.Front = [-1] * k
        self.Rear = [-1] * k
        self.Next = [i+1 for i in range(n)]
        self.Next[n-1] = -1
        self.free = 0



    def isEmpty(self, qn):
        if self.Front[qn] == -1:
            return True



    def isFull(self):
        if self.free == -1:
            return True



    def enqueue(self, qn, value):
        if self.isFull():
            return "Array is Full"

        index = self.free
        if self.isEmpty(qn):
            self.Front[qn] = self.Rear[qn] = index
        else:
            self.Rear[qn] = index
            self.Next[self.Rear[qn]] = index

        self.Arr[index] = value
        self.free = self.Next[index]
        self.Next[index] = -1



    def dequeue(self, qn):
        if self.isEmpty(qn):
            return "Queue is Empty"
        index = self.Front[qn]
        self.Front[qn] = self.Next[index]
        self.Next[index] = self.free
        self.free = index
        return self.Arr[index]
