# Middle of the Linked List
# Given a non-empty, singly linked list with head node head, return a middle node of
# linked list.
#
# If there are two middle nodes, return the second middle node.
#
# Example 1:
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
#
# Example 2:
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.
#
# Note:
# The number of nodes in the given list will be between 1 and 100.

from typing import List
import testlib


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "(%s, %s)" % (repr(self.val), repr(self.next))

    @staticmethod
    def fromList(input: List) -> "ListNode":
        nodes = [ListNode(el) for el in input]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
        return slow


if __name__ == "__main__":
    testdata = [([1, 2, 3, 4, 5], 3), ([1, 2, 3, 4, 5, 6], 4)]

    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().middleNode(ListNode.fromList(tc[0])).val, tc[1], tc
        ),
        testdata,
    )
