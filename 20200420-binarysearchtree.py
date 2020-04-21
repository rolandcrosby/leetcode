# Construct Binary Search Tree from Preorder Traversal
# Return the root node of a binary search tree that matches the given preorder traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
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

# 8 5 1 7 10 12
# [(8 _ _)] 5 1 7 10 12
# 5 < 8
# [(8 (5 _ _) _) (5 _ _)] 1 7 10 12 
# 1 < 5
# [(8 (5 (1 _ _) _) _) (5 (1 _ _) _) (1 _ _)] 7 10 12 
# 7 > 1
# 7 > 5
# 7 < 8
# [(8 (5 (1 _ _) (7 _ _)) _) (5 (1 _ _) (7 _ _)) (7 _ _)] 10 12 
# 10 > 7
# 10 > 5
# 10 > 8
# [(8 (5 (1 _ _) (7 _ _) (10 _ _)) (10 _ _)] 12 
# [(8 (5 (1 _ _) (7 _ _) (10 _ _)) (10 _ (12 _ _))]


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
        ([8, 5, 1, 7], TreeNode.from_list([8, [5, [1, None, None], [7, None, None]], None])),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().bstFromPreorder(tc[0]), tc[1], tc),
        testdata,
    )
