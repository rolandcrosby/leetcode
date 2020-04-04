# Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        zeroesSeen = 0

        while True:
            if nums[idx] == 0:
                zeroesSeen += 1
            else:
                idx += 1
            if idx + zeroesSeen >= len(nums):
                break
            nums[idx] = nums[idx+zeroesSeen]
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
        

if __name__ == "__main__":
    testdata = [
        ([0,1,0,3,12], [1,3,12,0,0])
    ]
    passed = 0
    for tc in testdata:
        out = tc[0]
        Solution().moveZeroes(out)
        assert out == tc[1]
        passed += 1
    print("%d of %d tests passed" % (passed, len(testdata)))