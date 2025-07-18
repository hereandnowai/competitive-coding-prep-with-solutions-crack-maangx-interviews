"""
Solution for LeetCode problem 001: Two Sum.

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
This solution uses a hash map (dictionary in Python) to store numbers and their indices, allowing for efficient lookups.
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Finds two numbers in the list that add up to the target.

    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        A list containing the indices of the two numbers that sum to target.
        Returns an empty list if no such pair is found (though problem states
        exactly one solution exists).

    Time Complexity: O(n)
        We iterate through the list once. For each element, we perform a
        dictionary lookup and insertion, both of which take O(1) on average.

    Space Complexity: O(n)
        In the worst case, we store all n elements in the hash map.
    """
    try:
        num_map = {}  # Dictionary to store number: index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                # If the complement exists in the map, we found the pair
                return [num_map[complement], i]
            # Otherwise, add the current number and its index to the map
            num_map[num] = i
        return [] # Should not be reached based on problem constraints
    except TypeError:
        raise TypeError("Input 'nums' must be a list of integers and 'target' an integer.")
    except Exception as e:
        # Catch any other unexpected errors during execution
        print(f"An unexpected error occurred: {e}")
        return []

