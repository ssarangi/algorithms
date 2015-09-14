__author__ = 'sarangis'

'''
Given a set of vertices V that describes a path in a graph, with each vertex assigned a weight. Find a subset of V that
maximizes the sum of vertex weights without any two vertices in that subset being adjacent.

https://www.mapbox.com/jobs/directions-developer/
'''

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation.independent_set import *

class Node:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return self.__name

    __repr__ = __str__

def render_graph(graph):
    plt.subplots()
    nx.draw_networkx(graph, with_labels=True)
    plt.show()

def create_graph():
    A = Node('A', 3)
    B = Node('B', 4)
    C = Node('C', 5)
    D = Node('D', 1)
    E = Node('E', 2)
    F = Node('F', 9)
    G = Node('G', 10)
    H = Node('H', 11)
    I = Node('I', 6)
    J = Node('J', 7)

    nodes = [A, B, C, D, E, F, G, H, I, J]

    edges = [(A, B),
             (A, F),
             (B, D),
             (B, C),
             (C, D),
             (D, I),
             (C, I),
             (D, E),
             (I, E),
             (I, H),
             (I, J),
             (H, J),
             (E, H),
             (E, G),
             (E, F),
             (E, D),
             (G, F),
             (G, H)]

    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    return g, nodes

def old_main():
    g, nodes = create_graph()
    # for node in nodes:
    #     print(str(node) + " --> " + str(g.neighbors(node)))

    print(maximum_independent_set(g))

def create_path(weights):
    soln = []
    i = len(weights) - 1
    while i > 0:
        if i > 0 and weights[i] > weights[i-1]:
            soln.append(i)
            i -= 1
        elif i == 0:
            soln.append(i)

        i -= 1

    return soln

def create_solution(weights):
    for i in range(2, len(weights)):
        if weights[i] + weights[i-2] > weights[i-1]:
            weights[i] += weights[i - 2]
        elif i > 2 and weights[i] + weights[i - 3] > weights[i - 1]:
            weights[i] += weights[i - 3]

    soln = create_path(weights).reverse()
    return weights, soln


def main():
    weights = [0, 3, 3, 4, 5, 6, 7, 1]
    new_weights, soln = create_solution(weights)
    print(new_weights)
    print(soln)

if __name__ == "__main__":
    main()