# Single Number II
# Given a non-empty array of integers, every element appears three times except for one,
# which appears exactly once. Find that single one.
#
# Note:
#
# - Your algorithm should have a linear runtime complexity. Could you implement it
#   without using extra memory?
#
# Example 1:
# Input: [2,2,3,2]
# Output: 3
#
# Example 2:
# Input: [0,1,0,1,0,1,99]
# Output: 99

import testlib
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        possible = set()
        for num in nums:
            count = counts.get(num, 0) + 1
            if count == 1:
                possible.add(num)
            elif count == 2:
                possible.remove(num)
            counts[num] = count
        return next(iter(possible))

    def singleNumber_bit_twiddling(self, nums: List[int]) -> int:
        # this does not work for negative numbers because
        # python does not them assign a fixed length
        bits = 64
        counts = [0] * bits
        for num in nums:
            for bit in range(bits):
                if num & (1 << bit):
                    counts[bit] += 1
        out = 0
        for bit, count in enumerate(counts):
            if count % 3 > 0:
                out |= 1 << bit
        return out



if __name__ == "__main__":
    testdata = [
        ([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2], -4),
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
        ([-2, -2, -2, 1], 1),
        (
            [-19, -46, -19, -46, -9, -9, -19, 17, 17, 17, -13, -13, -9, -13, -46, -28],
            -28,
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().singleNumber(tc[0]), tc[1], tc), testdata
    )
