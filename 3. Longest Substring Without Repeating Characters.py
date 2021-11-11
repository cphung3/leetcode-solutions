class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unseenChars = set()
        allLengths = set()
        count = 0
        for char in s:
            if char in unseenChars:
                unseenChars = set()
                allLengths.add(count)
                count = 0

            unseenChars.add(char)
            count += 1
        allLengths.add(count)
        return max(allLengths)
