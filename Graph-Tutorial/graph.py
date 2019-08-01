"""NOTE To Grader:
    The basic implementation of the graph and its requisite functions have been implemented below.
    For more advanced feautres of the graph adt, please see the appropriate challenges (2-8).

    Please note: I was referring to an earlier version of the repo that I had forked and cloned at the start of the term.

    As of 07/28/19, the required challenges are out of order and incomplete and will be refactored and completed by the end of the week (08/2/19).

"""


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
        self.id = vertex                # string
        self.neighbors = {}             # dictionary of vertex_id's to int weights

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight # add vertex-weight to self.neighbors dictionary

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors.keys()    # get all of the keys from the neighbors dictionary, keys == vertex_id strings

    def getId(self):
        """return the id of this vertex"""
        return self.id                  # get the vertex's id, a string

    def getEdgeWeight(self, vertex):
        """"return the weight of this edge"""
        return self.neighbors[vertex] if self.neighbors[vertex] else None #return the weight of a given vertex if the vertex is present in the self.neighbors dictionary

""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}              # a dictionary of vertex_id's to vertex objects
        self.numVertices = 0

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        self.numVertices += 1           # increment the count of number of vertices
        new_vertex = Vertex(key)        # create a new vertex object with the given vertex_id
        self.vertList[key] = new_vertex # add the vertex to the dictionary of self.vertList as vertex_id : vertex object
        return self.vertList[key]       # return the vertex object

    def getVertex(self, n):
        """return the vertex if it exists"""
        return self.vertList[n] if self.vertList[n] else None #return the vertex if the vertex is present in the self.vertList dictionary

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        if not self.vertList[f]:            # if the from_vert is not in the self.vertList
            new_vertex = Vertex(f)          # make a new vertex object
            self.vertList[f] = new_vertex   # add it to the self.vertList
        if not self.vertList[t]:            # if the to_vert is not in the self.vertList
            new_vertex = Vertex(t)          # make a new vertex object
            self.vertList[t] = new_vertex   # add it to the self.vertList
        self.vertList[f].addNeighbor(t,cost)# add the to_vert to the from_vert's neighbors dictionary with a weight

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()         # return all of the keys in the self.vertList dictionary, string vertex_ids

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values()) # return all of the vertex objects of the graph


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
