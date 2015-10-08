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
    def __init__(self, char):
        self._char = char
        self._child_nodes = [None] * 26

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
    for c in word:
        ascii = get_ascii(c)
        current_node = nodes[ascii]

        if current_node == None:
            current_node = Node(c)
            nodes[ascii] = current_node

        nodes = current_node.children

    return root

def create_trie(words, root):
    for word in words:
        root = trie(word, root)

    return root

def read_dictionary(filename):
    root = []
    for i in range(0, 26):
        root.append(Node(chr(i + ord('a'))))

    f = open(filename)
    words = f.readlines()
    f.close()

    create_trie(words, root)

def main():
    read_dictionary('wordsEn.txt')

if __name__ == "__main__":
    main()