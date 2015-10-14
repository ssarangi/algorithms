"""
The MIT License (MIT)

Copyright (c) 2015 <Satyajit Sarangi>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import heapq

class Node:
    def __init__(self, order):
        self._parent = None
        self._data = []
        self._children = []
        self._order = order

    def __lt__(self, other):
        return self._data[0] < other.data[0]

    @property
    def order(self):
        return self._order

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, p):
        self._parent = p

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v):
        self._data = v

    @property
    def children(self):
        return self._children

    def add_data(self, v, force_add = False):
        if len(self._children) == 0 or force_add:
            self._data.append(v)
            self._data = sorted(self._data)
            self._children = sorted(self._children)

            if len(self._data) == self._order:
                self._split()
        else:
            child_idx = -1
            # This needs to be added to the children
            for idx, c in enumerate(self._data):
                if ord(v) < ord(c):
                    child_idx = idx
                    break

            if child_idx == -1:
                child_idx = len(self._data)

            self._children[child_idx].add_data(v)

    def _split(self):
        center = int(self._order / 2)
        # Split the nodes to the LHS and the RHS

        # If the parent is not present then the splitting happens
        # differently.
        lhs = Node(self._order)
        rhs = Node(self._order)

        remove_data = []
        for i in range(0, center):
            c = self._data[i]
            lhs.add_data(c)
            remove_data.append(c)

        for i in range(center + 1, len(self._data)):
            c = self._data[i]
            rhs.add_data(c)
            remove_data.append(c)

        for c in remove_data:
            self._data.remove(c)

        for i in range(0, len(self._children)):
            if i < int(len(self._children) / 2):
                lhs.children.append(self._children[i])
            else:
                rhs.children.append(self._children[i])

        if self._parent is not None:
            lhs.parent = self._parent
            rhs.parent = self._parent
            # This needs to be added to its parent
            self._parent.children.append(lhs)
            self._parent.children.append(rhs)
            self._parent.children.remove(self) # Remove the current node since we are adding it to parent
            self._parent.add_data(self._data[0], force_add=True)
        else:
            self._children.clear()
            self._children.append(lhs)
            self._children.append(rhs)
            lhs.parent = self
            rhs.parent = self

    def search(self, data):
        seq = self._data
        min = 0
        max = len(seq) - 1
        while True:
            if max < min:
                return self._children[min].search(data)
            m = (min + max) // 2
            if seq[m] < data:
                min = m + 1
            elif seq[m] > data:
                max = m - 1
            else:
                return self

    def delete(self, node):
        pass

    def __str__(self):
        return str(self._data)

    __repr__ = __str__

def main():
    str = ["A","G","F","B","K","D","H","M","J","E","S","I","R","X","C","L","N","T","U","P"]
    root = Node(5)

    for c in str:
        root.add_data(c)

    search_node = root.search('P')
    print(search_node)


if __name__ == "__main__":
    main()