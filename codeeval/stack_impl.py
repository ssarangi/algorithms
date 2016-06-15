# https://www.codeeval.com/open_challenges/9/

import sys

class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, val):
        self.data.append(val)
        
    def pop(self):
        assert len(self.data) > 0
        
        v = self.data.pop()
        return v
        
    def empty(self):
        return len(self.data) == 0

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        num_list = [int(i) for i in test.split(" ")]
        s = Stack()
        
        for num in num_list:
            s.push(num)
            
        # Now pop every alternate element
        i = 0
        while not s.empty():
            v = s.pop()
            
            if i % 2 == 0:
                print(v, end=" ")
            
            i += 1
        print("")