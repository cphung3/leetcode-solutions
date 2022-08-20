from distutils.command.build import build


class Solution:
    def numDecodings(self, s: str) -> int:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        mapping = {str(i): alpha[i] for i in range(len(alpha))}
        dp = {}
        res = []

        def recurse(idx, buildup):
            if idx >= len(s) - 1:
                res.append(buildup)
                return
            # if idx == len(s) - 1:
            #     return
            
            # dp[idx] = buildup
            if idx + 1 <= len(s) - 1:
                str1 = mapping.get(s[idx: idx+1])
                if str1:
                    recurse(idx+1, buildup + str1)
            if idx + 2 <= len(s) - 1:
                str2 = mapping.get(s[idx: idx+2])
                if str2:
                    recurse(idx+2, buildup + str2)
        recurse(0, res)
        return res


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        if s[0] != '0': 
            dp[1] = 1
        for i in range(2, len(s)+1):
            if int(s[i-1]) >= 1 and int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            second = int(s[i-2:i])
            if second >= 10 and second <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if (i + 1 < len(s)) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                dp[i] += dp[i+2]
        return dp[0]

# Runtime: 39 ms, faster than 82.07% of Python3 online submissions for Decode Ways.
# Memory Usage: 13.9 MB, less than 80.77% of Python3 online submissions for Decode Ways.