# Counting Bits
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
# calculate the number of 1's in their binary representation and return them as an
# array.
#
# Example 1:
# Input: 2
# Output: [0,1,1]
#
# Example 2:
# Input: 5
# Output: [0,1,1,2,1,2]
#
# Follow up:
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can
# you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
import testlib
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        out = [0, 1]
        next_jump = 2
        for i in range(2, num + 1):
            if i == next_jump * 2:
                next_jump *= 2
            out.append(1 + out[i % next_jump])
        return out


if __name__ == "__main__":
    testdata = [(2, [0, 1, 1]), (5, [0, 1, 1, 2, 1, 2])]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().countBits(tc[0]), tc[1], tc), testdata
    )
