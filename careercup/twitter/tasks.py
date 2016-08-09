import unittest

def schedule(task_list, k):
    cycle = 0
    task_hash = {}
    scheduling = []
    for task in task_list:
        if task in task_hash:
            while cycle - (task_hash[task] + k) <= 0:
                cycle += 1
                scheduling.append('.')
            
        scheduling.append(task)
        task_hash[task] = cycle
        cycle += 1
    
    print(scheduling)
    return scheduling

class UnitTest(unittest.TestCase):
    def testTaskScheduling(self):
        self.assertEqual(schedule(['A', 'B', 'C', 'D'], 3), ['A', 'B', 'C', 'D'])
        self.assertEqual(schedule(['A', 'B', 'A', 'D'], 3), ['A', 'B', '.', '.', 'A', 'D'])
        self.assertEqual(schedule(['A', 'A', 'A', 'A'], 3), ['A', '.', '.', '.', 'A', '.', '.', '.', 'A', '.', '.', '.', 'A'])
        self.assertEqual(schedule(['A', 'B', 'C', 'A', 'C', 'B', 'D', 'A'], 4), ['A', 'B', 'C', '.', '.', 'A', '.', 'C', 'B', 'D', 'A'])
    
if __name__ == "__main__":
    unittest.main()