import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l = 0
        r = len(s) - 1
        print(s)

        while l < r:
            a = s[l]
            b = s[r]

            if a != b:
                return False
            l += 1
            r -= 1
        return True

a = "A man, a plan, a canal: Panama"
b = 'sas'
c = 'ab_a'
d = ''
e = ' '

tests = [a,b,c,d,e]

for i in tests:
    a = Solution().isPalindrome(i)
    print(a)  
    print()