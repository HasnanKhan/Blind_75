#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#Leetcode 49
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for i in strs:
            temp = [0] * 26
            for j in i:
                temp[ord(j) - ord("a")] += 1
            if str(temp) in x:
                x[str(temp)].append(i)
            else:
                x[str(temp)] = [i]
                
        
        return list(x.values())
