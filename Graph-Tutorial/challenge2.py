

from graph_adt_list import *
from graph_reader import *


def neighborLookup(graph, node):
    """
        graph == graph class, linked list implementation

        node == linkedlist object to find neghbors for / of

        this method calls the graph method getNeighborsOfAVertex(vertexId)
        which checks if the vertexId is in the graph's vertices and if it is
        calls the vertex method getNeighbors() which iterates through the linked list and returns the nodes' data
    """
    return graph.getNeighborsOfAVertex(node.id)



if __name__ == "__main__":
    file = sys.argv[1]
    nodeId = sys.argv[2]
    node = None

    nodesInGraph = []

    data = readGraph(file)
    graph = LLGraph(data[0])
    graph.addEdges(data[1])

    for v in graph.vertices:
        nodesInGraph.append(v.id)
        if v.id == nodeId:
            node = v

    if not node:
        print("The node you are looking for is not in this graph. Requested node: " + nodeId + ".\nThe nodes in the graph are: " + ", ".join(nodesInGraph))
    else:
        print("The neighbors of " + nodeId + " are " + ", ".join(neighborLookup(graph, node)))
