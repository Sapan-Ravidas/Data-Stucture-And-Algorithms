from abc import ABC, abstractmethod
from collections import defaultdict, deque
import sys

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.residual = None
        self.flow = 0
        
    def isResidual(self):
        return self.capacity == 0
    
    def remainingCapacity(self):
        return self.capacity - self.flow
    
    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.flow -= bottleneck
        

class NetworkFlowSolver(ABC):
    def __init__(self, N, source, sink):
        self.N = N
        self.source = source
        self.sink = sink
        self.graph = defaultdict(list)
        self.visited = [False] * N
        self.maxFlow = 0
        self.solved = False
     
    def addEdge(self, start, end, capacity):
        if capacity <= 0:
            raise ValueError("Forward edge capacity <=0")
        edge1 = Edge(start, end, capacity)
        edge2 = Edge(end, start, 0)
        edge1.residual = edge2
        edge2.residual = edge1
        self.graph[start].append(edge1)
        self.graph[end].append(edge2) 
    
    def getMaxFlow(self):
        self.execute()
        return self.maxFlow
    
    def visited(self, i):
        self.visited[i] = True
        
    def markAllNodeAsUnvisited(self):
        self.visited = [False] * self.N
        
    def execute(self):
        if (self.solved):
            return
        self.solved = True
        self.solve()
        
    @abstractmethod
    def solve(self):
        pass
    
    def displayGraph(self):
        for i in range(self.N):
            print(f"node {i} ", end="-> ")
            for edge in self.graph[i]:
                print(f"({edge.start}, {edge.end}, {edge.capacity}, ) , ", end=" ")
            print()


class EdmonKarpSolver(NetworkFlowSolver):
    def __init__(self, N, source, sink):
        super().__init__(N, source, sink)
        
    def solve(self):
        flow = 0
        while True:
            self.markAllNodeAsUnvisited()
            flow = self.bfs()
            self.maxFlow += flow
            if flow == 0:
                break
            
    def bfs(self):
        queue = deque()
        self.visited[self.source] = True
        queue.append(self.source)
        
        prev = [None] * self.N
        while queue:
            node = queue.popleft()
            if node == self.sink:
                break
            for edge in self.graph[node]:
                capacity = edge.remainingCapacity()
                if capacity > 0 and self.visited[edge.end] == False:
                    self.visited[edge.end] = True
                    prev[edge.end] = edge
                    queue.append(edge.end)
        
        # for debugging purpuse of prev
        def display_prev():
            for i in range(self.N):
                if prev[i]:
                    print(f"{i} - > ({prev[i].start}, {prev[i].end}, {prev[i].capacity})")
        
        display_prev()
    
        # sink not reachable                
        if prev[self.sink] is None:
            return 0

        # finding the augmented path and bottleneck value
        bottleneck = sys.maxsize
        edge = prev[self.sink]
        while edge:
            bottleneck = min(bottleneck, edge.remainingCapacity())
            edge = prev[edge.start]
        
        # retrace augmented path and update the flow values
        edge = prev[self.sink]
        while edge:
            edge.augment(bottleneck)
            edge = prev[edge.start]
        
        return bottleneck


if __name__ == '__main__':
    # n is number of nodes including the source code and the sink
    n = 6
    s = n - 2
    t = n - 1
    
    solver = EdmonKarpSolver(n, s, t)
    
    edges = [
        (s, 0, 8),
        (s, 3, 3),
        
        (0, 1, 9),
        (3, 1, 7), 
        (3, 2, 4), 
        
        (1, t, 2), 
        (2, t, 5)
    ]
    
    for u, v, c in edges:
        solver.addEdge(u, v, c)
    
    
    print(solver.getMaxFlow())