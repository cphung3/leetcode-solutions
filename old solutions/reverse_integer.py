class Solution:
    def reverse(self, x: int) -> int:
        # if abs(x) >= 2**31:
        #     return 0
        if x < 0:
            ans = -int("".join(reversed(str(abs(x)))))
            if abs(ans) >= 2**31:
                return 0
        else:
            ans = int("".join(reversed(str(x))))
            if abs(ans) >= 2**31:
                return 0
        return ans
