class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        wordList.reverse()
        return " ".join(wordList)

# Runtime: 55 ms, faster than 21.85% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 14.3 MB, less than 86.78% of Python3 online submissions for Reverse Words in a String.