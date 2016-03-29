import heapq
from enum import Enum

class HEAPTYPE(Enum):
    MAX_HEAP = 1
    MIN_HEAP = 2

class PriorityQueue:
    def __init__(self, heap_type):
        self._queue = []
        self.heap_type = heap_type

    def push(self, item, priority = None):
        if priority is None:
            priority = item

        if self.heap_type == HEAPTYPE.MAX_HEAP:
            priority = -priority

        heapq.heappush(self._queue, (priority, item))

    def pop(self):
        return heapq.heappop(self._queue)[1]

    def top(self):
        return heapq.nsmallest(1, self._queue)[0][1]

    def empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

    def __str__(self):
        return str(self._queue)


class StreamingMedian:
    def __init__(self):
        self.min_heap = PriorityQueue(HEAPTYPE.MIN_HEAP)
        self.max_heap = PriorityQueue(HEAPTYPE.MAX_HEAP)

    def add_num(self, n):
        if self.min_heap.empty():
            self.min_heap.push(n)
        else:
            if n > self.min_heap.top():
                self.min_heap.push(n)
            else:
                self.max_heap.push(n)

        if self.min_heap.size() > self.max_heap.size() + 1:
            self.max_heap.push(self.min_heap.pop())
        elif self.max_heap.size() > self.min_heap.size():
            self.min_heap.push(self.max_heap.pop())

        if self.min_heap.size() == self.max_heap.size():
            return 0.5 * (self.min_heap.top() + self.max_heap.top())
        else:
            return self.min_heap.top()

streaming = StreamingMedian()

for i in [1, 0, 3, 5, 2, 0, 1]:
    print(streaming.add_num(i))