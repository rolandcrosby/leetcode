# Search in Rotated Sorted Array
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
import testlib
from typing import List, Optional, Tuple


class Solution:
    def __init__(self, debug: bool=False):
        self.debug = debug

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        if self.debug:
            self._debug_input(nums, target)
        while start < end:
            guess = (start + end) // 2
            if self.debug:
                self._debug_iteration(nums, target, start, guess, end)
            if nums[guess] == target:
                return guess
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            new_indices = Solution._tbl[
                (
                    self._cmp(nums[start], target),
                    self._cmp(nums[guess], target),
                    self._cmp(nums[end], target),
                )
            ](start, guess, end)
            if new_indices is None:
                return -1
            (start, end) = new_indices
        if nums[start] == target:
            return start
        return -1

    # Comparison table worked out in https://1drv.ms/x/s!AqFhbsaIID-4iMBlq8hrBZXI2JMOMw
    _tbl = {
        (-1, -1, -1): lambda s, g, e: (s + 1, e - 1),
        (-1, -1, 1): lambda s, g, e: (g + 1, e - 1),
        (-1, 1, -1): lambda s, g, e: (s + 1, g - 1),
        (-1, 1, 1): lambda s, g, e: (s + 1, g - 1),
        (1, -1, -1): lambda s, g, e: None,
        (1, -1, 1): lambda s, g, e: (g + 1, e - 1),
        (1, 1, -1): lambda s, g, e: None,
        (1, 1, 1): lambda s, g, e: (s + 1, e - 1),
    }

    def _cmp(self, x, y):
        return (x > y) - (x < y)

    def _debug_input(self, nums: List[int], target: int, width: int=4):
        fmt = "{{:>{}}}".format(width)
        print(
            "".join([fmt.format(n) for n in nums])
            + ", looking for {}".format(target)
        )

    def _debug_iteration(self, nums: List[int], target: int, start: int, guess: int, end: int, width: int=4):
        fmt = "{{:>{}}}".format(width)
        pointers = [
            "^"
            if n == guess
            else ("[" if n == start else ("]" if n == end else ""))
            for n in range(len(nums))
        ]
        comparisons = [
            ""
            if p == ""
            else ("<" if nums[i] < target else (">" if nums[i] > target else "="))
            for (i, p) in enumerate(pointers)
        ]
        print("".join([fmt.format(p) for p in pointers]))
        print("".join([fmt.format(c) for c in comparisons]))


if __name__ == "__main__":
    testdata = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
        ([5, 1, 2, 3, 4], 1, 1),
        ([1], 1, 0),
        (
            [
                266,
                267,
                268,
                269,
                271,
                278,
                282,
                292,
                293,
                298,
                6,
                9,
                15,
                19,
                21,
                26,
                33,
                35,
                37,
                38,
                39,
                46,
                49,
                54,
                65,
                71,
                74,
                77,
                79,
                82,
                83,
                88,
                92,
                93,
                94,
                97,
                104,
                108,
                114,
                115,
                117,
                122,
                123,
                127,
                128,
                129,
                134,
                137,
                141,
                142,
                144,
                147,
                150,
                154,
                160,
                163,
                166,
                169,
                172,
                173,
                177,
                180,
                183,
                184,
                188,
                198,
                203,
                208,
                210,
                214,
                218,
                220,
                223,
                224,
                233,
                236,
                241,
                243,
                253,
                256,
                257,
                262,
                263,
            ],
            208,
            67,
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution(True).search(tc[0], tc[1]), tc[2]), testdata
    )
