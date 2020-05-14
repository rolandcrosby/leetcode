# Subarray Sum Equals K
# Given an array of integers and an integer k, you need to find the total number of
# continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
#
# Note:
# - The length of the array is in range [1, 20,000].
# - The range of numbers in the array is [-1000, 1000] and the range of the integer k
#   is [-1e7, 1e7].

import testlib
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        s = 0
        # sum_occurrences : {sum(nums[0:i]) : [i]}
        sum_occurrences = {0: [0]}
        for (i, n) in enumerate(nums):
            s += n
            if s not in sum_occurrences:
                sum_occurrences[s] = []
            sum_occurrences[s].append(i + 1)
        solutions = 0
        for s in sum_occurrences.keys():
            diff = s - k
            if diff in sum_occurrences:
                for end in sum_occurrences[s]:
                    for start in sum_occurrences[diff]:
                        if start >= end:
                            break
                        solutions += 1
        return solutions


if __name__ == "__main__":
    testdata = [([1, 1, 1], 2, 2)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().subarraySum(tc[0], tc[1]), tc[2], tc),
        testdata,
    )
