from collections import deque as d


""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""
class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors.keys()

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """"return the weight of this edge"""
        return self.neighbors[vertex] if self.neighbors[vertex] else None

""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        self.numVertices += 1
        new_vertex = Vertex(key)
        self.vertList[key] = new_vertex
        return self.vertList[key]

    def getVertex(self, n):
        """return the vertex if it exists"""
        return self.vertList[n] if self.vertList[n] else None

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if not self.vertList[f]:
            new_vertex = Vertex(f)
            self.vertList[f] = new_vertex
        if not self.vertList[t]:
            new_vertex = Vertex(t)
            self.vertList[t] = new_vertex
        self.vertList[f].addNeighbor(t,cost)

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())

    def breadth_first_search(self, vertex, n):
        # Make sure the input node is actually in the graph
        # Run breadth_first_search starting from the input node and going `n` levels deep
        # Return all nodes found at the `n`th level

        queue = d()
        degreesOfSeparation = int(n)
        result = []

        def __helper_breadth_first_search(current_vert, degreesOfSeparation):
            if self.vertList[current_vert].getNeighbors() and degreesOfSeparation>0 and len(queue) > 0:
                queue.extend(self.vertList[current_vert].getNeighbors())
            return __helper_breadth_first_search(queue.popleft(),degreesOfSeparation-1)

        if vertex not in self.vertList:
            raiseException("The vertex is not present in your graph.")
        # print(vertex,n)
        return __helper_breadth_first_search(vertex,n)

def make_graph_from_file(filepath):
    """input file should be of form:
            G
            1,2,3,4
            (1,2)
            (1,3)
            (2,4)
    returns an array of vertices (ints) and and array of edges (tuple of two vertices: source to target)
    """

    edges = []
    listOfVertices = []
    graphType = ""

    with open(filepath, "r") as f:
        entries = f.read().split("\n")

    for i, entry in enumerate(entries):
        if i == 0: # the first entry is either 'G' or 'D'
            if entry == 'G' or entry == 'D':
                graphType = entry
            else:
                raise Exception("File must begin with G or D.")
        elif i == 1: # the second entry is a list of vertices
            for i, v in enumerate(entry):
                    if not i % 2: # parse the string to get all numbers
                        listOfVertices.append(int(v))
        elif len(entry) > 0: # takes into account empty lines
            edges.append((int(entry[1]), int(entry[3])))
            if graphType == "G": # If it is a Graph and not a Digraph, add another edge in the opposite direction
                edges.append((int(entry[3]), int(entry[1])))

    return listOfVertices, edges

# Driver code

if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Friend 1")
    g.addVertex("Friend 2")
    g.addVertex("Friend 3")
    g.addVertex("Friend 4")
    g.addVertex("Friend 5")
    g.addVertex("Friend 6")
    g.addVertex("Friend 7")
    g.addVertex("Friend 8")
    g.addVertex("Friend 9")
    g.addVertex("ME!")
    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Friend 1", "Friend 2")
    g.addEdge("Friend 2", "Friend 3")
    g.addEdge("Friend 3", "Friend 4")
    g.addEdge("Friend 4", "Friend 5")
    g.addEdge("Friend 5", "Friend 6")
    g.addEdge("Friend 6", "Friend 7")
    g.addEdge("Friend 7", "Friend 8")
    g.addEdge("Friend 8", "Friend 9")
    g.addEdge("Friend 9", "ME!")
    g.addEdge("ME!", "Friend 1")

    g.addEdge("Friend 1", "Friend 3")
    g.addEdge("Friend 2", "Friend 4")
    g.addEdge("Friend 3", "Friend 5")
    g.addEdge("Friend 4", "Friend 6")
    g.addEdge("Friend 5", "Friend 7")
    g.addEdge("Friend 6", "Friend 8")
    g.addEdge("Friend 7", "Friend 9")
    g.addEdge("Friend 8", "ME!")
    g.addEdge("Friend 9", "Friend 1")
    g.addEdge("ME!", "Friend 2")

    # Challenge 1: Output the vertices & edges
    print("\n Challenge 1: Output the vertices & edges:")
    print("The vertices are: ", g.getVertices())

    print("The edges are: ")
    for v in g.vertList:
        print("( %s, %s , %s )" % (v, g.vertList[v].neighbors.keys(), g.vertList[v].neighbors.values()))

    print("\n stretch challenge for challenge #1")
    print(make_graph_from_file("/Users/jamesmccrory/Documents/dev/CS-2.2-labs/sampleGraphFile.txt"))

    # challenge 2: testing the getNeighbors method.
    print("\nChallenge 2: testing the getNeighbors method:")
    print('testing getNeighbors() method:')
    for v in g.vertList:
        print(v)
        print(g.vertList[v].getNeighbors())

    # challenge 3: breadth first search:
    print("\nchallenge 3: breadth first search:")
    print(g.breadth_first_search("Friend 1", 1))
