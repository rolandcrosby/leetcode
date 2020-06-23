# Count Complete Tree Nodes
# Given a complete binary tree, count the number of nodes.
#
# Note:
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled,
# and all nodes in the last level are as far left as possible. It can have between 1 and
# 2h nodes inclusive at the last level h.
#
# Example:
#
# Input:
#      1
#    /   \
#   2     3
#  / \   /
# 4   5 6
#
# Output: 6

import testlib
from datastructures import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = 0
        right_depth = 0
        node = root
        while node is not None:
            left_depth += 1
            node = node.left
        node = root
        while node is not None:
            right_depth += 1
            node = node.right
        if left_depth == right_depth:
            return (1 << left_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == "__main__":
    testdata = [
        ([1, None, None], 1),
        ([1, [2, None, None], None], 2),
        ([1, [2, None, None], [3, None, None]], 3),
        ([1, [2, [4, None, None], [5, None, None]], [3, [6, None, None], None]], 6),
        ([1, [2, [3, None, None], None], None], 3),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().countNodes(TreeNode.from_list(tc[0])), tc[1], tc
        ),
        testdata,
    )

