# Binary Tree Maximum Path Sum
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
# Input: [1,2,3]
#        1
#       / \
#      2   3
# Output: 6
#
# Example 2:
# Input: [-10,9,20,null,null,15,7]
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# Output: 42

import testlib
from datastructures import TreeNode
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def best_paths(node: Optional[TreeNode]) -> (int, Optional[int]):
            """left is the best path sum including current node,
            right is the best path sum within either child"""
            if node is None:
                return (0, None)
            best_including = node.val
            l = best_paths(node.left)
            r = best_paths(node.right)
            if l[0] > 0:
                if r[0] > 0:
                    best_including += max(l[0], r[0])
                else:
                    best_including += l[0]
            elif r[0] > 0:
                best_including += r[0]
            best_child = max(
                [
                    n
                    for n in [
                        l[1],
                        r[1],
                        node.val + sum([v for v in [l[0], r[0]] if v > 0]),
                    ]
                    if n is not None
                ]
            )
            return (best_including, best_child)

        out = best_paths(root)
        if out[1]:
            return max(out)
        return out[0]


if __name__ == "__main__":
    testdata = [
        ([1, [2, None, None], [3, None, None]], 6),
        ([-10, [9, None, None], [20, [15, None, None], [7, None, None]]], 42),
        ([-3, None, None], -3),
        (
            [
                9,
                [6, None, None],
                [
                    -3,
                    [-6, None, None],
                    [2, [2, [-6, [-6, None, None], None], [-6, None, None]], None],
                ],
            ],
            16,
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().maxPathSum(TreeNode.from_list(tc[0])), tc[1], tc
        ),
        testdata,
    )
