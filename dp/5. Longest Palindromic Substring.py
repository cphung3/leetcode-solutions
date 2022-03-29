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