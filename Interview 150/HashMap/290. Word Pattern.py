class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        countPattern = {}
        orderPattern = []
        idxPattern = 0

        countString = {}
        idxString = 0
        for i in pattern:
            if i not in countPattern:
                countPattern[i] = idxPattern
                idxPattern += 1
            orderPattern.append(countPattern.get(i))

        stringList = s.split(' ')
        if len(stringList) != len(pattern):
            return False
        for idx, j in enumerate(stringList):
            if j not in countString:
                countString[j] = idxString
                idxString += 1
            if orderPattern[idx] != countString.get(j):
                return False
        return True
            