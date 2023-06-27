class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for i in magazine:
            count[i] = count.get(i, 0) + 1
        
        for j in ransomNote:
            if j not in count or count[j] == 0:
                return False
            count[j] -= 1
        return True
            