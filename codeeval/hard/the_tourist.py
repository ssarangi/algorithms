# Floyd Warshall Algorithm: Use this to find all the shortest paths for all nodes
# https://compprog.wordpress.com/2007/11/15/all-sources-shortest-path-the-floyd-warshall-algorithm/
import sys

class Node:
    def __init__(self, id):
        self.id = id

class Edge:
    def __init__(self, n1, n2, length):
        self.n1 = n1
        self.n2 = n2
        self.length = length
        
class Graph:
    def __init__(self):
        self.edges = []
        self.nodes = set()
        self.max_node_id = 0

def create_adjacency_matrix(graph):
    num_nodes = graph.max_node_id + 1
    adj_matrix = [[sys.maxsize] * num_nodes for i in range(0, num_nodes)]
    
    for edge in graph.edges:
        adj_matrix[edge.n1.id][edge.n2.id] = edge.length
        adj_matrix[edge.n2.id][edge.n1.id] = edge.length

    return adj_matrix
    
def does_path_exist(path, adj_matrix, start, end):
    if path[start][end] is -1:
        return []
    
    total_path = 0
    newpath = [start]
    while start != end:
        total_path += adj_matrix[start][path[start][end]]
        start = path[start][end]
        newpath.append(start)
        
    if len(newpath) != (end - start):
        newpath = []

    return total_path, newpath

def floyd_warshall(graph, adj_matrix):
    num_nodes = len(adj_matrix)
    path = [[-1] * num_nodes for i in range(0, num_nodes)]
    
    for i in range(0, num_nodes):
        for j in range(0, num_nodes):
            if adj_matrix[i][j] != sys.maxsize and i != j:
                path[i][j] = j
            else:
                path[i][j] = -1
    
    for k in range(1, num_nodes):
        for i in range(1, num_nodes):
            for j in range(1, num_nodes):
                if adj_matrix[i][k] + adj_matrix[k][j] < adj_matrix[i][j]:
                    adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
                    path[i][j] = path[i][k]

    # Now find if there is a path between the first and last node and if it
    # touches all the nodes in between or not.
    return path

def create_graph(test):
    # Split the input string with "|"
    splitted = test.split("|")
    graph = Graph()
    
    g_nodes = {}
    for path in splitted:
        nodes = path.split(" ")
        nodes = [int(i) for i in nodes if i != ""]

        id0 = int(nodes[0])
        id1 = int(nodes[1])

        graph.max_node_id = max(graph.max_node_id, id0, id1)

        length = int(nodes[2])
        
        if id0 not in g_nodes:
            node1 = Node(id0)
        else:
            node1 = g_nodes[id0]
            
        if id1 not in g_nodes:
            node2 = Node(id1)
        else:
            node2 = g_nodes[id1]

        g_nodes[id0] = node1
        g_nodes[id1] = node2
        
        edge = Edge(node1, node2, length)
        graph.edges.append(edge)
        graph.nodes.add(node1)
        graph.nodes.add(node2)

    return graph

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        graph = create_graph(test)
        adj_matrix = create_adjacency_matrix(graph)
        path = floyd_warshall(graph, adj_matrix)
        
        # Find the minimum path from 1 to every other node
        total_path_length = 0
        invalid_length = False
        for i in range(1, len(graph.nodes)):
            if adj_matrix[i][i+1] == sys.maxsize:
                invalid_length = True
                break
            
            total_path_length += adj_matrix[i][i+1]
        
        if invalid_length:
            print("False")
        else:
            print(total_path_length)