import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        
    def top(self, heap):
        val = heapq.heappop(heap)
        heapq.heappush(heap, val)
        return val

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # If the min heap is empty then add it to min heap
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)
        else:
            if num > self.top(self.min_heap):
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, num)
                
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.push(self.max_heap, heapq.pop(self.min_heap))
        else:
            heapq.heappush(self.min_heap, heapq.heappop(self.max_heap))
            
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return 0.5 * (heapq.heappop(self.min_heap), heapq.heappop(self.max_heap))
        else:
            return heapq.heappop(self.min_heap)

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()

mf.addNum(-1)
mf.findMedian()
mf.addNum(-2)
mf.findMedian()
mf.addNum(-3)
mf.findMedian()
mf.addNum(-4)
mf.findMedian()
mf.addNum(-5)
mf.findMedian()