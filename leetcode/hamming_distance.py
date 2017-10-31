class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num_bits = 32
        hamming_distance = 0
        while num_bits > 0:
            last_bit_x = x & 0x1
            last_bit_y = y & 0x1
            x = x >> 1
            y = y >> 1
            if last_bit_x != last_bit_y:
                hamming_distance += 1
            num_bits -= 1
        return hamming_distance
        
import unittest

class UnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.soln = Solution()

    def testkSmallestPairs(self):
        self.assertEqual(self.soln.hammingDistance(1, 4), 2)

if __name__ == "__main__":
    unittest.main()