from collections import  defaultdict

class Vertex:
    def __init__(self, name, source  = False, sink = False):
        self.name = name
        self.source = source
        self.sink = sink
    
    def __hash__(self):
        return hash((self.name, self.source, self.sink))
        

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.retuenEdge = None
    
    
class FlowNetwork:
    def __init__(self):
        self.vertices = []
        self.network = defaultdict(list)  # key ->cls-vertex : value -> list< cls-Edge >
    
    
    # add vertex to the network
    def addVertex(self, name, source = False, sink = False):
        # check for start and sink to be same vetex
        assert not (source and sink), "Vetrex cant be source and sink at the same time error"
        
        # check for duplicate vertices
        assert not self.vertexInNetwork(name), "Duplicate vertex error"
        
        if source == True:
            if self.getSource() != None:
                raise Exception("Source already exists")
        
        if sink == True:
            if self.getSink() != None:
                raise Exception("Sink already exists")
        
        newVertex = Vertex(name, source, sink)
        self.vertices.append(newVertex)
        self.network[newVertex] = []
          
    
    # check if vertex id already present in the network
    def vertexInNetwork(self, name):
        return  any([vertex.name == name for vertex in self.vertices])
    
    
    # add edge to the network
    def addEdge(self, src, dest, capacity):
        assert src != dest, "Cannot have same start and end point"
        
        if not self.vertexInNetwork(src):
            raise Exception(f"{src} vertex is not added in the network yet")
        
        if not self.vertexInNetwork(dest):
            raise Exception(f"{dest} vertex is not added in the network yet")
        
        newEdge = Edge(src, dest, capacity)
        returnEdge = Edge(dest, src, 0)
        newEdge.retuenEdge = returnEdge
        returnEdge.retuenEdge = newEdge
        
        vertex = self.getVertex(src)
        self.network[vertex].append(newEdge)
        
        returnVertex = self.getVertex(dest)
        self.network[returnVertex].append(returnEdge)
    
        
    # get the source / start node of the network
    def getSource(self):
        for vertex in self.vertices:
            if vertex.source == True:
                return vertex
        return None
    
    # get the vertex
    def getVertex(self, name):
        for vertex in self.vertices:
            if name == vertex.name:
                return vertex
            
    # get the edge
    def getEdges(self):
        edges = []
        for vertex in self.network:
            for edge in self.network[vertex]:
                edges.append(edge)
        return edges
    
    
    # get the sink node of the network
    def getSink(self):
        for vertex in self.vertices:
            if vertex.sink == True:
                return vertex
        return None
    
    
    # get the augmented path for the network
    def getPath(self, start, end, path):
        if start == end:
            return path
        for edge in self.network[start]:
            residual_capacity = edge.capacity - edge.flow
            if residual_capacity > 0 and not(edge, residual_capacity) in path:
                result = self.getPath(edge.end, end, path + [(edge, residual_capacity)])
                if result != None:
                    return result
        
        
    # calculate the max flow algorithms
    def calculateMaxFlow(self):
        source = self.getSource()
        sink = self.getSink()
        
        if (not source) or (not sink):
            raise Exception("Network doesn't have source or sink")
        
        path = self.getPath(source, sink, [])
        
        while path:
            flow = min(edge[1] for edge in path)
            for edge, res in path:
                edge.flow += flow
                edge.retuenEdge.flow -= flow
            path = self.getPath(source, sink, [])
        return sum(edge.flow for edge in self.network[source])
        

if __name__ == '__main__':
    fn = FlowNetwork()
    
    fn.addVertex('S', True, False)
    fn.addVertex('T', False, True)
    # map(fn.addVertex, ['A', 'B', 'C', 'D'])
    arr = ['A', 'B', 'C', 'D']
    for a in arr:
        fn.addVertex(a)
    
    fn.addEdge('S', 'A', 4)
    fn.addEdge('A', 'B', 4)
    fn.addEdge('B', 'T', 2)
    fn.addEdge('S', 'C', 3)
    fn.addEdge('C', 'D', 6)
    fn.addEdge('D', 'T', 6)
    fn.addEdge('B', 'C', 3)
    
    result = fn.calculateMaxFlow()
    print(result)