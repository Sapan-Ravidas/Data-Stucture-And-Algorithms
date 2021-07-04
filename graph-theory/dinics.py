from abc import abstractmethod, ABC
from collections import defaultdict, deque
import sys

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.returnEdge = None
        
    def isResidula(self):
        return self.capacity == 0
    
    def remainingCapacity(self):
        return self.capacity - self.flow
    
    def augment(self, bottleneck):
        self.flow += bottleneck
        self.returnEdge.flow -= bottleneck
        

class NetworkFlowSolver(ABC):
    def __init__(self, source, sink, N):
        self.source = source
        self.sink = sink
        self.N = N
        self.solved = False
        self.maxFlow = 0
        self.graph = defaultdict(list)
        
    def addEdge(self, start, end, capacity):
        if capacity <= 0:
            raise ValueError("Forward edge can't be <= 0")
        edge1 = Edge(start, end, capacity)
        edge2 = Edge(end, start, 0)
        edge1.returnEdge = edge2
        edge2.returnEdge = edge1
        self.graph[start].append(edge1)
        self.graph[end].append(edge2)
        
    def getMaxFlow(self):
        self.execute()
        return self.maxFlow
    
    def execute(self):
        if self.solved:
            return
        self.solved = True
        self.solve()
    
    @abstractmethod
    def solve(self):
        pass
    
    
class DinicSolver(NetworkFlowSolver):
    def __init__(self, source, sink, N):
        super().__init__(source, sink, N)
        # self.level = [0] * N
        
    def solve(self):
        # next[i] indicates the next edge to take in the adjancy list for 
        # node i. This is of the Shimon Evene and Alon Itai optimization 
        # of pruning deads as the part of dfs phase 
        
        while self.bfs():
            next = [0] * self.N
            # find the ,ax flow by adding all augmenting path flows
            flow = self.dfs(self.source, next, sys.maxsize)
            while flow != 0:
                self.maxFlow += flow
                flow = self.dfs(self.source, next, sys.maxsize)

    
    # Do bfs from source to sink and compute the depth/level of each node
    # which is the minimum numbe of edges from that node the to source 
    def bfs(self):
        self.level = [-1] * self.N
        queue = deque()
        queue.append(self.source)
        self.level[self.source] = 0
        
        while queue:
            node = queue.popleft()
            for edge in self.graph[node]:
                capacity = edge.remainingCapacity()
                if capacity > 0 and self.level[edge.end] == -1:
                    self.level[edge.end] = self.level[node] + 1
                    queue.append(edge.end)
        # return whether we were able to reach the sink node
        return self.level[self.sink] != -1
            

    def dfs(self, node, next, flow):
        if node == self.sink:
            return flow
        
        numEdges = len(self.graph[node])
        while next[node] < numEdges:
            edge = self.graph[node][next[node]]
            capacity = edge.remainingCapacity()
            if capacity > 0 and self.level[edge.end] == self.level[node] + 1:
                bottleneck = self.dfs(edge.end, next, min(flow, capacity))
                if bottleneck > 0:
                    edge.augment(bottleneck)
                    return bottleneck
            next[node] += 1
        
        return 0


if __name__ == '__main__':
    n = 6
    source = n - 1
    sink = n - 2 
    
    solver = DinicSolver(source, sink, n)
    
    edges = [
        (source, 0, 8),
        (source, 3, 3),
        
        (0, 1, 9),
        (3, 1, 7), 
        (3, 2, 4), 
        
        (1, sink, 2), 
        (2, sink, 5)
    ]
    
    for u, v, c in edges:
        solver.addEdge(u, v, c)
    
    
    print(solver.getMaxFlow())
    