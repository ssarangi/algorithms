class TreeNode:
    def __init__(self, intervals):
        self.intervals = []
        self.left = None
        self.right = None
        
        sum_all = 0
        for i in intervals:
            sum_all += i[0] + i[1]
        
        self.split_point = sum_all / (len(intervals) * 2)
        
        left_child_intervals = []
        right_child_intervals = []
        
        for i in intervals:
            if i[1] < self.split_point:
                left_child_intervals.append(i)
                
            elif i[0] > self.split_point:
                right_child_intervals.append(i)
        
            else:
                self.intervals.append(i)
        
        if len(left_child_intervals) > 0:
            self.left = TreeNode(left_child_intervals)
            
        if len(right_child_intervals) > 0:
            self.right = TreeNode(right_child_intervals)
        
    def search_query(self, coord, result_intervals):
        for interval in self.intervals:
            if coord >= interval[0] and coord <= interval[1]:
                result_intervals.append(interval)
        
        if self.right is not None and coord > self.split_point:
            self.right.search_query(coord, result_intervals)
        elif self.left is not None and coord < self.split_point:
            self.left.search_query(coord, result_intervals)
                        
        
def main():
    inp = [[2, 4], [1, 5], [6, 21], [20, 30]]
    
    root = TreeNode(inp)
    
    result_query = []
    coord = 20.5
    root.search_query(20.5, result_query)
    
    print(result_query)
    
if __name__ == "__main__":
    main()
        
# 
# Your previous C++ content is preserved below:
# 
# 
# [2,4] [1,5]  [6,21] [20,30]
# (2+4+1+5+6+21+20+30)/8 = 11.125
# 
#       R:10 [6,21]
#       /         \
# LC:[1,5],[2,4]  RC:25 [20,30]
#                  /       \
#             RLC:[...]   RRC: [31, 32]
