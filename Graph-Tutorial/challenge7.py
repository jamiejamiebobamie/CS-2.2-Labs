"""
STRETCH : Chapter 7: Long-Distance Friendships

We know you're six degrees away from Kevin Bacon, but who are you the furthest away from?
Not your pen pal in Bhutan (that would still be a neighbor!),
but someone you don't know, and who you in fact know the least!

Graph Diameter

One concept around graph distance that helps us solve this problem is finding
the diameter of a graph. The diameter of a graph is the calculated by finding
the shortest path between every possible pair of nodes, and then selecting the longest of those paths.

Challenge: Write a method diameter(self) that outputs the diameter of the graph

def diameter(self):
# For every node, find the shortest path from it to every other node in the graph and track the paths and their length
# From your list of path/length pairs, pick the one with the largest length and return the length.
Note: The algorithm above will work for small graphs, but takes a lot of time. There are lots of quicker algorithms you can use.

"""
from challenge5 import *

def diameter(graph):
    # intialize return variables
    max_length = float("-inf")
    max_length_nodes = None

    # iterate through all vertices
    # while iterating through all vertices
    # to compare each vertex to the other
    for from_vert in graph.vertices:
        for to_vert in graph.vertices:

    # find the shortest path from_vert to_vert
            if from_vert.id != to_vert.id:
                nodes = find_path(graph, from_vert, to_vert)
        # store the max_length attribute and update the max_length with the length of the 'nodes' array
                store = max_length
                max_length = max(max_length, len(nodes))
        # if the new nodes have the max length store them in 'max_length_nodes'
                if max_length != store:
                    max_length_nodes = nodes

    # once finsihed iterating return the max_length and nodes with the max_length
    return max_length, max_length_nodes

if __name__ == "__main__":
    file = sys.argv[1]

    data = readGraph(file)
    graph = LLGraph(data[0])
    graph.addEdges(data[1])

    diam = diameter(graph)

    print("The diameter of the graph is " + str(diam[0]) + ". And consists of the nodes " + ", ".join(diam[1]))
