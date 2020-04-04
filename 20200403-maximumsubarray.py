# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List


class NaiveSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums) > 0
        ans = nums[0]
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                s = sum(nums[i:i+j+1])
                if s > ans:
                    ans = s
        return ans


class DivideSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        assert len(nums) > 0
        if len(nums) == 1:
            return nums[0]
        pivot = len(nums) // 2
        left = nums[0:pivot]
        right = nums[pivot:]
        bestLeft = self.maxSubArray(left)
        bestRight = self.maxSubArray(right)
        bestLeftSuffix = nums[pivot-1]
        leftSuffixSum = 0
        for start in range(pivot - 1, -1, -1):
            leftSuffixSum += nums[start]
            if leftSuffixSum > bestLeftSuffix:
                bestLeftSuffix = leftSuffixSum
        bestRightPrefix = nums[pivot]
        rightPrefixSum = 0
        for end in range(len(nums) - pivot):
            rightPrefixSum += nums[pivot + end]
            if rightPrefixSum > bestRightPrefix:
                bestRightPrefix = rightPrefixSum
        bestMiddle = bestLeftSuffix + bestRightPrefix
        return max(bestLeft, bestRight, bestMiddle)


class LinearSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        prefixSum = 0
        for n in nums:
            prefixSum += n
            if prefixSum > maxSoFar:
                maxSoFar = prefixSum
            if prefixSum < 0:
                prefixSum = 0
        return maxSoFar


if __name__ == "__main__":
    testdata = [
        ([-2], -2),
        ([-2, 1], 1),
        ([-2, 1, -3], 1),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-2, 1, -3, 4, -1, 2, 1, -4, 5], 7),
        ([1, 2], 3),
        ([-2, -1], -1)
    ]
    for klass in [NaiveSolution, DivideSolution, LinearSolution]:
        passed = 0
        for tc in testdata:
            ans = klass().maxSubArray(tc[0])
            if ans != tc[1]:
                print("%s: wrong answer for input %s: expected %s, got %s" % (klass.__name__, tc[0], tc[1], ans))
            else:
                passed += 1
        print("%s: %d of %d tests passed" % (klass.__name__, passed, len(testdata)))
