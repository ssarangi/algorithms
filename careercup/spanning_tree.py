class Node:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.neighbors = set()

    def add_neighbor(self, node):
        self.neighbors.add(node)

class Graph:
    def add_edge(self, n1, n2):
        n1.add_neighbor(n2)
        n2.add_neighbor(n1)

RED = 0
BLACK = 1

A = Node('A', BLACK)
B = Node('B', RED)
C = Node('C', RED)
D = Node('D', BLACK)
E = Node('E', BLACK)
F = Node('F', RED)

graph = Graph()
graph.add_edge(A, B)
graph.add_edge(A, C)
graph.add_edge(A, D)
graph.add_edge(A, E)
graph.add_edge(A, F)
graph.add_edge(B, C)
graph.add_edge(B, D)
graph.add_edge(B, E)
graph.add_edge(B, F)
graph.add_edge(C, D)
graph.add_edge(C, E)
graph.add_edge(C, F)
graph.add_edge(D, E)
graph.add_edge(D, F)
graph.add_edge(E, F)

from queue import Queue

# Now that the graph is created.
def spanning_tree(node, paths):
    
    for neighbor in node.neighbors:
        if node.color != neighbor.color:
            tmp_path = [p for p in paths]
            spanning_tree(neighbor, tmp_path)


spanning_tree(graph, A)