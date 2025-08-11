# Leetcode 49 - Group Anagrams
# 
# PROBLEM ANALYSIS:
# - We are given an array of strings, and we need to group words that are anagrams of each other
# - An anagram means two words have exactly the same letters with the same frequency, but possibly in a different order
# - We must return a list of groups, where each group contains words that are anagrams
#
# APPROACH - Hash Table with Character Count as Key:
# - For each word, we can represent it by a fixed-length array of size 26 (for each lowercase English letter)
# - Each position in the array stores the count of that letter in the word
# - Example: "eat" → [1,0,0,0,1,0,...,1] (1 'a', 1 'e', 1 't')
# - This array acts as a unique identifier for all words that are anagrams of each other
# - Use a dictionary to group words by this identifier
# - Convert the array to a string (or tuple) to use it as a hashable dictionary key
#
# ALGORITHM WALKTHROUGH:
# 1. Initialize an empty dictionary to store groups
# 2. For each word in the input list:
#    - Create a frequency array of length 26 initialized with zeros
#    - For each character in the word, increment the correct index in the frequency array
#    - Convert the frequency array into a string (or tuple) to be a dictionary key
#    - If the key exists in the dictionary, append the word to that list
#    - If not, create a new entry with the word in a new list
# 3. Return all grouped values from the dictionary
#
# TIME COMPLEXITY: O(n * k)
# - n = number of words
# - k = maximum length of a single word
# - For each word, we build a 26-length array (O(k)) and update the dictionary (O(1) average)
#
# SPACE COMPLEXITY: O(n * k)
# - We store all words and their groupings in the dictionary
# - The key (character count array) uses constant space (26), so extra space depends on storing the words
#
# ALTERNATIVE APPROACHES:
# 1. Sorting each word: Sort characters in each word to create a key; O(k log k) per word
# 2. Prime number multiplication mapping: Assign each letter a prime number and use the product as the key
#
# This character count hash approach avoids sorting, making it faster for long words.

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
