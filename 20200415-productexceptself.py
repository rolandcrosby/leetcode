# Product of Array Except Self
# Given an array nums of n integers where n > 1,  return an array output such that
# output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix
# of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count
# as extra space for the purpose of space complexity analysis.)

from typing import List
import testlib


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = nums.copy()
        suffixes = nums.copy()
        out = []
        for i in range(1, len(nums)):
            prefixes[i] *= prefixes[i - 1]
            suffixes[len(nums) - i - 1] *= suffixes[len(nums) - i]
        for i in range(len(nums)):
            p = 1 if i == 0 else prefixes[i - 1]
            s = 1 if i == len(nums) - 1 else suffixes[i + 1]
            out.append(p * s)
        return out


if __name__ == "__main__":
    testdata = [([1, 2, 3, 4], [24, 12, 8, 6])]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().productExceptSelf(tc[0]), tc[1], tc),
        testdata,
    )
