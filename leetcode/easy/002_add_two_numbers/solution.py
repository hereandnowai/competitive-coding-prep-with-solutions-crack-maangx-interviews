"""
Solution for LeetCode problem 002: Add Two Numbers.

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Adds two numbers represented by linked lists.

    Args:
        l1: The first linked list.
        l2: The second linked list.

    Returns:
        A new linked list representing the sum of the two numbers.

    Time Complexity: O(max(m, n))
        Where m and n are the lengths of l1 and l2 respectively.
        We iterate through both lists once.

    Space Complexity: O(max(m, n))
        The length of the new list is at most max(m, n) + 1.
    """
    try:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            digit = total_sum % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
    except Exception as e:
        print(f"An error occurred during addition: {e}")
        return None

