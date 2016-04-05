class Heap:
    def __init__(self):
        self.data = [0]
        
    def push(self, item):
        self.data.append(item)
        self.heapify_up()
        print(self.data)
        
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

    def get_bigger_child(self, parent):
        left_child_idx = 2 * parent + 1
        right_child_idx = 2 * parent + 2
        
        if left_child_idx >= len(self.data):
            return None
            
        if right_child_idx >= len(self.data):
            return left_child_idx
            
        left_child = self.data[left_child_idx]
        right_child = self.data[right_child_idx]
        
        if left_child > right_child:
            return left_child_idx
        else:
            return right_child_idx

    def heapify_down(self):
        if len(self.data) == 1:
            return
        
        cn = 1
        bigger_child = self.get_bigger_child(1)
        print("Bigger Child: %s" % self.data[bigger_child])
        while bigger_child == None and self.data[bigger_child] < self.data[cn]:
            self.data[cn], self.data[bigger_child] = self.data[bigger_child], self.data[cn]
            cn = bigger_child
            bigger_child = self.get_bigger_child(cn)
            print("Bigger Child: %s" % self.data[bigger_child])

    def pop(self):
        if len(self.data) > 1:
            v = self.data[1]
            self.data[1] = self.data[len(self.data) - 1]
            self.data.pop()
            self.heapify_down()
            return v
        else:
            raise Exception("No elements in the data")
            
    def empty(self):
        return len(self.data) == 1

heap = Heap()

heap.push(5)
heap.push(8)
heap.push(2)
heap.push(1)
heap.push(10)
heap.push(9)
heap.push(15)


while not heap.empty():
    print(heap.pop())