class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I'       :      1,
            'V'       :      5,
            'X'       :      10,
            'L'       :      50,
            'C'       :      100,
            'D'       :      500,
            'M'       :      1000
        }
        exceptionEnd = set(['V', 'X', 'L', 'C', 'D', 'M'])
        exceptionStart = {
            'I' : {'V': 4, 'X': 9}, 
            'X' : {'L': 40, 'C': 90}, 
            'C' : {'D': 400, 'M': 900}, 
        }
        total = 0
        seenException = False
        seenExceptionChar = ''
        for char in s: 
            if seenException and char in exceptionEnd:
                total += exceptionStart[seenExceptionChar][char]
                seenException = False
                total -= mapping[seenExceptionChar]
            elif char in exceptionStart: 
                seenException = True
                seenExceptionChar = char
                total += mapping[char]
            else:
                total += mapping[char]
        return total

# Runtime: 71 ms, faster than 45.21% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14 MB, less than 72.57% of Python3 online submissions for Roman to Integer.