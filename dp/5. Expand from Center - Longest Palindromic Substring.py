class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        res = ""
        dp = [None for i in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                    dp[i] = True
                elif j == i+1:
                    dp[i] = (s[i] == s[j])
                else:
                    dp[i] = (dp[i+1] and s[i] == s[j])
                if dp[i] and j - i + 1 > len(res):
                    res = s[i:j+1]
                # print('op = ', dp, res, j, i)
        return res

# https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome#solution-3
# Runtime: 7369 ms, faster than 9.49% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14 MB, less than 81.78% of Python3 online submissions for Longest Palindromic Substring.
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        # Treat every character as a possible center 
        # and expand outward from that center
        for i in range(len(s)):
            l, r = i, i

            # odd case, aba
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even case, abba
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

# Runtime: 701 ms, faster than 81.08% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.9 MB, less than 89.82% of Python3 online submissions for Longest Palindromic Substring.