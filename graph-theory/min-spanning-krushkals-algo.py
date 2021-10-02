import heapq
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        
    def add_edges(self, u, v, w):
        self.graph.append((u, v, w))
        
    # find
    def find(self, parent, i):
        if i == parent[i]:
            return i
        return self.find(parent, parent[i])
    
    # union
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        
        if rank[xroot] > rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    
    # Applying Krushkal Algorithm
    def krushkalAlgo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda x: x[2])
        parent = {i: i for i in range(1, self.V + 1)}
        rank = {i : 0 for i in range(1, self.V + 1)}
        
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)
        
        print("Krushkal's Algorithm")
        for u, v, weight in result:
            print(f"{u} - {v} : {weight}")
            
            
def MinimumSpanningTree(edges, N):
    G = Graph(N)
    for u, v, w in edges:
        G.add_edges(u, v, w)
        G.add_edges(v, u, w)
        
    G.krushkalAlgo()


if __name__ == '__main__':
    N = 7
    edges = [ 
        (1, 6, 10),
        (6, 5, 25),
        (5, 7, 24),
        (5, 4, 22),
        (7, 4, 18), 
        (7, 2, 14), 
        (1, 2, 28), 
        (2, 3, 16), 
        (3, 4, 12)
    ]
    
    MinimumSpanningTree(edges, N)
    