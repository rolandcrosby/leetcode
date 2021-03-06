# Jump Game
#
# Given an array of non-negative integers, you are initially positioned at the first
# index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length
# is 0, which makes it impossible to reach the last index.

import testlib
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        max_reachable = 0
        for (i, n) in enumerate(nums):
            if max_reachable >= target:
                return True
            if max_reachable < i:
                break
            max_reachable = max(max_reachable, i + n)
        return max_reachable >= target


if __name__ == "__main__":
    testdata = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([2, 5, 0, 0], True),
        ([0], True),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().canJump(tc[0]), tc[1], tc), testdata
    )
