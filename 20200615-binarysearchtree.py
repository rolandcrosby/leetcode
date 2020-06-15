# Search in a Binary Search Tree
# Given the root node of a binary search tree (BST) and a value. You need to find the
# node in the BST that the node's value equals the given value. Return the subtree
# rooted with that node. If such node doesn't exist, you should return NULL.
#
# For example,
#
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# And the value to search: 2
# You should return this subtree:
#
#       2
#      / \
#     1   3
# In the example above, if we want to search the value 5, since there is no node with
# value 5, we should return NULL.
#
# Note that an empty tree is represented by NULL, therefore you would see the expected
# output (serialized tree format) as [], not null.

import testlib
from datastructures import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur is not None and cur.val != val:
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return cur


if __name__ == "__main__":
    testdata = [
        (
            [4, [2, [1, None, None], [3, None, None]], [7, None, None]],
            2,
            [2, [1, None, None], [3, None, None]],
        )
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().searchBST(TreeNode.from_list(tc[0]), tc[1]),
            TreeNode.from_list(tc[2]),
        ),
        testdata,
    )
