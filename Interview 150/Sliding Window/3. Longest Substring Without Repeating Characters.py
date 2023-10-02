class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, curSum, l = 0, 0, 0
        visited = set()
        
        for r, n in enumerate(s):
            curSum += 1
            # print('before: ', n, visited, res, l)
            while n in visited and l <= r:
                visited.remove(s[l])
                # res = max(res, r - l + 1)
                curSum -= 1
                l +=1
            # print('after: ', n, visited, res, l)
            visited.add(n)
            res = max(res, r - l + 1)
        return res % (len(s)+1) or curSum
    
a ="abcabcbb"
b ="bbbbb"
c = "pwwkew"
d = "au"
e = "aab"
f = " "

tests = [a,b,c,d,e,f]

for i in tests:
    ans = Solution().lengthOfLongestSubstring(i)
    print(ans)  
    print()