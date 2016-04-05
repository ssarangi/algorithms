import heapq

MIN_HEAP = 1
MAX_HEAP = -1

class PriorityQueue:
    def __init__(self, heap_type):
        self.heap_type = heap_type
        self.queue = []

    def push(self, item, priority = None):
        if priority is None:
            sign = 0
            if self.heap_type == MIN_HEAP:
                sign = 1
            else:
                sign = -1
            priority = sign * item

        heapq.heappush(self.queue, (priority, item))

    def pop(self):
        return heapq.heappop(self.queue)[1]

    def top(self):
        v = heapq.heappop(self.queue)
        heapq.heappush(self.queue, v)
        return v[1]

    def empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap = PriorityQueue(MIN_HEAP)
        self.max_heap = PriorityQueue(MAX_HEAP)

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # If the min heap is empty then add it to min heap
        if self.min_heap.size() == 0:
            self.min_heap.push(num)
        else:
            if num >= self.min_heap.top():
                self.min_heap.push(num)
            else:
                self.max_heap.push(num)

        if self.min_heap.size() > self.max_heap.size() + 1:
            self.max_heap.push(self.min_heap.pop())
        elif self.max_heap.size() > self.min_heap.size() + 1:
            self.min_heap.push(self.max_heap.pop())

            
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.min_heap.size() == self.max_heap.size():
            return 0.5 * (self.min_heap.top() + self.max_heap.top())
        elif self.min_heap.size() > self.max_heap.size():
            return self.min_heap.top()
        else:
            return self.max_heap.top()

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()

mf.addNum(-1)
print(mf.findMedian())
mf.addNum(-2)
print(mf.findMedian())
mf.addNum(-3)
print(mf.findMedian())
mf.addNum(-4)
print(mf.findMedian())
mf.addNum(-5)
print(mf.findMedian())