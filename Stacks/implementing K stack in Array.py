class Kstack:
    def __init__(self, n, k):
        self.Arr = [0] * n
        self.Top = [-1] * k
        self.Next = [i+1 for i in range(n)]
        self.Next[n-1] = -1
        self.free = 0



    def isFull(self):
        if self.free == -1:
            return True



    def isEmpty(self, sn):
        if self.Top[sn] == -1:
            return True



    def push(self,value, sn):
        if self.isFull():
            return "Array is Full"

        index = self.free
        self.free = self.Next[self.free]
        self.Arr[index] = value
        self.Next[index] = self.Top[sn]
        self.Top[sn] = index



    def pop(self, sn):
        if self.isEmpty(sn):
            return "Stack {} Is Empty".format(sn)

        index = self.Top[sn]
        value = self.Arr[index]
        self.Top[sn] = self.Next[index]
        self.Next[index] = self.free
        self.free = index
        return value





if __name__=="__main__":
    n = 5 ; k = 3
    x = Kstack(n, k)
    x.push(95, 0)
    x.push(88, 1)
    x.push(75, 2)
    print(x.pop(0))
    x.push(23, 1)
    print(x.pop(0))
    x.push(66, 0)
