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
        """
        challenge3.py contains the code below, but uses a different graph implementation than the one in this file.
        Please refer to challenge3.py and the accompanying graph_adt_list.py file for BFS.
        """

        def findVertexIndex(vertex_id):
            # vertex argument is a string that is the label or id of the vertex , NOT a linkedlist object
            # returns the vertices index in the graph if present
            # otherwise returns False
            for i, v in enumerate(graph.vertices):
                if int(v.id) == int(vertex_id):
                    return i
            return False

        # check to see if the node is in the graph
        index = findVertexIndex(node.id)

        if not index > -1:
            return "Node not in graph."

        result = []
        queue = deque()
        checkedSet = set()

        queue.append(node)
        checkedSet.add(node)

        while queue and n:

            current = queue.popleft()
            result.append(current.id)

            # getNeighbors returns an array of strings / vertex.id to look up...
            for vertex in current.getNeighbors():
                # look up the index into graph.vertices array based on the vertex's id.
                index = findVertexIndex(vertex)
                # print(index+"hello")
                if index > -1:
                    if graph.vertices[index] not in checkedSet:
                        queue.append(graph.vertices[index])
                        checkedSet.add(graph.vertices[index])
                else:
                    "something's up..."

            n -= 1

        else:
            for leftovers in list(queue):
                result.append(leftovers.id)

        return result



# Challenge: Write a method findPath(self, from_vert, to_vert) in the Graph() class
# that takes in two nodes (from_vert and to_vert) as input, and outputs the list
# of nodes that must be traversed to get from from_vert to to_vert.
# The output list of nodes must be in order of nodes
# visited starting from from_vert and ending at to_vert.
#
# Hint: BFS or it's familiar friend Depth First Search (DFS) could be useful here.
# Again if you need a refresher, here's that Tree Traversals lesson from CS 1.3

    def findPath(self, from_vert, to_vert):
        array = []

        def __helper(curr_vert):
            if curr_vert != None:
                array.append(curr_vert)
            print(curr_vert,to_vert, curr_vert == to_vert)
            if curr_vert == to_vert:
                return array
            for v in self.vertList[curr_vert].getNeighbors():
                return __helper(v)

        if from_vert not in self.vertList:
            return from_vert + "not in Graph."

        if to_vert not in self.vertList:
            return to_vert + "not in Graph."

        return __helper(from_vert)


# Make sure that both nodes from_vert and to_vert are actually in the graph
# Run BFS or DFS starting from from_vert
# Figure out a way to keep track of each path you take
# Once you find to_vert, end the search.
# Since you've been tracking the paths, find the path that goes from from_vert to to_vert
# Return the path, in the order of nodes visited starting with from_vert and ending with to_vert
#
# Optimizing our Path
#
# This works, but what if there are multiple paths between two nodes?
# What if one of those paths is significantly longer than the other?
# Do you know Veronica from high school from your cousin Ricky,
# who went to college with Sarah, who dated Jane, who is friends with Billy,
# who was on the swim team with Veronica? Or do you know Veronica from your friend
# Tom who also is friends with Veronica? In the next chapter,
# we'll learn how to differentiate paths in order to optimize our route.

# Driver code

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

    print("\n stretch challenge for challenge #1")
    print(make_graph_from_file("/Users/jamesmccrory/Documents/dev/CS-2.2-labs/sampleGraphFile.txt"))

    # challenge 2: testing the getNeighbors method.
    print("\nChallenge 2: testing the getNeighbors method:")
    print('testing getNeighbors() method:')
    for v in g.vertList:
        print(v)
        print(g.vertList[v].getNeighbors())

    # challenge 3: breadth first search:
    g.addEdge("Friend 2", "Friend 8") # 1 -> 2 -> 8
    g.addEdge("Friend 3", "Friend 9") # 1 -> 3 -> 9
                                      # 1 -> 2 -> 4
                                      # 1 -> 3 -> 5
    print("\nchallenge 3: breadth first search:")
    print(g.breadth_first_search("Friend 1", 2))

    # challenge 4: DEPTH first search:
    print("\nchallenge 4: DEPTH first search:")
    print(g.findPath("Friend 1", "Friend 7"))
