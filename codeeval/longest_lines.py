# https://www.codeeval.com/open_challenges/2/submit/

import sys
from queue import PriorityQueue

with open(sys.argv[1], 'r') as test_cases:
    lines = []
    n = 0
    pq = PriorityQueue()
    for i, test in enumerate(test_cases):
        # ignore test if it is an empty line
        # 'test' represents the test case, do something with it
        # ...
        # ...
        if i == 0:
            n = int(test)
        else:
            test = test.replace("\n", "")
            lines.append(test)
            length = len(test)
            pq.put((-length, i - 1))

    i = 0
    while i < n and not pq.empty():
        length, lineno = pq.get()
        line = lines[lineno]
        print(line)
        i += 1