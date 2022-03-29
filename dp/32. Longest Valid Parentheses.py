class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if (s[i] == ')'):
                if (s[i-1] == '('):
                    if i > 2: 
                        dp[i] = dp[i - 2] + 2
                    else: 
                        dp[i] = 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    if (i - dp[i - 1]) >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else: 
                        dp[i] = dp[i - 1] + 2
                maxans = max(maxans, dp[i])
        return maxans
        
# Runtime: 65 ms, faster than 50.04% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 14.2 MB, less than 79.32% of Python3 online submissions for Longest Valid Parentheses.