
from graph_adt_list import *
from graph_reader import *
from collections import deque

def breadth_first_search(graph, node, n=1):
    """
    This method assumes you want the vertex ids of all vertices that are less than the input n.
    """

    def findVertexIndex(vertex_id):
        """
        vertex_id argument is a string
        returns the vertices index in the graph if present
        otherwise returns -1, out of bounds
        """
        for i, v in enumerate(graph.vertices):
            if int(v.id) == int(vertex_id):
                return i
        return -1

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


if __name__ == "__main__":
    file = sys.argv[1]
    nodeId = sys.argv[2]
    n = int(sys.argv[3])


    data = readGraph(file)
    graph = LLGraph(data[0])
    graph.addEdges(data[1])

    node = None
    nodesInGraph = []
    for v in graph.vertices:
        nodesInGraph.append(v.id)
        if v.id == nodeId:
            node = v

    if not node:
        print("The node you are looking for is not in this graph. Requested node: " + nodeId + ".\nThe nodes in the graph are: " + ", ".join(nodesInGraph))
    else:
        print("The friends of " + nodeId + " are " + ", ".join(breadth_first_search(graph, node, n)))
