
"""
Chapter 6: Find your friend group

Find “cliques” of friends (small groups of tightly-connected users), etc…

The clique problem is a popular computational problem in computer science.

Clique Discovery

Among other applications, the clique problem can arise in a social network.
With our social network, a clique will represent a subset of people (nodes)
who all know each other (share edges), and we can use various algorithms to find these cliques.

Challenge: Write a method clique(self) that finds a clique in a graph that
cannot have any other vertices added to it (note this is called a maximal clique).

def clique(self):
#
Start with an arbitrary vertex u and add it to the clique

For v in remaining vertices not in the clique
If v is adjacent to every other vertex already in the clique.
	Add v to the clique
	Discard v otherwise
"""

from graph_adt_list import *
from graph_reader import *
import random

def clique(graph):
    """finds a clique in a graph that
        cannot have any other vertices added to it (note this is called a maximal clique).
        Starts with an arbitrary vertex u and adds it to the clique

        For v in remaining vertices not in the clique
        If v is adjacent to every other vertex already in the clique.
        	Add v to the clique
        	Discard v otherwise
    """
    remainingVertices = graph.vertices.copy()
    randomInt = random.randint(0,len(remainingVertices)-1)
    startingVert = remainingVertices.pop(randomInt)
    friend_group = [startingVert.id]

    while remainingVertices:

        randomInt = random.randint(0, len(remainingVertices)-1)
        candidate = remainingVertices.pop(randomInt)
        testInclusion = True
        candidate_neighbors = candidate.getNeighbors()

        # iterate through each person in the clique
        # if the friend is not candidate's adjacent neighbors
        # set the boolean 'testInclusion' to False
        # and do not add the candidate to the friend group.
        for friend in friend_group:
            if friend not in candidate_neighbors:
                testInclusion = False
        if testInclusion:
            friend_group.append(candidate.id)
            
    return startingVert, friend_group

if __name__ == "__main__":
    file = sys.argv[1]

    data = readGraph(file)
    graph = LLGraph(data[0])
    graph.addEdges(data[1])

    friend_group = clique(graph)
    print("starting at " + friend_group[0].id + " the found clique consists of " + ", ".join(friend_group[1]))
