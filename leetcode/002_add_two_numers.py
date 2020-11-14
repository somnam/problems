"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[int] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.add_nodes(l1, l2)

    @classmethod
    def node_from_value(cls, value: int):
        nodes = []
        for idx, v in enumerate(str(value)):
            node = nodes[-1] if idx else None
            nodes.append(ListNode(val=int(v), next=node))

        return nodes[-1]

    @classmethod
    def node_to_value(cls, node: ListNode) -> int:
        value = ""
        while node:
            value += str(node.val)
            node = node.next

        return int(value[::-1])

    def add_nodes(self, this, other):
        return self.node_from_value(self.node_to_value(this) + self.node_to_value(other))


class SolutionTest(unittest.TestCase):
    def test_example_1(self):
        # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        # Output: 7 -> 0 -> 8
        # Explanation: 342 + 465 = 807.
        l1 = Solution.node_from_value(342)
        l2 = Solution.node_from_value(465)

        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(807, Solution.node_to_value(result))


if __name__ == '__main__':
    unittest.main()
