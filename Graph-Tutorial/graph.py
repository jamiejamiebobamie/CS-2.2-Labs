#!python

# Challenge 1:

# This tutorial will focus on properties of a social network.
# To begin with, we'll need to define a network as a set of people (vertices)
# and the people they know.
# If person A knows person B then there is an edge between them.
# We will begin by assuming that if person A knows person B then the reverse is also true.
# (So the edge is undirected).
#
# Draw a graph with you at the center connected by an edge to another 9 people you know.
# Do any of these 9 know each other?
# If so draw an edge between them.
# This will be your "Social Graph" to use as a sample in the rest of this tutorial.
# Your graph must have the following properties:
# Every person knows at least 2 other people.
# No person knows more than 5 people.
# Challenge Add a diagram (or hand drawn image) of your friend network
# to the readme of your tutorial code.
# Label the nodes with you and your 9 friends names.
# If you don't want to use your real friends,
# feel free to use Faker to give fake names.
#
# Implement in code
#
# Throughout this tutorial we will build up a graph data structure that will
# implement our graph and graph algorithms in python.
#
# We will be building onto the basic Graph Abstract Data Type (ADT)
# which is defined as follows:
#
# Graph() #creates a new, empty graph.
# addVertex(vert) #adds an instance of Vertex to the graph.
# addEdge(fromVert, toVert) #Adds a new, directed edge to the graph that connects two vertices.
# addEdge(fromVert, toVert, weight) #Adds a new, weighted, directed edge to the graph that connects two vertices.
# getVertex(vertKey) #finds the vertex in the graph named vertKey.
# getVertices() #returns the list of all vertices in the graph.

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
        # TODO check if vertex is already a neighbor
        # TODO if not, add vertex to neighbors and assign weight.

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " +
        str([x.id for x in self.neighbors])

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        # TODO return the neighbors

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """return the weight of this edge"""
        # TODO return the weight of the edge from this
        # vertext to the given vertex.


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
        # TODO increment the number of vertices
        # TODO create a new vertex
        # TODO add the new vertex to the vertex list
        # TODO return the new vertex

    def getVertex(self, n):
        """return the vertex if it exists"""
        # TODO return the vertex if it is in the graph

    def addEdge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        # TODO if both vertices in the graph, add the
        # edge by making t a neighbor of f
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex f is stored in self.vertList[f].

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Friend 1")
    g.addVertex("Friend 2")
    g.addVertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Friend 1", "Friend 2")
    g.addEdge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.getVertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))
