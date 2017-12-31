# https://leetcode.com/problems/clone-graph/description/

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def __init__(self):
        self.nodes_dict = {}
        self.traversed = set()
        
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        root_node = self.nodes_dict.get(node.label, UndirectedGraphNode(node.label))
        self.nodes_dict[root_node.label] = root_node
        self.traversed.add(root_node)
        for neighbor in root_node.neighbors:
            neighbor_clone = self.cloneGraph(neighbor)
            self.nodes_dict[neighbor_clone.label] = neighbor_clone
            root_node.neighbors.append(neighbor_clone)
        
        return root_node
    
def create_graph(input):
    nodes_dict = {}
    
    # First split the input by #
    nodes = input.split("#")
    
    for connection in nodes:
        connection = connection.split(',')
        node = nodes_dict.get(connection[0], UndirectedGraphNode(connection[0]))
        
        node.neighbors = [nodes_dict.get(connection[i], UndirectedGraphNode(connection[i])) \
                          for i in range(1, len(connection))]
        nodes_dict[connection[0]] = node

    return nodes_dict[input[0]]

def main():
    inp = "0,1,2#1,2#2,2"
    graph = create_graph(input)
    soln = Solution()
    new_graph = soln.cloneGraph(graph)


if __name__ == "__main__":
    main()