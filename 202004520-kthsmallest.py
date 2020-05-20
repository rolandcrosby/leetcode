# Kth Smallest Element in a BST
# Given a binary search tree, write a function kthSmallest to find the kth smallest
# element in it.
#
# Note:
# - You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
#
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the
# kth smallest frequently? How would you optimize the kthSmallest routine?

import testlib
from datastructures import TreeNode
from typing import List
import bisect


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        seen: List[int] = []
        todo: List[TreeNode] = [root]
        while todo:
            node = todo.pop(0)
            if node.left is not None:
                todo.append(node.left)
            if node.right is not None:
                todo.append(node.right)
            pos = bisect.bisect_right(seen, node.val)
            if pos < k:
                seen.insert(pos, node.val)
            if len(seen) > k:
                seen.pop(-1)
        return seen[k - 1]


if __name__ == "__main__":
    testdata = [
        ([3, [1, None, [2, None, None]], [4, None, None]], 1, 1),
        ([5, [3, [2, [1, None, None], None], [4, None, None]], [6, None, None]], 3, 3),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().kthSmallest(TreeNode.from_list(tc[0]), tc[1]), tc[2], tc
        ),
        testdata,
    )
