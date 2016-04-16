# https://leetcode.com/problems/add-and-search-word-data-structure-design/

class TrieNode:
    def __init__(self, char, parent):
        self.char = char
        self.parent = parent
        self.child_nodes = [None] * 26
        self.is_complete_word = False

    def __str__(self):
        return self.char

    __repr__ = __str__

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode('', None)


    def addWord(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if word == '':
            return

        node = self.root
        for c in word:
            parent = node
            node = node.child_nodes[ord(c) - ord('a')]

            if node is None:
                parent.child_nodes[ord(c) - ord('a')] = TrieNode(c, parent)
                node = parent.child_nodes[ord(c) - ord('a')]

        node.is_complete_word = True

    def search(self, word, node=None):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word == "":
            if node is None:
                return False
            elif node.is_complete_word:
                return True
            else:
                return False

        if node is None:
            node = self.root

        find_result = False
        c = word[0]
        if c == ".":
            for i in range(0, 26):
                cn = node.child_nodes[i]
                if cn is not None:
                    find_result |= self.search(word[1:], cn)
        else:
            node = node.child_nodes[ord(c) - ord('a')]

            if node is None:
                return False

            find_result = self.search(word[1:], node)

        return find_result