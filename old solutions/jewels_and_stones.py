class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for char in J:
            total += S.count(char)
        return total
