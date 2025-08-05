#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#Leetcode 242

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = {}
        y = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            print(s[i])
            print(t[i])
            if s[i] in x:
                x[s[i]] = x[s[i]] + 1
            else:
                x[s[i]] = 1
            if t[i] in y:
                y[t[i]] = y[t[i]] + 1
            else:
                y[t[i]] = 1
        return x == y
