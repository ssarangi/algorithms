# https://www.codeeval.com/open_challenges/229/

import sys
from queue import PriorityQueue

def reconstruct_path(came_from, start, end):
    current = end
    path = [current]
    while current is not None and current != start:
        if current not in came_from:
            return path
        current = came_from[current]
        path.append(current)
        
    path.reverse()
    return path

def dijkstra(nodes, start, end):
    neighbors = {}
    for node in nodes:
        n1, n2, length = node[0], node[1], node[2]
        if n1 not in neighbors:
            neighbors[n1] = [(n2, length)]
        else:
            neighbors[n1].append((n2, length))
    
        if n2 not in neighbors:
            neighbors[n2] = [(n1, length)]
        else:
            neighbors[n2].append((n1, length))
            
    if start not in neighbors:
        return "False"
    
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {}
    cost_so_far = {}
    cost_so_far[start] = 0
    came_from[start] = None
    paths_considered = []
    
    while not pq.empty():
        c, current = pq.get()
        
        if current == end:
            break
        
        for neighbor, cost in neighbors[current]:
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                pq.put((new_cost, neighbor))
                came_from[neighbor] = current
                paths_considered.append((current, neighbor))
    
    path = reconstruct_path(came_from, start, end)
    
    if len(path) < 2:
        return "False"
        
    return cost_so_far[end]

with open(sys.argv[1], 'r') as test_cases:
    for idx, test in enumerate(test_cases):
        nodes, start_end = test.split("|")
        nodes = nodes.strip()
        start_end = start_end.strip()
        
        start, end = start_end.split(" ")
        start = int(start)
        end = int(end)
        
        nodes = nodes.split(",")
        nodelist = []
        for node in nodes:
            node = node.strip()
            n1, n2, length = node.split(" ")
            n1 = int(n1)
            n2 = int(n2)
            length = int(length)
            nodelist.append((n1, n2, length))
        
        shortest_path = dijkstra(nodelist, start, end)
        print(shortest_path)