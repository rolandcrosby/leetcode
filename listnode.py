from typing import List


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
