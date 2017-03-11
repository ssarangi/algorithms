# https://leetcode.com/problems/word-ladder/

import sys
# from queue import PriorityQueue
import heapq

MIN_HEAP = 1
MAX_HEAP = -1

class PriorityQueue:
    def __init__(self, heap_type):
        self.heap_type = heap_type
        self.queue = []

    def put(self, item, priority = None):
        if priority is None:
            sign = 0
            if self.heap_type == MIN_HEAP:
                sign = 1
            else:
                sign = -1
            priority = sign * item

        heapq.heappush(self.queue, (priority, item))

    def get(self):
        return heapq.heappop(self.queue)[1]

    def top(self):
        v = heapq.heappop(self.queue)
        heapq.heappush(self.queue, v)
        return v[1]

    def empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        def differs_by_one_char(w1, w2):
            sw1 = set(w1)
            sw2 = set(w2)

            return len(sw1.difference(sw2)) == 1

        # Create a path from one word to the other
        def create_paths(list_of_words):
            list_of_words = set(list_of_words)
            paths = {}

            for idx, w in enumerate(list_of_words):
                for idx1, w1 in enumerate(list_of_words):
                    if idx != idx1 and differs_by_one_char(w, w1):
                        paths[w] = [w1] if w not in paths else paths[w] + [w1]

            return paths

        graph = create_paths([beginWord, endWord] + list(wordList))

        # Apply Dijkstra to figure out the shortest path
        pq = PriorityQueue(MIN_HEAP)
        costs = dict()
        costs[beginWord] = 0
        costs[endWord] = sys.maxsize

        for w in wordList:
            costs[w] = sys.maxsize

        pq.put((0, beginWord))

        while not pq.empty():
            cost, node = pq.get()

            if node == endWord:
                break

            neighbors = []
            if node in graph:
                neighbors = graph[node]
            
            for neighbor in neighbors:
                newcost = cost + 1
                if costs[neighbor] > newcost:
                    costs[neighbor] = newcost
                    pq.put((newcost, neighbor))

        if costs[endWord] == sys.maxsize:
            return 0

        return costs[endWord] + 1


import unittest


class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testLadderLength(self):
        self.assertEqual(self.soln.ladderLength("hit", "cog", {"hot", "dot", "dog", "lot", "log"}), 5)
        self.assertEqual(self.soln.ladderLength("a", "c", {"a", "b", "c"}), 2)
        self.assertEqual(self.soln.ladderLength("hot", "dog", {"hot", "dog"}), 0)
        self.assertEqual(self.soln.ladderLength("leet", "code", {"lest","leet","lose","code","lode","robe","lost"}), 6)

if __name__ == "__main__":
    unittest.main()
