class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) == 1): return s
        queue = []
        buildup = ''
        for char in s:
            if len(queue) == 1:
                if char == queue[-1]:
                    buildup += char
                    buildup += queue.pop()
                else:
                    queue.append(char)
            elif len(queue) == 0:
                queue.append(char)            
            else:
                if char == queue[-1]:
                    buildup += char
                    buildup += queue.pop()
                elif char == queue[-2]:
                    buildup += char
                    buildup += queue.pop()
                    buildup += queue.pop()
            print(char, queue, buildup)
        return buildup

a = Solution().longestPalindrome('abba')
print(a)
