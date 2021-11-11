class Solution:
    def reverse(self, x: int) -> int:
        if (x == 0): return 0
        neg = x < 0
        string = str(x).rstrip('0').lstrip('-')
        string = string[::-1]
        returnVal = int(string)
        if (returnVal > 2**31 - 1 or returnVal < -2**31):
            return 0
        if (neg):
            returnVal = -1 * returnVal
        return returnVal

# Runtime: 23 ms, faster than 97.87% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.3 MB, less than 43.58% of Python3 online submissions for Reverse Integer.