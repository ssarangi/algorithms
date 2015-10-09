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

from misc.incremental_search.ternary_tree import *
from misc.incremental_search.trie import *

def build_tree(words, algorithm):
    tree = None
    if algorithm == "trie":
        tree = Trie()
    elif algorithm == "ternary_tree":
        tree = TernaryTree()
    else:
        assert(0, "Not a valid algorithm")

    tree.create(words)
    return tree

def incremental_search(tree, search_string):
    results = tree.search(search_string)
    return results

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
    words = read_dictionary('test.txt')
    # search_string = input("String: ")
    search_string = "ok"
    root = create_trie(words)
    results = incremental_search_trie(search_string, root)
    # results1 = incremental_search_ternary_tree(search_string, words)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()