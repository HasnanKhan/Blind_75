# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Leetcode 1

"""
PROBLEM ANALYSIS:
- We need to find TWO numbers in an array that add up to a target value
- Return the INDICES of these two numbers, not the numbers themselves
- We can assume there's exactly one solution and can't use the same element twice

APPROACH - Hash Table (Dictionary):
- Use a hash table to store numbers we've seen and their indices
- For each number, calculate what its "complement" would need to be (target - current_number)
- Check if this complement already exists in our hash table
- If it exists, we found our pair - return both indices
- If not, store current number and its index for future lookups

ALGORITHM WALKTHROUGH:
1. Initialize an empty dictionary to store {number: index} pairs
2. Iterate through array with both index and value
3. For each element:
   - Calculate complement = target - current_number
   - Check if complement exists in our dictionary
   - If yes: return [current_index, stored_index_of_complement]
   - If no: store current_number and its index in dictionary
4. Continue until we find the pair (guaranteed by problem constraints)

EXAMPLE: nums = [2,7,11,15], target = 9
- i=0, nums[0]=2: complement = 9-2 = 7, not in dict yet, store {2: 0}
- i=1, nums[1]=7: complement = 9-7 = 2, found 2 in dict at index 0, return [1, 0]

TIME COMPLEXITY: O(n)
- We iterate through the array once: O(n)
- Dictionary lookup and insertion are O(1) on average
- Overall: O(n) where n is the length of the array

SPACE COMPLEXITY: O(n)
- In worst case, we might store nearly all elements before finding the pair
- Space grows linearly with input size

ALTERNATIVE APPROACHES:
1. Brute Force: O(n²) time, O(1) space - check every pair of numbers
2. Two Pointers: O(n log n) time, O(1) space - sort first, but loses original indices
3. This hash table approach is optimal for both time and preserving indices

Why this approach is optimal:
- Maintains original indices (required by problem)
- Single pass through array
- Immediate termination when solution found
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize hash table to store {number: index} pairs
        # Key: number value, Value: its index in original array
        x = {}
        
        # Iterate through array with both index and value
        for i in range(len(nums)):
            # Calculate what number we need to complete the target sum
            complement = target - nums[i]
            
            # Check if complement already exists in our hash table
            if complement in x:
                # Found our pair! Return current index and stored index
                # Note: x[complement] gives us the index where complement was found
                return [i, x[complement]]
            else:
                # Haven't found complement yet, store current number and its index
                # This allows future iterations to find this number as their complement
                x[nums[i]] = i
