#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Leetcode 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       x = {}
       for i in range(len(nums)):
        if target - nums[i] in x:
            return [i, x[target - nums[i]]]
        else:
            x[nums[i]] = i
