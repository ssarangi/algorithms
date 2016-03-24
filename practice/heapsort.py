class Heap:
    def __init__(self, comparator, inverse_comparator):
        self.comparator = comparator
        self.inverse_comparator = inverse_comparator
        self.internal = [None]

    def add_element(self, el):
        self.internal.append(el)
        self.heapify_up()

    def is_empty(self):
        return len(self.internal) == 1

    def get_root(self):
        if len(self.internal) == 1:
            raise "Empty Heap"

        return self.internal[1]

    def remove_root(self):
        root = self.get_root()
        self.internal[1] = self.internal[len(self.internal) - 1]
        self.internal.pop()
        self.heapify()
        return root

    def get_child(self, cn):
        cn_1 = 2 * cn
        cn_2 = 2 * cn + 1

        rn = None
        if len(self.internal) > cn_1:
            rn = cn_1

        if len(self.internal) > cn_2:
            if self.comparator(self.internal[cn_1], self.internal[cn_2]):
                rn = cn_1
            else:
                rn = cn_2

        return rn

    def heapify(self):
        perform_heapify = True

        cn = 1
        while perform_heapify:
            child = self.get_child(cn)

            if child is not None and not self.comparator(self.internal[cn], self.internal[child]):
                self.internal[cn], self.internal[child] = self.internal[child], self.internal[cn]
                cn = child
            else:
                perform_heapify = False

    def heapify_up(self):
        perform_heapify = True

        cn = len(self.internal) - 1
        while cn > 0 and perform_heapify:
            parent = cn // 2
            if parent > 0 and not self.inverse_comparator(self.internal[cn], self.internal[parent]):
                self.internal[cn], self.internal[parent] = self.internal[parent], self.internal[cn]
                cn = parent
            else:
                perform_heapify = False

from random import randint

def main():
    arr = [5,2,9,10,15,11,18,12,3,6]

    min_heap = lambda x, y: x < y
    max_heap = lambda x, y: x > y
    heap = Heap(min_heap, max_heap)
    for i in arr:
        heap.add_element(i)

    while not heap.is_empty():
        print(heap.remove_root())


if __name__ == "__main__":
    main()