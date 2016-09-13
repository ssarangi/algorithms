def unique_routes(rows, cols):
    grid = [[0] * cols for _ in range(0, rows)]
    
    for i in range(0, cols):
        grid[0][i] = 1
    
    for i in range(0, rows):
        grid[i][0] = 1
        
    for x in range(1, cols):
        for y in range(1, rows):
            grid[y][x] = grid[y-1][x] + grid[y][x-1]
    
    return grid[rows-1][cols-1]

import unittest

class UnitTest(unittest.TestCase):
    def testUniqueRoutes(self):
        self.assertEqual(unique_routes(4, 5), 35)
        self.assertEqual(unique_routes(1, 2), 1)
        self.assertEqual(unique_routes(1, 1), 1)
        self.assertEqual(unique_routes(7, 7), 924)
        self.assertEqual(unique_routes(5, 2), 5)
        

if __name__ == "__main__":
    unittest.main()