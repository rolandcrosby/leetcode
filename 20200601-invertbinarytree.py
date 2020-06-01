# Invert Binary Tree
# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import testlib
from datastructures import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        if root.left:
            root.left = self.invertTree(root.left)
        if root.right:
            root.right = self.invertTree(root.right)
        return root


if __name__ == "__main__":
    testdata = [
        (
            [
                4,
                [2, [1, None, None], [3, None, None]],
                [7, [6, None, None], [9, None, None]],
            ],
            [
                4,
                [7, [9, None, None], [6, None, None]],
                [2, [3, None, None], [1, None, None]],
            ],
        )
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().invertTree(TreeNode.from_list(tc[0])),
            TreeNode.from_list(tc[1]),
            tc,
        ),
        testdata,
    )
