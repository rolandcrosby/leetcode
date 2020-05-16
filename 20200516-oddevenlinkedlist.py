# Odd Even Linked List
# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and
# O(nodes) time complexity.
#
# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
#
# Example 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#
# Note:
# - The relative order inside both the even and odd groups should remain as it was in
#   the input.
# - The first node is considered odd, the second node even and so on ...

import testlib
from listnode import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        odd_head = ListNode(head.val)
        odd_tail = odd_head
        even_head = ListNode(head.next.val)
        even_tail = even_head
        head = head.next.next
        odd = True
        while head is not None:
            if odd:
                odd_tail.next = ListNode(head.val)
                odd_tail = odd_tail.next
            else:
                even_tail.next = ListNode(head.val)
                even_tail = even_tail.next
            head = head.next
            odd = not odd
        odd_tail.next = even_head
        return odd_head


class BetterSolution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == "__main__":
    testdata = [
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            repr(Solution().oddEvenList(ListNode.fromList(tc[0]))),
            repr(ListNode.fromList(tc[1])),
            tc,
        ),
        testdata,
    )
