class TrieNode:
    def __init__(self, char, parent):
        self.char = char
        self.parent = parent
        self.child_nodes = [None] * 26
        self.is_complete_word = False

    def __str__(self):
        return self.char

    __repr__ = __str__

class Trie(object):

    def __init__(self):
        self.root = TrieNode('', None)


    def insert(self, word):
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

    def search(self, word, prefix=False):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word == "":
            return False

        node = self.root
        for c in word:
            node = node.child_nodes[ord(c) - ord('a')]

            if node is None:
                return False

        if prefix == False:
            # Look to see if this terminating node is a complete word
            if not node.is_complete_word:
                return False

        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.search(prefix, True)


trie = Trie()
# words = ["cat", "can", "cow", "bat"]
words = ["ab"]

for word in words:
    trie.insert(word)

print(trie.search("a"))
print(trie.startsWith("a"))