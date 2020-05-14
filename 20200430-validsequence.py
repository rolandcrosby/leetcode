# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
# Given a binary tree where each path going from the root to any leaf form a valid
# sequence, check if a given string is a valid sequence in such binary tree.
#
# We get the given string from the concatenation of an array of integers arr and the
# concatenation of all values of the nodes along a path results in a sequence in the
# given binary tree.
#
# Example 1:
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation:
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
# Other valid sequences are:
# 0 -> 1 -> 1 -> 0
# 0 -> 0 -> 0
#
# Example 2:
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
# Output: false
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
#
# Example 3:
# Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
# Output: false
# Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
#
# Constraints:
# - 1 <= arr.length <= 5000
# - 0 <= arr[i] <= 9
# - Each node's value is between [0 - 9].

from datastructures import TreeNode
import testlib
from typing import List


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        to_check = [(root, arr)]
        while len(to_check) > 0:
            (root, remaining) = to_check.pop(0)
            if len(remaining) == 1:
                if (
                    root.val == remaining[0]
                    and root.left is None
                    and root.right is None
                ):
                    return True
                continue
            if root.val != remaining[0]:
                continue
            if root.left is not None:
                to_check.insert(0, (root.left, remaining[1:]))
            if root.right is not None:
                to_check.insert(0, (root.right, remaining[1:]))
        return False


if __name__ == "__main__":
    testdata = [
        (
            [
                0,
                [1, [0, None, [1, None, None]], [1, [0, None, None], [0, None, None]]],
                [0, [0, None, None], None],
            ],
            [0, 1, 0, 1],
            True,
        ),
        (
            [
                3,
                None,
                [
                    7,
                    [6, None, [4, None, [6, None, None]]],
                    [8, [1, [4, None, None], None], None],
                ],
            ],
            [3, 7, 6, 4, 6],
            True,
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().isValidSequence(TreeNode.from_list(tc[0]), tc[1]), tc[2], tc
        ),
        testdata,
    )
