# Delete Node in a Linked List
# Write a function to delete a node (except the tail) in a singly linked list, given
# only access to that node.
#
# Given linked list -- head = [4,5,1,9], which looks like following:
# 4 -> 5 -> 1 -> 9
#
# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become
# 4 -> 1 -> 9 after calling your function.
#
# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become
# 4 -> 5 -> 9 after calling your function.
#
# Note:
# - The linked list will have at least two elements.
# - All of the nodes' values will be unique.
# - The given node will not be the tail and it will always be a valid node of the linked
#   list.
# - Do not return anything from your function.

import testlib
from listnode import ListNode
from typing import List, Tuple


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next


def run_test_case(t: testlib.unittest.TestCase, tc: Tuple[List[int], int, List[int]]):
    head = ListNode.fromList(tc[0])
    el_to_remove = head
    for _ in range(tc[1]):
        el_to_remove = el_to_remove.next
    Solution().deleteNode(el_to_remove)
    t.assertEqual(repr(head), repr(ListNode.fromList(tc[2])))


if __name__ == "__main__":
    testdata = [
        ([4, 5, 1, 9], 1, [4, 1, 9]),
        ([4, 5, 1, 9], 2, [4, 5, 9]),
        ([2, 0, 1, 3], 0, [0, 1, 3]),
    ]
    testlib.run(run_test_case, testdata)
