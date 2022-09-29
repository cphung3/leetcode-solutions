class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # Treat every character as a possible center 
        # and expand outward from that center
        for i in range(len(s)):
            l, r = i, i

            # odd case, aba
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even case, abba
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

# Runtime: 362 ms, faster than 31.37% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 13.9 MB, less than 75.92% of Python3 online submissions for Palindromic Substrings.