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

class TSTNode:
    def __init__(self, char):
        self._data = char
        self._left = None
        self._right = None
        self._middle = None
        self._is_end = False

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, v):
        self._left = v

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, v):
        self._right = v

    @property
    def middle(self):
        return self._middle

    @middle.setter
    def middle(self, v):
        self._middle = v

    @property
    def is_end(self):
        return self._is_end

    @is_end.setter
    def is_end(self, v):
        self._is_end = v

    def __str__(self):
        return self._data

    __repr__ = __str__

class TernaryTree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def _insert(self, node, word):
        if len(word) == 0:
            return

        c = word[0]
        if node is None:
            node = TSTNode(c)

        if ord(c) < ord(node.data):
            node.left = self._insert(node.left, word)
        elif ord(c) > ord(node.data):
            node.right = self._insert(node.right, word)
        else:
            if len(word) > 1:
                node.middle = self._insert(node.middle, word[1:])
            else:
                node.is_end = True

        return node

    def insert(self, word):
        node = self._insert(self._root, word)
        if self._root == None:
            self._root = node

    def create(self, words):
        for word in words:
            self._insert(self._root, word)

    # def search(self, word, node=None):
    #     if node is None:
    #         return False
    #
    #     c = word[0]
    #     if ord(c) < ord(node.data):
    #         self.search(node.left, word[1:])
    #     elif ord(c) > ord(node.data):
    #         self.search(node.right, word[1:])
    #     else:
    #         if node.is_end and len(word) == 0:
    #             return True
    #         elif len(word) == 0:
    #             return False
    #         else:
    #             return self.search(node.middle, word[1:])

    def _get_suffixes(self, node, word, curr_string="", results=[]):
        if node is None:
            return

        if len(word) == 0:
            if node.is_end:
                results.append(curr_string + node.data)

            self._get_suffixes(node.left, "", curr_string, results)
            self._get_suffixes(node.middle, "", curr_string + node.data, results)
            self._get_suffixes(node.right, "", curr_string, results)
            return

        c = word[0]

        if ord(c) < ord(node.data):
            self._get_suffixes(node.left, word, curr_string, results)
        elif ord(c) > ord(node.data):
            self._get_suffixes(node.right, word, curr_string, results)
        else:
            curr_string += node.data
            if node.is_end:
                results.append(curr_string)

            self._get_suffixes(node.middle, word[1:], curr_string, results)

    def search(self, search_string):
        results = []
        self._get_suffixes(self._root, search_string, "", results)
        return results