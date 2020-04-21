from typing import List, Optional, Union

ListNode = Union[Optional[int], List["ListNode"]]


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        if other is None:
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )

    def __repr__(self):
        if self.left is None:
            l = "_"
        else:
            l = repr(self.left)
        if self.right is None:
            r = "_"
        else:
            r = repr(self.right)
        return "(%s %s %s)" % (repr(self.val), l, r)

    @staticmethod
    def from_list(ls: ListNode):
        """
        Recursively build a tree based on a list of values, like this:

        ```
        [0, None, None] # => single node with value 0
        [0, [1, None, None], None] # => root 0 with left leaf 1
        ```
        """
        if ls is None:
            return None
        n = TreeNode(ls[0])
        n.left = TreeNode.from_list(ls[1])
        n.right = TreeNode.from_list(ls[2])
        return n
