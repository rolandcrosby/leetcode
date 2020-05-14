# Cousins in Binary Tree
# In a binary tree, the root node is at depth 0, and children of each depth k node are
# at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different
# parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of
# two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.
#
# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
#    1
#  2   3
# 4
# Output: false
#
# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
#     1
#   2   3
#    4    5
# Output: true
#
# Example 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3
#    1
#  2   3
#   4
# Output: false
#
# Note:
# - The number of nodes in the tree will be between 2 and 100.
# - Each node has a unique integer value from 1 to 100.

import testlib
from datastructures import TreeNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_found, y_found = False, False
        x_parent, y_parent = None, None
        x_depth, y_depth = 0, 0
        todo = [(root, None, 0)]
        while not x_found or not y_found:
            (node, parent, depth) = todo.pop(0)
            if node.val == x:
                x_found = True
                x_parent = parent
                x_depth = depth
            if node.val == y:
                y_found = True
                y_parent = parent
                y_depth = depth
            if node.left is not None:
                todo.append((node.left, node.val, depth + 1))
            if node.right is not None:
                todo.append((node.right, node.val, depth + 1))
        return x_depth == y_depth and x_parent != y_parent


if __name__ == "__main__":
    testdata = [
        ([1, [2, [4, None, None], None], [3, None, None]], 4, 3, False),
        ([1, [2, None, [4, None, None]], [3, None, [5, None, None]]], 5, 4, True),
        ([1, [2, None, [4, None, None]], [3, None, None]], 2, 3, False),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().isCousins(TreeNode.from_list(tc[0]), tc[1], tc[2]), tc[3], tc
        ),
        testdata,
    )
