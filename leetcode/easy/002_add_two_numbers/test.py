import unittest
from solution import ListNode, add_two_numbers

class TestAddTwoNumbers(unittest.TestCase):

    def list_to_linkedlist(self, lst: list) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy_head.next

    def linkedlist_to_list(self, node: ListNode) -> list:
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_example_one(self):
        l1 = self.list_to_linkedlist([2, 4, 3])
        l2 = self.list_to_linkedlist([5, 6, 4])
        expected = self.list_to_linkedlist([7, 0, 8])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), self.linkedlist_to_list(expected))

    def test_example_two(self):
        l1 = self.list_to_linkedlist([0])
        l2 = self.list_to_linkedlist([0])
        expected = self.list_to_linkedlist([0])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), self.linkedlist_to_list(expected))

    def test_example_three(self):
        l1 = self.list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
        l2 = self.list_to_linkedlist([9, 9, 9, 9])
        expected = self.list_to_linkedlist([8, 9, 9, 9, 0, 0, 0, 1])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), self.linkedlist_to_list(expected))

    def test_different_lengths(self):
        l1 = self.list_to_linkedlist([1, 2, 3])
        l2 = self.list_to_linkedlist([9, 8])
        expected = self.list_to_linkedlist([0, 1, 4])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), self.linkedlist_to_list(expected))

    def test_carry_at_end(self):
        l1 = self.list_to_linkedlist([9, 9])
        l2 = self.list_to_linkedlist([1])
        expected = self.list_to_linkedlist([0, 0, 1])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), self.linkedlist_to_list(expected))

    def test_empty_lists(self):
        # Problem constraints state non-empty lists, but for robustness
        l1 = self.list_to_linkedlist([])
        l2 = self.list_to_linkedlist([])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), [])

if __name__ == '__main__':
    unittest.main()
