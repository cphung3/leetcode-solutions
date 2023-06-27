class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0

        while t_idx < len(t):
            if s_idx > len(s)-1:
                break
            if t[t_idx] == s[s_idx]:
                s_idx += 1
            t_idx += 1
        
        if s_idx >= len(s):
            return True
        return False
    
a = "abc", "ahbgdc"
b = "axc", "ahbgdc"
c = "awfa", "ahbgdc"
d = "", "ahbgdc"
e = "abc", "ahabbabgdc"

tests = [a,b,c,d,e]

for i, j in tests:
    a = Solution().isSubsequence(i, j)
    print(a)  
    print()