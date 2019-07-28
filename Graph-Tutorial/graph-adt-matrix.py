# The Graph Abstract Data Type (ADT) is defined as follows:
#
# class `Graph()``
# creates a new, empty graph.
#
# has the methods
# addVertex(vert) adds -> a new vertex
# addEdge(fromVert, toVert) adds -> a directed edge
# addEdge(fromVert, toVert, weight) adds -> a weighted, directed edge.
# getVertex(vertKey) finds -> the named vertKey
# getVertices() returns -> the list of all vertices.
#
# graph should be implemented with an adjacency matrix.


class AMGraph(object):
    """An Graph ADT with adjacency matrix.
    """
    def __init__(self, numberOfVertices):
        self.numberOfVertices = numberOfVertices
        self.vertices = [[0]*self.numberOfVertices for _ in range(self.numberOfVertices)]

    def addVertex(self, n=1):
        """increases the number of vertices by n.
        adds new edges of weight 0 to each of the existing vertices.
        adds the new vertices to the end of the vertex matrix.
        """
        number = int(n) #   cast the number to an int regardless.
        self.numberOfVertices += number
        for vertex in self.vertices:
            addVertices = [0]*number
            vertex.extend(addVertices)
        self.vertices.append([0]*self.numberOfVertices)

    def addEdge(self,vFrom, vTo, weight=1):
        """adds a directed edge from a vertex to a vertex with a given weight
           if weight is not given, all edges are assumed to have a weight of one.
        """
        # check to make sure the vertices exist:
        if vFrom-1 >= 0 and vTo-1 >= 0 and vTo-1 <= self.numberOfVertices and vFrom-1 <= self.numberOfVertices:
            self.vertices[vFrom-1][vTo-1] = weight

    def addEdges(self, graph_data):
        """takes in an array of tuples (from_vert, to_vert) and adds their edges of weight 1 to the graph."""
        for entry in graph_data:
            self.addEdge(entry[0],entry[1],1)

    def getVertex(self, vertKey):
        """returns the vertex matrix
           takes in a vertKey which is the index of the desired vertex in the self.vertices array
           returns the item at that index in the array.
        """
        return self.vertices[vertKey-1]

    def getVertices(self):
        """returns the vertex matrix"""
        return self.vertices

    def getEdges(self, vertex):
        """returns the the edges for a single vertex"""
        return self.vertices[vertex-1]
