# Sort Colors
# Given an array with n objects colored red, white or blue, sort them in-place so that
# objects of the same color are adjacent, with the colors in the order red, white and
# blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue
# respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array
# with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

import testlib
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeroes = 0
        ones = 0
        for n in nums:
            if n == 0:
                zeroes += 1
            elif n == 1:
                ones += 1
        for i in range(len(nums)):
            if i < zeroes:
                nums[i] = 0
            elif i < zeroes + ones:
                nums[i] = 1
            else:
                nums[i] = 2


def run(t, tc):
    ans = tc[0]
    Solution().sortColors(ans)
    t.assertEqual(ans, tc[1])


if __name__ == "__main__":
    testdata = [([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])]
    testlib.run(run, testdata)
