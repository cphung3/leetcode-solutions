class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_num = str(x)
        rev = string_num[::-1]
        return string_num == rev


ans = Solution().isPalindrome(1001)
print(ans)

# Runtime: 64 ms, faster than 64.31% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.3 MB, less than 15.77% of Python3 online submissions for Palindrome Number.