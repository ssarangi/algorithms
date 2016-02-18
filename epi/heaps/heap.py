class Heap:
    def __init__(self, comparator):
        self._adt = []
        self._comparator = comparator

    def insert(self, item):
        self._adt.append(item)
        self.heapify_up()

    @staticmethod
    def get_parent(el_idx):
        if el_idx % 2 == 0:
            parent = (el_idx - 2) // 2
        else:
            parent = (el_idx - 1) // 2

        return parent

    @staticmethod
    def get_left_child(parent):
        return 2 * parent + 1

    @staticmethod
    def get_right_child(parent):
        return 2 * parent + 2

    def heapify_up(self):
        # Now heapify the arr by starting with the last element which just got inserted
        last_el = len(self._adt) - 1
        parent = Heap.get_parent(last_el)

        while parent >= 0 and self._comparator(self._adt[last_el], self._adt[parent]):
            self._adt[parent], self._adt[last_el] = self._adt[last_el], self._adt[parent]
            last_el = parent
            parent = Heap.get_parent(last_el)

    def empty(self):
        if len(self._adt) > 0:
            return False

        return True

    def remove_max(self):
        max_el = self._adt[0]

        # Now pick up the last element and put it on the top
        self._adt[0] = self._adt[len(self._adt) - 1]
        self._adt = self._adt[:len(self._adt) - 1]

        top_el_idx = 0
        left_child = Heap.get_left_child(0)
        right_child = Heap.get_right_child(0)

        while left_child < len(self._adt) - 1 and right_child < len(self._adt) - 1:

            if self._comparator(self._adt[left_child], self._adt[top_el_idx]) or self._comparator(self._adt[right_child], self._adt[top_el_idx]):
                # Compare the two children and find out which one it is
                if self._comparator(self._adt[left_child], self._adt[right_child]):
                    gt = left_child
                else:
                    gt = right_child

                if self._comparator(self._adt[gt], self._adt[top_el_idx]):
                    self._adt[gt], self._adt[top_el_idx] = self._adt[top_el_idx], self._adt[gt]
                    top_el_idx = gt
                    left_child = Heap.get_left_child(top_el_idx)
                    right_child = Heap.get_right_child(top_el_idx)
            else:
                break

        return max_el


    def get_max(self):
        return self._adt[0]

    def __str__(self):
        return str(self._adt)

def main():
    arr = [15, 10, 9, 8, 9, 6, 3, 4, 2]

    gt = lambda x, y: x > y
    lt = lambda x, y: x < y

    heap = Heap(lt)
    for item in arr:
        heap.insert(item)

    heap.insert(12)

    while not heap.empty():
        print(heap.remove_max())

if __name__ == "__main__":
    main()
