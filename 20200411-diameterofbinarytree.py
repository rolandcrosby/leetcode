# Diameter of Binary Tree
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
# max maxinternal (maxinternal = max (l + r) max of maxes)
#                1  [2 1 2]
#               / \
#        [1 2] 2   3 [0 0]
#             / \
#      [0 0] 4   5  [0 0]
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

from typing import List, Optional


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "(%s, %s, %s)" % (repr(self.val), repr(self.left), repr(self.right))

    @staticmethod
    def from_list(ls: List[Optional[int]]):
        if ls is None:
            return None
        n = TreeNode(ls[0])
        n.left = TreeNode.from_list(ls[1])
        n.right = TreeNode.from_list(ls[2])
        return n


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depths(node: TreeNode) -> (int, int):
            if node is None:
                return (0, 0)
            depth_l = 0
            depth_r = 0
            prev_max = 0
            if node.left is not None:
                lds = depths(node.left)
                depth_l = 1 + lds[0]
                prev_max = lds[1]
            if node.right is not None:
                rds = depths(node.right)
                depth_r = 1 + rds[0]
                prev_max = max(prev_max, rds[1])
            return (max(depth_l, depth_r), max(depth_l + depth_r, prev_max))
        return depths(root)[1]

            

if __name__ == "__main__":
    testdata = [
        ([1, [2, [4, None, None], [5, None, None]], [3, None, None]], 3)
    ]
    passed = 0
    for tc in testdata:
        assert Solution().diameterOfBinaryTree(
            TreeNode.from_list(tc[0])) == tc[1]
        passed += 1
    print("%d of %d tests passed" % (passed, len(testdata)))
