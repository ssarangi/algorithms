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

"""
Given two words (start and end), and a dictionary, find the length of shortest
transformation sequence from start to end, such that only one letter can be changed
at a time and each intermediate word must exist in the dictionary. For example, given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", the program
should return its length 5.
"""

""" IMPLEMENT WITH GRAPH """

from program_creek.utils import Stack
import string

class Node:
    def __init__(self, data, parent, transformations):
        self._data = data
        self._children = []
        self._parent = parent
        self._transformations = transformations

    @property
    def parent(self):
        return self._parent

    @property
    def transformations(self):
        return self._transformations

    @property
    def data(self):
        return self._data

    @property
    def children(self):
        return self._children

    def __str__(self):
        return self._data

    __repr__ = __str__


def shortest_transformation(start, end, dict):
    assert(len(start) == len(end))

    dict.append(end)

    root = Node(start, None, 1)
    stack = Stack()
    stack.push(root)

    char_list = []

    for i in range(0, len(start)):
        char_list.append(set([word[i] for word in dict]))

    added_to_stack = [start]

    while not stack.empty():
        top = stack.pop()
        original_str = top.data
        num_transformations = top.transformations + 1

        for i in range(0, len(original_str)):
            for c in char_list[i]:
                new_str = original_str
                new_str = new_str.replace(new_str[i], c)

                if new_str == original_str:
                    continue

                if new_str == end:
                    # figure out the transformations
                    transformations = [new_str]
                    node = top
                    while node.parent is not None:
                        transformations.append(node.data)
                        node = node.parent

                    transformations.append(start)
                    transformations.reverse()
                    print(" --> ".join(transformations))
                    return num_transformations

                if new_str in dict:
                    if new_str not in added_to_stack:
                        n = Node(new_str, top, num_transformations)
                        stack.push(n)
                        added_to_stack.append(new_str)
    return 0, []

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(shortest_transformation("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 5)

if __name__ == "__main__":
    # unittest.main()
    print(shortest_transformation("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    print(shortest_transformation("dog", "him", ["dam","dat", "ham", "dag"]))