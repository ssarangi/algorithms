class Heap:
    def __init__(self):
        self.data = [0]
        
    def push(self, item):
        self.data.append(item)
        self.heapify_up()
        
    def heapify_up(self):
        n = len(self.data) - 1
        cv = self.data[n]
        parent_idx = n // 2
        parent = self.data[parent_idx]
        
        while parent > cv:
            self.data[parent_idx], self.data[n] = self.data[n], self.data[parent_idx]
            n = parent_idx
            parent_idx = n // 2
            parent = self.data[parent_idx]
            
    def get_smaller_child(self, parent):
        left_child_idx = 2 * parent
        right_child_idx = 2 * parent + 1
        
        if left_child_idx >= len(self.data):
            return None
            
        if right_child_idx >= len(self.data):
            return left_child_idx
            
        left_child = self.data[left_child_idx]
        right_child = self.data[right_child_idx]
        
        if left_child < right_child:
            return left_child_idx
        else:
            return right_child_idx

    def heapify_down(self):
        if len(self.data) == 1:
            return
        
        cn = 1
        smaller_child = self.get_smaller_child(1)
        while smaller_child != None and self.data[smaller_child] < self.data[cn]:
            self.data[cn], self.data[smaller_child] = self.data[smaller_child], self.data[cn]
            cn = smaller_child
            smaller_child = self.get_smaller_child(cn)

    def pop(self):
        if len(self.data) > 1:
            v = self.data[1]
            self.data[1] = self.data[len(self.data) - 1]
            self.data.pop()
            print(" ".join([str(i) for i in self.data]))
            self.heapify_down()
            print(" ".join([str(i) for i in self.data]))
            return v
        else:
            raise Exception("No elements in the data")
            
    def empty(self):
        return len(self.data) == 1

heap = Heap()
arr = [5, 1, 2, 9, 10, 4, 6, 8, 11, 20]

for i in arr:
    heap.push(i)

print(heap.data)
while not heap.empty():
    print(heap.pop())