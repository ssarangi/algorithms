# https://www.codeeval.com/open_challenges/218/submit/

import sys

def num_squares(size, connections):
    grid = [[0] * size for _ in range(0, size)]
    
    for connection in connections:
        grid[connection[0]][connection[1]] = 1
        grid[connection[1]][connection[0]] = 1
        
    

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        sconnections = test.split("|")
        connections = []
        for connection in sconnections:
            connection = connection.strip()
            connection = connection.split(" ")
            
            connection = [int(i) for i in connection]
            connections.append(connection)
        
        print(connections)
        num_squares(60, connections)