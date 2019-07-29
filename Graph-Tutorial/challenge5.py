# Chapter 5: Closest of Friends
#
# If you were trying to show how two people are socially connected,
# you would want to do so in the least number of connections possible.
# Can you imagine if LinkedIn couldn't determine if someone was a 2nd or 20th degree connection?
#
# Shortest Path
#
# In order to solve this problem, we want to find the shortest path between two nodes in a graph.
#
# Challenge 1: Write a function that takes in a graph and two nodes (A and B) as input,
# and outputs the list of nodes that make up the shortest path from A to B.
# The output list of nodes must be in order of nodes visited starting from A and ending at B.
#
# CODE GOES HERE
#
# Make sure that both nodes A and B are actually in the graph
# Run BFS starting from A
# Figure out a way to keep track of each path you take
# Once you find B, end the search.
# Since you've been tracking the paths, find the shortest path that goes from A to B
# Return the shortest path, in the order of nodes visited starting with A and ending with B
# This seems pretty similar to what we did in an earlier chapter, right?
# What if not all edges were of equal connection?
#
# Dijkstra's Algorithm
#
# For a given graph, it may take more work to traverse one edge over another.
# These are show through edge weights, or weighted edges.
# Up until now, all of our edges have had an implicit weight of one (1),
# so they were all equal. But in many cases, weights could be any value.
# Going back to our house example,
# some places are more challenging to walk through than others
# (hills, no sidewalk, a horde of gnomes blocking the path, etc.).
#
# We can't use BFS or DFS anymore to find the shortest path since those two algorithms
# don't take weights into consideration. So what can we use instead?
#
# Dijkstra's Algorithm is a shortest path algorithm that takes weighted edges
# into consideration! From the starting node, the algorithm visits neighbors one
# by one and assigns them a distance value based on the cumulative weights of the
# shortest path to get to that neighbor. Distances are updated if a shorter path
# can be found, and once we're at the target node, we'll know the shortest path to
# get to there. It's like running a more thoughtful BFS!
#
# Note: For the below challenge, you'll be using the weighted graph from the
# starter code, which can be found here
#
# Challenge 2: Write a function that takes in a weighted graph and two nodes
# (A and B) as input, and outputs the shortest path from A to B using Dijkstra's algorithm.
#
# CODE GOES HERE
#
# step by step walkthrough of implementing Dijkstra
# The Long and Short of it is...
#
# Now we can handle the shortest path for both unweighted and weighted graphs!
# Great work! It's great to find the shortest path, but sometimes we want to know
# more about a graph. There's a lot of properties around distance we can measure,
# and we'll dive into another one of them in the next chapter!

"""challenge1

    Challenge 1: Write a function that takes in a graph and two nodes (A and B) as input,
    and outputs the list of nodes that make up the shortest path from A to B.
    The output list of nodes must be in order of nodes visited starting from A and ending at B.

    CODE GOES HERE:

    Please see challenge 4 for this exact problem / solution.

"""

from graph_adt_list import *
from graph_reader import *
import heapq

"""challenge2

# Challenge 2: Write a function that takes in a weighted graph and two nodes
# (A and B) as input, and outputs the shortest path from A to B using Dijkstra's algorithm.
#
# CODE GOES HERE
#
# step by step walkthrough of implementing Dijkstra
# The Long and Short of it is...
"""

filepath = "graph_data.txt"

graph_data = readGraph(filepath)

vertices = graph_data[0]
edges = graph_data[1]

new_graph = LLGraph(vertices)
new_graph.addEdges(edges)

def dijkstra(graph,A,B):

    dist = {}
    dist[A.id] = 0

    priorityQueue = []

    index = graph.findVertexIndex(A.id)

    for v in graph.vertices:
        if v.id != A.id:
            dist[v.id] = float('inf')
            # print(dist)
            # i = graph.findVertexIndex(v)
            # node = graph.vertices[i]
            priorityQueue.append(v)
            print(priorityQueue)
    heapq.heappush(priorityQueue, v)

    while priorityQueue:
        pass

dijkstra(new_graph, new_graph.vertices[0], new_graph.vertices[3])
