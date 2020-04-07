# Counting Elements
# Given an integer array arr, count element x such that x + 1 is also in arr.
#
# If there're duplicates in arr, count them seperately.
#
# Example 1:
#
# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
# Example 2:
#
# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
# Example 3:
#
# Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.
# Example 4:
#
# Input: arr = [1,1,2,2]
# Output: 2
# Explanation: Two 1s are counted cause 2 is in arr.
#
# Constraints:
# 1 <= arr.length <= 1000
# 0 <= arr[i] <= 1000

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        values = set(arr)
        return sum([1 for el in arr if el+1 in values])


if __name__ == "__main__":
    testdata = [
        ([1, 2, 3], 2),
        ([1, 1, 3, 3, 5, 5, 7, 7], 0),
        ([1, 3, 2, 3, 5, 0], 3),
        ([1, 1, 2, 2], 2)
    ]
    passed = 0
    for tc in testdata:
        assert Solution().countElements(tc[0]) == tc[1]
        passed += 1
    print("%d of %d tests passed" % (passed, len(testdata)))
