# Leetcode 347 - Top K Frequent Elements
#
# PROBLEM ANALYSIS:
# - We are given an integer array nums and an integer k
# - Our task is to return the k elements that occur most frequently in the array
# - The order of the result does not matter
#
# APPROACH - Frequency Dictionary + Sorting:
# - First, count how many times each number appears using a hash table (dictionary)
# - Store each element's frequency in the dictionary with the number as the key and the count as the value
# - Convert the frequency dictionary into a list of [count, number] pairs
# - Sort this list by count (ascending order)
# - Pop elements from the end of the sorted list (highest frequency) until we have k elements
#
# ALGORITHM WALKTHROUGH:
# 1. Initialize an empty dictionary 'count' to store frequencies
# 2. Iterate through nums:
#    - For each number, increment its count in the dictionary
# 3. Create a list 'arr' to store [count, number] pairs from the dictionary
# 4. Sort 'arr' by count (ascending)
# 5. Initialize result list 'res'
# 6. Pop elements from the end of 'arr' (highest count) and append their number to 'res' until res has k elements
# 7. Return 'res'
#
# TIME COMPLEXITY: O(n log n)
# - Counting frequencies: O(n)
# - Sorting the list of unique elements: O(m log m) where m is the number of unique elements (m ≤ n)
# - Overall: O(n log n) in the worst case
#
# SPACE COMPLEXITY: O(n)
# - We store the frequency dictionary and the array of pairs
#
# ALTERNATIVE APPROACHES:
# 1. Heap (Priority Queue) - O(n log k) time: Use a min-heap to keep track of the top k elements without fully sorting
# 2. Bucket Sort - O(n) time: Group numbers by frequency into buckets, then collect top k from the highest frequencies
#
# This sorting-based approach is straightforward and works well when n is not extremely large.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
