# 136. Single Number
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# 
# Example 1:
# Input: [2,2,1]
# Output: 1
# 
# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """This implementation will only work if elements occur exactly
        once or twice in the input."""
        possible = set()
        for n in nums:
            if n in possible:
                possible.remove(n)
            else:
                possible.add(n)
        return list(possible)[0]

class AnnoyingSolution:
    def singleNumber(self, nums: List[int]) -> int:
        """After submitting, I heard that this is the "right" answer that
         doesn't require you to use extra memory. Thanks, I hate it."""
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums, 0)

if __name__ == "__main__":
    testdata = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4)
    ]
    for klass in [Solution, AnnoyingSolution]:
        passed = 0
        for tc in testdata:
            assert klass().singleNumber(tc[0]) == tc[1]
            passed += 1
        print("%s: %d of %d tests passed" % (klass.__name__, passed, len(testdata)))
