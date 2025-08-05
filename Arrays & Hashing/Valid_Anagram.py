# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Leetcode 242

"""
PROBLEM ANALYSIS:
- An anagram is a word formed by rearranging the letters of another word
- Two strings are anagrams if they contain the same characters with the same frequencies
- Examples: "listen" and "silent", "evil" and "vile"

APPROACH - Character Frequency Count:
- Use two hash tables (dictionaries) to count character frequencies in both strings
- If both strings have identical character frequency distributions, they are anagrams
- First optimization: if lengths differ, they cannot be anagrams

ALGORITHM WALKTHROUGH:
1. Quick length check - if lengths differ, return False immediately
2. Initialize two empty dictionaries to count character frequencies
3. Iterate through both strings simultaneously (same length guaranteed)
4. For each position:
   - Count frequency of character from string s in dictionary x
   - Count frequency of character from string t in dictionary y
5. Compare the two dictionaries - if identical, strings are anagrams

TIME COMPLEXITY: O(n)
- We iterate through both strings once: O(n) where n is string length
- Dictionary operations (lookup, insertion) are O(1) on average
- Dictionary comparison is O(n) in worst case
- Overall: O(n) where n is the length of the strings

SPACE COMPLEXITY: O(k)
- We store character frequencies in two dictionaries
- k is the number of unique characters (at most 26 for lowercase English letters)
- In practice: O(1) for fixed alphabet size, O(n) in general case

ALTERNATIVE APPROACHES:
1. Sorting: O(n log n) time, O(1) space - sort both strings and compare
2. Single Dictionary: O(n) time, O(k) space - increment for s, decrement for t
3. Counter from collections: O(n) time, O(k) space - more concise but same logic

This two-dictionary approach is clear and optimal for time complexity.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick optimization: if lengths differ, cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Initialize frequency count dictionaries for both strings
        x = {}  # Character frequencies for string s
        y = {}  # Character frequencies for string t
        
        # Iterate through both strings simultaneously (same length guaranteed)
        for i in range(len(s)):
            # Debug prints to visualize the character processing
            print(s[i])
            print(t[i])
            
            # Count frequency of current character in string s
            if s[i] in x:
                x[s[i]] = x[s[i]] + 1  # Increment existing count
            else:
                x[s[i]] = 1  # First occurrence, set count to 1
            
            # Count frequency of current character in string t
            if t[i] in y:
                y[t[i]] = y[t[i]] + 1  # Increment existing count
            else:
                y[t[i]] = 1  # First occurrence, set count to 1
        
        # Compare frequency dictionaries - if identical, strings are anagrams
        return x == y
