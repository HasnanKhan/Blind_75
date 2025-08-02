# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Leetcode 217

"""
PROBLEM ANALYSIS:
- We need to detect if there are any duplicate values in an array
- Return True if duplicates exist, False if all elements are unique

APPROACH - Hash Table (Dictionary):
- Use a hash table to keep track of elements we've seen
- For each element, check if it already exists in our hash table
- If it exists, we found a duplicate - return True immediately
- If we finish the loop without finding duplicates, return False

ALGORITHM WALKTHROUGH:
1. Initialize an empty dictionary to store seen elements
2. Iterate through each element in the array
3. For each element:
   - Check if it's already in our dictionary (seen before)
   - If yes: duplicate found, return True
   - If no: add it to dictionary and continue
4. If loop completes without finding duplicates, return False

TIME COMPLEXITY: O(n)
- We iterate through the array once: O(n)
- Dictionary lookup and insertion are O(1) on average
- Overall: O(n) where n is the length of the array

SPACE COMPLEXITY: O(n)
- In worst case (no duplicates), we store all n elements in the dictionary
- Space grows linearly with input size

ALTERNATIVE APPROACHES:
1. Brute Force: O(n²) time, O(1) space - check every pair
2. Sorting: O(n log n) time, O(1) space - sort then check adjacent elements
3. Set: O(n) time, O(n) space - convert to set and compare lengths

This hash table approach is optimal for time complexity while using reasonable space.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize hash table to track seen elements
        seen = {}
        
        # Iterate through each number in the array
        for num in nums:
            # Check if current number already exists in our hash table
            if num in seen:
                # Duplicate found! Return True immediately
                return True
            else:
                # First time seeing this number, add it to hash table
                # Note: We could store any value, the key is what matters
                seen[num] = True
        
        # Completed iteration without finding duplicates
        return False
