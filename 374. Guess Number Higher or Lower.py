# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def __init__(self, ans) -> None:
        self.ans = ans

    def guess(self, n):
        if n < self.ans:
            return 1
        elif n > self.ans:
            return -1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        hint = self.guess(n//2)
        ans = n//2
        prev_high = n
        prev_low = 1
        new_guess = ans
        while(hint != 0):
            if hint == 1:
                # guess higher
                prev_low = new_guess
                new_guess = (prev_low + prev_high + 1)//2
                print('newguess: ', new_guess, prev_high, prev_low)
                hint = self.guess(new_guess)
            elif hint == -1:
                # guess lower
                prev_high = new_guess
                new_guess = (prev_low + prev_high)//2
                hint = self.guess(new_guess)
            print(new_guess, hint, ans, prev_high, prev_low)
        return new_guess

a = Solution(1).guessNumber(2)
print(a)

# Runtime: 26 ms, faster than 84.24% of Python3 online submissions for Guess Number Higher or Lower.
# Memory Usage: 14.4 MB, less than 10.22% of Python3 online submissions for Guess Number Higher or Lower.