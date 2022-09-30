from collections import defaultdict

# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pat = p
        txt = s
        count = []
        M = len(pat)
        N = len(txt)

        # countP[]:  Store count of
        # all characters of pattern
        # countTW[]: Store count of
        # current window of text
        countP = defaultdict(int)

        countTW = defaultdict(int)

        for i in range(M):
            countP[pat[i]] += 1
            countTW[txt[i]] += 1

        # Traverse through remaining
        # characters of pattern
        for i in range(M,N):

            # Compare counts of current
            # window of text with
            # counts of pattern[]
            if countP == countTW:
                count.append(i-M)

            # Add current character to current window
            countTW[ txt[i] ] += 1

            # Remove the first character of previous window
            countTW[ txt[i-M] ] -= 1
            if countTW[ txt[i-M]] == 0:
                del countTW[ txt[i-M]]
            
        # Check for the last window in text   
        if countP == countTW:
            count.append(N-M)
        return count

# Runtime: 249 ms, faster than 53.40% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.2 MB, less than 82.10% of Python3 online submissions for Find All Anagrams in a String.