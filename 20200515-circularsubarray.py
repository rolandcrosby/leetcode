# Maximum Sum Circular Subarray
# Given a circular array C of integers represented by A, find the maximum possible sum
# of a non-empty subarray of C.
#
# Here, a circular array means the end of the array connects to the beginning of the
# array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i
# >= 0.)
#
# Also, a subarray may only include each element of the fixed buffer A at most once.
# (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <=
# j with k1 % A.length = k2 % A.length.)
#
# Example 1:
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
#
# Example 2:
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
#
# Example 3:
# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
#
# Example 4:
# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
#
# Example 5:
# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
#
# Note:
# - -30000 <= A[i] <= 30000
# - 1 <= A.length <= 30000


import testlib
from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]
        most_positive_internal = A[0]
        most_negative_internal = A[0]
        max_prefix_sum = 0
        min_prefix_sum = 0
        total_sum = A[0]
        seq = iter(A)
        next(seq)
        for n in seq:
            total_sum += n
            max_prefix_sum += n
            if max_prefix_sum > most_positive_internal:
                most_positive_internal = max_prefix_sum
            if max_prefix_sum < 0:
                max_prefix_sum = 0
            min_prefix_sum += n
            if min_prefix_sum < most_negative_internal:
                most_negative_internal = min_prefix_sum
            if min_prefix_sum > 0:
                min_prefix_sum = 0
        return max(
            total_sum, most_positive_internal, total_sum - most_negative_internal
        )


if __name__ == "__main__":
    testdata = [
        ([1, -2, 3, -2], 3),
        ([5, -3, 5], 10),
        ([3, -1, 2, -1], 4),
        ([3, -2, 2, -3], 3),
        ([-2, -3, -1], -1),
        ([3, 1, 3, 2, 6], 15),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().maxSubarraySumCircular(tc[0]), tc[1], tc
        ),
        testdata,
    )
