# Chapter 2: Won't you Be My Neighbor?
#
# Have you ever had that moment where you find out a friend knows another one of your friends?
# Having one of those "worlds collide" moments can be exciting, scary, or a whole mixture of emotions.
# Instead of having that situation surprise us, what if we had a way to look know this information. in advanced?
#
# Find Your Neighbors
#
# Turns out we do!
# We can utilize a neighbor lookup for a given node in our graph to see what other nodes it is connected with.
# If you and a friend are connected, you two share a friendship. How do we know if two nodes are connected? They share an edge!
#
# Challenge: Write a function that takes in a graph and a node as input, and outputs all nodes connected to the input node.
#
# CODE GOES HERE
#
# Make sure the input node is actually in the graph
# Find all edges for the input node
# See what nodes are connected to the input node via the edge
# return the connected nodes
# Down The Friend Chain We Go
#
# Alright, no more surprise connections for us! But what if we want to go even further than one connection? Onward!

from graph_adt_list import *

def neighborLookup(graph, node):
    """
        graph == graph class, list implementation

        node == linkedlist object

        a node in a graph (both a list and AM implementation) is an entry into an array.
        using a list implementation, the entires are linkedlist objects.

        this function makes the assumption that you are inputting a linkedlist object for the node argument
        and not an index into the vertex array.
    """
        # intialize index to 1
        # as the getNeighborsOfAVertex method takes in a number
        # between 1 and the number of vertices in the graph
        index = 1
        for i, v in enumerate(graph.vertices):
            if v == node:
                index += i

        return graph.getNeighborsOfAVertex(index)
