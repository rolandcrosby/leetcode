# Online Stock Span
# Write a class StockSpanner which collects daily price quotes for some stock, and
# returns the span of that stock's price for the current day.
#
# The span of the stock's price today is defined as the maximum number of consecutive
# days (starting from today and going backwards) for which the price of the stock was
# less than or equal to today's price.
#
# For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60,
# 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
#
#
#
# Example 1:
# Input: ["StockSpanner","next","next","next","next","next","next","next"],
# [[],[100],[80],[60],[70],[60],[75],[85]]
# Output: [null,1,1,1,2,1,4,6]
# Explanation:
# First, S = StockSpanner() is initialized.  Then:
# S.next(100) is called and returns 1,
# S.next(80) is called and returns 1,
# S.next(60) is called and returns 1,
# S.next(70) is called and returns 2,
# S.next(60) is called and returns 1,
# S.next(75) is called and returns 4,
# S.next(85) is called and returns 6.
#
# Note that (for example) S.next(75) returned 4, because the last 4 prices
# (including today's price of 75) were less than or equal to today's price.
#
# Note:
# - Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# - There will be at most 10000 calls to StockSpanner.next per test case.
# - There will be at most 150000 calls to StockSpanner.next across all test cases.
# - The total time limit for this problem has been reduced by 75% for C++, and 50% for
#   all other languages.

import testlib
from typing import List


class StockSpanner:
    def __init__(self):
        self.prices = []
        self.gte_indices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        if len(self.prices) == 1:
            self.gte_indices = [0]
        while self.gte_indices and self.prices[self.gte_indices[-1]] <= price:
            self.gte_indices.pop(-1)
        if self.gte_indices:
            ans = len(self.prices) - 1 - self.gte_indices[-1]
        else:
            ans = len(self.prices)
        self.gte_indices.append(len(self.prices) - 1)
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == "__main__":
    testdata = [
        ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        ([28, 14, 28, 35, 46, 53, 66, 80, 87, 88], [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]),
    ]

    def run(t: testlib.unittest.TestCase, input: List[int], output: List[int]):
        uut = StockSpanner()
        for i, n in enumerate(input):
            t.assertEqual(uut.next(n), output[i])

    testlib.run(lambda t, tc: run(t, tc[0], tc[1]), testdata)
