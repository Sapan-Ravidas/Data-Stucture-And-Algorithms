from collections import defaultdict
import sys

def prims(edges, n, start):
    result = []
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    select = {i : False for i in range(1, n + 1)}
    
    e, u = 0, start

    while e < n - 1:
        select[u] = True
        min_value = sys.maxsize
        temp = u
        for v, weight in graph[u]:
            if select[v] == False and weight < min_value:
                temp = v
                min_value = weight
        u = temp
        e += 1
        result.append((u, min_value))
        
    # print prims
    stringresult = ''
    for v, weight in result:
        stringresult += f'{start} - {v} : {weight}\n'
        start = v
        
    print(stringresult)
    

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
    
    prims(edges, N, 1)
    