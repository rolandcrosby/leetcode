# Majority Element
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
# Input: [3,2,3]
# Output: 3
#
# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

from typing import List
import testlib


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) / 2
        counts = {}
        for n in nums:
            count = counts.setdefault(n, 0) + 1
            if count > maj:
                return n
            counts[n] = count


if __name__ == "__main__":
    testdata = [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().majorityElement(tc[0]), tc[1], tc),
        testdata,
    )

