# Coin Change 2
# You are given coins of different denominations and a total amount of money. Write a
# function to compute the number of combinations that make up that amount. You may
# assume that you have infinite number of each kind of coin.
#
# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
# Example 3:
# Input: amount = 10, coins = [10]
# Output: 1
#
# Note:
# You can assume that
# - 0 <= amount <= 5000
# - 1 <= coin <= 5000
# - the number of coins is less than 500
# - the answer is guaranteed to fit into signed 32-bit integer

import testlib
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        answers_by_amount = [0 for _ in range(amount + 1)]
        answers_by_amount[0] = 1
        for coin in sorted(coins):
            for amt in range(coin, amount + 1):
                answers_by_amount[amt] += answers_by_amount[amt - coin]
        return answers_by_amount[amount]


if __name__ == "__main__":
    testdata = [(5, [1, 2, 5], 4), (3, [2], 0), (10, [10], 1)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().change(tc[0], tc[1]), tc[2], tc),
        testdata,
    )
