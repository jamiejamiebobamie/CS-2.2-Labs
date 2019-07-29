#
# Chapter 3: Breadth of Fresh Neighbors
#
# How does Facebook or LinkedIn know what friends to recommend to you?
# They look at who your friends are friends with, and who their friends are friends with, and so on two friends
#
# Source: Giphy
#
# Friends of Friends
#
# The function you just wrote is great for finding your immediate friends,
# but what if we want to see their friend's friends?
#
# Think back to CS 1.3: what's an algorithm at your disposal we could use here?
#
# Since we want to find all friends at a certain connection level away
# (friend's friend would be 2 connections from you),
# this sounds like a perfect application of Breadth First Search (BFS).
# Check out the Tree Traversals lesson from CS 1.3 if you want a refresher.
#
# Challenge: Write a function that takes in a graph, a node, and n (an integer) as input,
# and outputs all nodes that are n connections away from the input node.
#
# CODE GOES HERE
#
# Make sure the input node is actually in the graph
# Run BFS starting from the input node and going n levels deep
# Return all nodes found at the nth level
# A More Granular Approach
#
# Great application of BFS! But as with anything related to BFS,
# specificity isn't a strong suite.
# Having all of your 3rd, 4th, 5th degree connections is daunting.
# What if we just want to see how two specific people are connected?
# We'll solve this in the next chapter!

from graph_adt_list import *
from graph_reader import *
from collections import deque

# if tests need to be written...

# filepath = "sampleGraphFile.txt"
# graph_data = readGraph(filepath)
#
#
# vertices = graph_data[0]
# edges = graph_data[1]
#
# print(edges)
#
#
# new_graph = LLGraph(vertices)
# new_graph.addEdges(edges)
# print(graph_data)
# print(new_graph.__iter__())


def breadth_first_search(graph, node, n=1):
    """
    This method assumes you want the vertex ids of all vertices that are less than the input n.
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

# print(breadth_first_search(new_graph, new_graph.vertices[0], n=1))
