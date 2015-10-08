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
Main file for implementing all algorithms for incremental search.
tries, suffix trees etc
"""

class Node:
    def __init__(self, char, parent):
        self._char = char
        self._child_nodes = [None] * 26
        self._parent = parent

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

    @root.setter
    def root(self, v):
        self._root = v

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

    def insert(self, words):
        for word in words:
            self._root = self._insert(self._root, word)

    def search(self, word, node=None):
        if node is None:
            return False

        c = word[0]
        if ord(c) < ord(node.data):
            self.search(node.left, word[1:])
        elif ord(c) > ord(node.data):
            self.search(node.right, word[1:])
        else:
            if node.is_end and len(word) == 0:
                return True
            elif len(word) == 0:
                return False
            else:
                return self.search(node.middle, word[1:])

    def get_suffixes(self, node, word, curr_string="", results=[]):
        print(curr_string)
        if node is None:
            return

        if len(word) == 0:
            curr_string += node.data
            if node.is_end:
                results.append(curr_string)
                return
            else:
                self.get_suffixes(node.left, [], curr_string, results)
                self.get_suffixes(node.middle, [], curr_string, results)
                self.get_suffixes(node.right, [], curr_string, results)
                return

        c = word[0]

        if ord(c) < ord(node.data):
            self.get_suffixes(node.left, word, curr_string, results)
        elif ord(c) > ord(node.data):
            self.get_suffixes(node.right, word, curr_string, results)
        else:
            curr_string += node.data
            self.get_suffixes(node.middle, word[1:], curr_string, results)


def get_ascii(char):
    return ord(char) - ord('a')

def get_character(ascii):
    return chr(ascii + ord('a'))

def trie(word, root):
    nodes = root
    parent = None
    for c in word:
        ascii = get_ascii(c)
        current_node = nodes[ascii]

        if current_node == None:
            current_node = Node(c, parent)
            nodes[ascii] = current_node

        nodes = current_node.children
        parent = current_node

    return root

def get_suffixes(node, result, curr_string):
    is_leaf = True
    for child in node.children:
        if child is not None:
            is_leaf = False
            new_str = curr_string + child.char
            get_suffixes(child, result, new_str)

    if is_leaf:
        result.append(curr_string)

def incremental_search_trie(string, root):
    results = []
    nodes = root
    print(nodes)
    current_node = None
    for c in string:
        ascii = get_ascii(c)
        current_node = nodes[ascii]

    get_suffixes(current_node, results, "")

    new_results = []
    for result in results:
        new_results.append(string + result)

    return new_results

def incremental_search_ternary_tree(search_string, words):
    ternary_tree = TernaryTree()
    ternary_tree.insert(words)
    results = []
    ternary_tree.get_suffixes(ternary_tree.root, search_string, "", results)
    return results

def create_trie(words):
    root = []
    for i in range(0, 26):
        root.append(Node(chr(i + ord('a')), None))

    for word in words:
        root = trie(word, root)

    return root

def read_dictionary(filename):
    f = open(filename)
    words = f.readlines()
    f.close()

    new_words = []
    for word in words:
        word = word.rstrip('\n')
        new_words.append(word)

    return new_words

def main():
    words = read_dictionary('wordsEn.txt')
    search_string = input("String: ")
    # root = create_trie(words)
    # results = incremental_search_trie(string, root)
    results1 = incremental_search_ternary_tree(search_string, words)

    for result in results1:
        print(result)

if __name__ == "__main__":
    main()