import Queue

class Graph(object):
    
    def __init__(self):
        self.max_vertices = 6
        self.vertices = [0] * self.max_vertices
        self.count = 0
    
    def addNode(self, x):
        if self.count < self.max_vertices:
            self.vertices[self.count] = x
            self.count += 1
        else:
            raise Exception('Graph is Full')
    
    def getNodes(self):
        return self.vertices
    
class Node(object):

    def __init__(self, vertex, adjacentLength):
        self.adjacent = [0] * adjacentLength
        self.vertex = vertex
        self.adjacentCount = 0
        self.visited = False
    
    def addAdjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            raise Exception('No more adjacent Nodes can be added')
    
    def getAdjacent(self):
        return self.adjacent
    
    def getVertex(self):
        return self.vertex

def createNewGraph():
    g = Graph()
    sizeGraph = 6
    temp = [0] * sizeGraph

    temp[0] = Node('a',3)
    temp[1] = Node('b',0)
    temp[2] = Node('c',0)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 1)
    temp[5] = Node("f", 0)

    temp[0].addAdjacent(temp[1])
    temp[0].addAdjacent(temp[2])
    temp[0].addAdjacent(temp[3])
    temp[3].addAdjacent(temp[4])
    temp[4].addAdjacent(temp[5])

    for i in range(sizeGraph):
        g.addNode(temp[i])
    return g
def createNewGraphWithLoop():
    g = Graph()
    sizegraph = 6
    temp = [0] * sizegraph

    temp[0] = Node("a", 1)
    temp[1] = Node("b", 1)
    temp[2] = Node("c", 1)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 2)
    temp[5] = Node("f", 0)

    temp[0].addAdjacent(temp[1])
    temp[1].addAdjacent(temp[2])
    temp[2].addAdjacent(temp[3])
    temp[3].addAdjacent(temp[4])
    temp[4].addAdjacent(temp[1])
    temp[4].addAdjacent(temp[5])

    for i in range(sizegraph):
        g.addNode(temp[i])
    return g


g = createNewGraph()
n = g.getNodes()
start = n[0]
end = n[5]
print "Start at:", start.getVertex(), "End at: ", end.getVertex()

