# Construct Binary Search Tree from Preorder Traversal
# Return the root node of a binary search tree that matches the given preorder
# traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of node.right has
# a value > node.val.  Also recall that a preorder traversal displays the value of the
# node first, then traverses node.left, then traverses node.right.)
#
# Example 1:
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
#        8
#    5      10
#  1   7  \N  12
#
# Note:
# - 1 <= preorder.length <= 100
# - The values of preorder are distinct.


from typing import List
from datastructures import TreeNode
import testlib


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def add(root: TreeNode, new: TreeNode) -> TreeNode:
            if new.val < root.val:
                if root.left is None:
                    root.left = new
                else:
                    root.left = add(root.left, new)
            else:
                if root.right is None:
                    root.right = new
                else:
                    root.right = add(root.right, new)
            return root

        root = TreeNode(preorder[0])
        for child in preorder[1:]:
            node = TreeNode(child)
            root = add(root, node)
        return root


class BetterSolution:
    # Thanks to https://github.com/collares for explaining the logic here
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        current = root
        left_nodes = []  # nodes from which we descended to the left
        for val in preorder[1:]:
            node = TreeNode(val)
            if val < current.val:
                left_nodes.append(current)
                current.left = node
                current = current.left
            else:
                while len(left_nodes) > 0 and left_nodes[-1].val < val:
                    current = left_nodes.pop(-1)
                current.right = node
                current = current.right
        return root


if __name__ == "__main__":
    testdata = [
        (
            [8, 5, 1, 7, 10, 12],
            TreeNode.from_list(
                [8, [5, [1, None, None], [7, None, None]], [10, None, [12, None, None]]]
            ),
        ),
        ([8, 5, 10], TreeNode.from_list([8, [5, None, None], [10, None, None]])),
        ([8], TreeNode.from_list([8, None, None])),
        ([8, 10], TreeNode.from_list([8, None, [10, None, None]])),
        (
            [8, 5, 1, 7],
            TreeNode.from_list([8, [5, [1, None, None], [7, None, None]], None]),
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().bstFromPreorder(tc[0]), tc[1], tc),
        testdata,
    )
