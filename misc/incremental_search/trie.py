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

from misc.incremental_search.utils import *

class Node:
    def __init__(self, char, parent):
        self._char = char
        self._child_nodes = [None] * 26
        self._parent = parent
        self._is_end = False

    @property
    def is_end(self):
        return self._is_end

    @is_end.setter
    def is_end(self, v):
        self._is_end = v

    @property
    def parent(self):
        return self._parent

    @property
    def char(self):
        return self._char

    @property
    def children(self):
        return self._child_nodes

    def __str__(self):
        return self._char

    __repr__ = __str__


class Trie:
    def __init__(self):
        self._root = []
        for i in range(0, 26):
            self._root.append(Node(chr(i + ord('a')), None))

    @property
    def root(self):
        return self._root

    def _insert(self, word):
        nodes = self._root
        parent = None
        current_node = None
        for c in word:
            ascii = get_ascii(c)
            current_node = nodes[ascii]

            if current_node == None:
                current_node = Node(c, parent)
                nodes[ascii] = current_node

            nodes = current_node.children
            parent = current_node

        current_node.is_end = True

    def insert(self, word):
        self._insert(word)

    def create(self, words):
        for word in words:
            self._insert(word)

    def _get_suffixes(self, node, result, curr_string):
        is_leaf = True
        for child in node.children:
            if child is not None:
                is_leaf = False
                new_str = curr_string + child.char
                self.get_suffixes(child, result, new_str)

        if is_leaf or node.is_end:
            result.append(curr_string)

    def incremental_search_trie(self, string):
        results = []
        nodes = self._root
        current_node = None
        for c in string:
            ascii = get_ascii(c)
            current_node = nodes[ascii]
            nodes = current_node.children

        self._get_suffixes(current_node, results, "")

        new_results = []
        for result in results:
            new_results.append(string + result)

        return new_results

