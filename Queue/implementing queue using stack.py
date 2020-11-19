'''making deueue operation costly'''
class CostlyDequeue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def enqueue(self, value):
        self.stack1.append(value)


    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        x = self.stack2.pop()
        return x


'''making enqueue operation costly'''
class CostlyEnqueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def enqueue(self, value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            self.stack1.append(value)
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        x = self.stack1.pop()


'''using recurssion'''
class UsingRecurssion:
    def __init__(self):
        self.stack = []


    def enqueue(self, value):
        self.stack.append(value)


    def dequeue(self):
        if not self.stack:
            return

        x = self.stack.pop()
        if not self.stack:
            return x

        item = self.dequeue()
        self.stack.append(x)
        return item


if __name__=="__main__":
    q = UsingRecurssion()
    q.enqueue(1)
    print(q.dequeue())
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
