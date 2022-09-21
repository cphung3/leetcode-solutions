from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fq= defaultdict( int )
        for w in s:
            fq[w] += 1
        
        for w in t:
            fq[w] -= 1
        vals = set(fq.values())
        return len(vals) == 1 and list(vals)[0] == 0 
        
# Runtime: 96 ms, faster than 31.00% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.5 MB, less than 67.19% of Python3 online submissions for Valid Anagram.