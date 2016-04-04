import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_lt = []
        self.data_gt = []
        self.num_data = 0

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.num_data % 2 == 0:
            # Add to the left array
            heapq.heappush(self.data_lt, num)
        else:
            heapq.heappush(self.data_gt, -1 * num)
            
        self.num_data += 1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.num_data % 2 == 0:
            n1 = heapq.heappop(self.data_lt)
            heapq.heappush(self.data_lt, n1)
            n2 = -1 * heapq.heappop(self.data_gt)
            heapq.heappush(self.data_gt, -1 * n2)
            median = (n1 + n2) / 2.0
        else:
            if len(self.data_gt) > 0:
                median = -1 * heapq.heappop(self.data_gt)
                heapq.heappush(self.data_gt, -1 * median)
            else:
                assert len(self.data_lt) == 1
                median = self.data_lt[0]
                
        return float(median)

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