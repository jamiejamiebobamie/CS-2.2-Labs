# Chapter 4: Friends Along the Way
#
# There's this idea of six degrees of separation: take two people in the world,
# and they are at most six social connections away from each other.
# You may be more familiar with the Six Degrees of Kevin Bacon as an example of this.
#
# kevin bacon
#
# Source: MisterDressup
#
# You may not know Kevin Bacon (or do you?),
# but we can still apply this to our graph of friends to find the connections that
# create a chain between two people. This is an application of path finding
#
# Finding the Path
#
# Think of a graph as a neighborhood, each house as a node, and immediate neighbors
# as nodes that share an edge. If you wanted to figure out how to get from one house to another,
# you'd walk to that house, passing other houses along the way. You'd be walking a path,
# walking from one node to another via edges!
#
# Challenge: Write a function that takes in a graph and two nodes (A and B) as input,
# and outputs the list of nodes that must be traversed to get from A to B.
# The output list of nodes must be in order of nodes visited starting from A and ending at B.
#
# Hint: BFS or it's familiar friend Depth First Search (DFS) could be useful here.
# Again if you need a refresher, here's that Tree Traversals lesson from CS 1.3
#
# CODE GOES HERE
#
# Make sure that both nodes A and B are actually in the graph
# Run BFS or DFS starting from A
# Figure out a way to keep track of each path you take
# Once you find B, end the search.
# Since you've been tracking the paths, find the path that goes from A to B
# Return the path, in the order of nodes visited starting with A and ending with B
# Optimizing our Path
#
# This works, but what if there are multiple paths between two nodes?
# What if one of those paths is significantly longer than the other?
# Do you know Veronica from high school from your cousin Ricky,
# who went to college with Sarah, who dated Jane, who is friends with Billy,
# who was on the swim team with Veronica? Or do you know Veronica from your friend
# Tom who also is friends with Veronica? In the next chapter,
# we'll learn how to differentiate paths in order to optimize our route.


from graph_adt_list import *
from graph_reader import *
from collections import deque

# if tests need to be written...

# filepath = "sampleGraphFile.txt"
# graph_data = readGraph(filepath)

# vertices = graph_data[0]
# edges = graph_data[1]

# new_graph = LLGraph(vertices)
# new_graph.addEdges(edges)


def find_path(graph, nodeA, nodeB):
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
    nodeA_index = findVertexIndex(nodeA.id)
    nodeB_index = findVertexIndex(nodeB.id)

    if not nodeA_index > -1:
        return nodeA.id + " not in graph."

    if not nodeB_index > -1:
        return nodeB.id + " not in graph."

    result = []
    queue = deque()
    checkedSet = set()

    queue.append(nodeA)
    checkedSet.add(nodeA)

    while queue:

        current = queue.popleft()
        result.append(current.id)

        # getNeighbors returns an array of strings / vertex.id to look up...
        for vertex in current.getNeighbors():
            # look up the index into graph.vertices array based on the vertex's id.
            index = findVertexIndex(vertex)
            if index > -1:
                if graph.vertices[index] == nodeB:
                    result.append(graph.vertices[index].id)
                    return result
                elif graph.vertices[index] not in checkedSet:
                    queue.append(graph.vertices[index])
                    checkedSet.add(graph.vertices[index])
            else:
                return "something's up..." # these are here for control flow / edge cases. at no point should the program reach this point in the code, but if it does...
    else:
        for leftovers in list(queue):
            result.append(leftovers.id)

    return "I have no idea..." # these are here for control flow / edge cases. at no point should the program reach this point in the code, but if it does...


# print(find_path(new_graph, new_graph.vertices[0], new_graph.vertices[3]))
