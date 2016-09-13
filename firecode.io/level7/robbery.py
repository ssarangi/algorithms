def robbery(amounts):
    dp = [0] * len(amounts)
    final_max = 0
    for idx, amount in enumerate(amounts):
        maxv = 0
        for i in range(0, idx - 1):
            maxv = max(maxv, dp[i])

        dp[idx] = maxv + amount
        final_max = max(final_max, dp[idx])

    return final_max

import unittest

class UnitTest(unittest.TestCase):
    def testRobbery(self):
        self.assertEqual(robbery([60, 50, 20, 32, 20, 50]), 142)
        self.assertEqual(robbery([40, 25, 25, 30]), 70)

if __name__ == "__main__":
    unittest.main()