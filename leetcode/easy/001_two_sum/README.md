# Two Sum - Easy

## Summary

Given an array of integers, return indices of the two numbers that add up to a specific target.

## Approach

The most efficient approach involves using a hash map (dictionary in Python) to store numbers and their corresponding indices as we iterate through the array. For each number `num` in the array, we calculate its `complement` (i.e., `target - num`). We then check if this `complement` already exists in our hash map. If it does, we have found the two numbers that sum to the target, and we return their indices. If the `complement` is not found, we add the current `num` and its index to the hash map for future lookups.

This method avoids nested loops, significantly improving performance.

## Complexity

- **Time Complexity:** O(n)
  We iterate through the `nums` list once. For each element, dictionary operations (insertion and lookup) take an average time complexity of O(1). Therefore, the overall time complexity is linear with respect to the number of elements in the input list.

- **Space Complexity:** O(n)
  In the worst-case scenario, we might need to store all elements from the `nums` list in the hash map if no two numbers sum up to the target until the very last element. This makes the space complexity linear with respect to the number of elements in the input list.

## Example I/O

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Real-World Value

Mastering the Two Sum problem is crucial for several reasons:

1.  **Hash Map Proficiency:** It's a classic problem that demonstrates the power and efficiency of hash maps (or hash tables) for quick lookups, a fundamental data structure in computer science.
2.  **Interview Staple:** It's one of the most frequently asked questions in coding interviews, serving as a warm-up or a foundational problem to assess a candidate's basic algorithmic thinking and data structure knowledge.
3.  **Foundation for Complex Problems:** The underlying technique of using a hash map for efficient lookups can be extended to solve many more complex problems involving pairs, sums, or frequency counts.
4.  **Optimized Search:** It teaches the concept of optimizing search operations from O(n^2) (brute-force with nested loops) to O(n) using appropriate data structures.

## Next Steps

- Consider variations where there might be multiple valid pairs, or no pairs at all.
- Explore how this problem could be solved if the input array was sorted.
- Think about how to adapt this solution if you needed to find three numbers that sum to a target (3Sum problem).
