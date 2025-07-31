#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Leetcode 217
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for i in nums:
            if i in x:
                return True
            else:
                x[i] = i
        return False
