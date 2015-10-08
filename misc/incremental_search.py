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


def create_trie(words, root):
    for word in words:
        word = word.rstrip('\n')
        root = trie(word, root)

    return root

def read_dictionary(filename):
    root = []
    for i in range(0, 26):
        root.append(Node(chr(i + ord('a')), None))

    f = open(filename)
    words = f.readlines()
    f.close()

    root = create_trie(words, root)
    return root

def main():
    root = read_dictionary('wordsEn.txt')
    string = input("String: ")
    results = incremental_search_trie(string, root)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()