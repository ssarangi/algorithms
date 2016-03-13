import sys
from queue import Queue

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def get_node(self, id):
        for node in self.nodes:
            if node.id == id:
                return node

        return None

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, edge, weight):
        self.edges.append(edge)
        edge.n1.add_neighbor(edge.n2, weight)
        edge.n2.add_neighbor(edge.n1, weight)

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

    def __str__(self):
        return str(self.id)

    __repr__ = __str__

def solve(graph, start_pt):
    num_nodes = graph.num_nodes()
    costs = [-1] * (num_nodes + 1)
    costs[start_pt] = 0
    Q = Queue()
    start_node = graph.get_node(start_pt)
    Q.put(start_node)
    visited = {}

    while not Q.empty():
        node = Q.get()
        if node in visited:
            continue

        visited[node] = True

        current_cost = costs[node.id]
        for neighbor, weight in node.neighbors:
            if neighbor not in visited:
                Q.put(neighbor)
                new_cost = current_cost + weight
                if costs[neighbor.id] == -1 or costs[neighbor.id] > new_cost:
                    costs[neighbor.id] = new_cost

    return costs

def create_graph(rep):
    N = rep[0]
    start_pt = rep[1]
    actual_rep = rep[2]

    nodes = {}
    graph = Graph()
    for i in range(0, N):
        n = Node(i)
        nodes[i] = n
        graph.add_node(n)

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
        graph.add_edge(nedge, 6)

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

        cases.append((N, start_pt, graph))
    return cases

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            test_cases = read(f.readline)
    else:
        test_cases = read(input)

    for test_case in test_cases:
        start_pt, graph = create_graph(test_case)
        costs = solve(graph, start_pt)
        s = ""
        for i, c in enumerate(costs):
            if i != start_pt and i != 0:
                s += str(c) + " "

        print(s)

if __name__ == "__main__":
    main()