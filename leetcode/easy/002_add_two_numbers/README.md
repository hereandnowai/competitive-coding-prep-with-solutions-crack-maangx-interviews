# Add Two Numbers - Medium

## Summary

Given two non-empty linked lists representing two non-negative integers with digits stored in reverse order, add the two numbers and return the sum as a linked list.

## Approach

The problem can be solved by simulating the process of adding two numbers digit by digit, starting from the least significant digit. Since the digits are stored in reverse order, this naturally aligns with how we perform addition from right to left.

We initialize a `dummy_head` node to simplify the handling of the new linked list and a `current` pointer to traverse and build the result list. We also maintain a `carry` variable, initialized to 0.

We iterate as long as there are digits in either of the input linked lists (`l1` or `l2`) or if there's a `carry` from the previous addition. In each iteration:
1.  We retrieve the value of the current digit from `l1` and `l2`. If a list has been exhausted, we consider its value as 0.
2.  We calculate the `total_sum` of the current digits from `l1`, `l2`, and the `carry` from the previous step.
3.  The new `carry` is determined by `total_sum // 10` (integer division).
4.  The `digit` to be placed in the new linked list node is `total_sum % 10` (remainder).
5.  A new `ListNode` with this `digit` is created and appended to the `current.next`.
6.  The `current` pointer is moved to the newly created node.
7.  We advance `l1` and `l2` to their next nodes if they exist.

Finally, we return `dummy_head.next`, which points to the beginning of the sum linked list.

## Complexity

- **Time Complexity:** O(max(m, n))
  Where `m` and `n` are the lengths of the linked lists `l1` and `l2` respectively. We traverse each linked list at most once. The operations inside the loop (addition, modulo, division, node creation) are all constant time operations.

- **Space Complexity:** O(max(m, n))
  The space complexity is determined by the length of the new linked list created to store the sum. In the worst case, the sum linked list can have `max(m, n) + 1` nodes (if there's a final carry). Thus, the space required is proportional to the length of the longer input list.

## Example I/O

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

## Real-World Value

This problem, while seemingly abstract, reinforces several fundamental computer science concepts:

1.  **Linked List Manipulation:** It provides excellent practice in traversing, creating, and manipulating linked list nodes, which are common operations in data structures.
2.  **Arithmetic Simulation:** It demonstrates how basic arithmetic operations (like addition) can be simulated using fundamental programming constructs, which is relevant in areas like arbitrary-precision arithmetic.
3.  **Handling Edge Cases:** It requires careful consideration of edge cases such as different list lengths and handling the final carry, which are crucial skills for robust software development.
4.  **Iterative Problem Solving:** The iterative approach with a `carry` variable is a common pattern for problems that involve accumulating results over a sequence.

## Next Steps

- Consider how you would solve this problem if the digits were stored in forward order.
- Explore how to handle negative numbers in this linked list representation.
- Implement subtraction or multiplication of linked list numbers.
