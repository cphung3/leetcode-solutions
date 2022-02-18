class Solution:
    def myAtoi(self, s: str) -> int:
        output = []
        neg = False
        nums = range(48,58)
        minMax = (-2**31, 2**31 - 1)
        signSeen = False
        numberSeen = False
        for char in s:
            if char == " ":
                if not signSeen and not numberSeen:
                    continue
                else: break
            elif char == "-":
                if not signSeen and not numberSeen:
                    signSeen = True
                    neg = True
                else:
                    break
            elif char == "+":
                if not signSeen and not numberSeen:
                    signSeen = True
                else:
                    break
            elif ord(char) in nums:
                # print('inp = ', char, ord(char), nums)
                numberSeen = True
                output.append(char)
            else: 
                break
        if not output:
            return 0
        outputString = ""
        for s in output:
            outputString += s
        if neg: outputString = '-' + outputString
        if float(outputString) < minMax[0]:
            outputNum = minMax[0]
        elif float(outputString) > minMax[1]:
            outputNum = minMax[1]
        else:
            outputNum = int(outputString)
        # print()
        
        return outputNum

# Runtime: 28 ms, faster than 97.78% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 13.9 MB, less than 83.22% of Python3 online submissions for String to Integer (atoi).