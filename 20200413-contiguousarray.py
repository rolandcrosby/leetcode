# Contiguous Array
# Given a binary array, find the maximum length of a contiguous subarray with equal
# number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of
# 0 and 1.
#
# Note: The length of the given binary array will not exceed 50,000.


from typing import List
import testlib


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cumSum = 0
        longest = 0
        firsts = {0: -1}
        for (i, n) in enumerate(nums):
            bias = -1 if n < 1 else 1
            cumSum += bias
            if cumSum not in firsts:
                firsts[cumSum] = i
            else:
                length = i - firsts[cumSum]
                if length > longest:
                    longest = length
        return longest


if __name__ == "__main__":
    testdata = [
        ([0, 1], 2),
        ([0, 1, 0], 2),
        ([0, 1, 0, 1], 4),
        ([0, 0, 0, 1, 0, 1], 4),
        ([0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1], 10),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().findMaxLength(tc[0]), tc[1], repr(tc)),
        testdata,
    )
