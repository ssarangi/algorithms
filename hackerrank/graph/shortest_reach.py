import sys
from queue import Queue

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

def solve(graph, start_pt):
    num_nodes = graph.num_nodes()
    costs = [-1] * num_nodes
    Q = Queue()

    while not Q.empty():
        node = Q.get()


def create_graph(rep):
    start_pt = rep[0]
    actual_rep = rep[1]

    graph = Graph()
    nodes = {}
    for edge in actual_rep:
        n1 = edge[0]
        n2 = edge[1]
        if n1 in nodes:
            n1 = nodes[n1]
        else:
            nn1 = Node(n1)
            nodes[n1] = nn1
            n1 = nn1

        if n2 in nodes:
            n2 = nodes[n2]
        else:
            nn2 = Node(n2)
            nodes[n2] = nn2
            n2 = nn2

        nedge = Edge(n1, n2)
        graph.add_edge(nedge)

    return start_pt, graph

def read(read_fn):
    T = int(read_fn())
    cases = []
    for i in range(0, T):
        line = read_fn().split()
        N, M = int(line[0]), int(line[1])
        graph = []
        for j in range(0, M):
            line = read_fn().split()
            x, y = int(line[0]), int(line[1])
            graph.append((x, y))
        start_pt = int(read_fn())

        cases.append((start_pt, graph))
    return cases

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            test_cases = read(f.readline)
    else:
        test_cases = read(input)

    for test_case in test_cases:
        start_pt, graph = create_graph(test_case)
        solve(graph, start_pt)


if __name__ == "__main__":
    main()