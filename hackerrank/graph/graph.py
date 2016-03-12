class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, edge, weight):
        self.edges.append(edge)
        self.nodes.add(edge.n1)
        edge.n1.add_neighbor(edge.n2, weight)
        self.nodes.add(edge.n2)

    def num_nodes(self):
        return len(self.nodes)

class Edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def opposite(self, node):
        if self.n1 == node:
            return self.n2
        elif self.n2 == node:
            return self.n1
        else:
            raise Exception("Cannot find the required Node")

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = set()

    def add_neighbor(self, node, weight):
        self.neighbors.add((node, weight))