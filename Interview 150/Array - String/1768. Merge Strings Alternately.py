class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))

        buildup = ''
        for i in range(min_len):
            buildup += word1[i]
            buildup += word2[i]
        
        if len(word1) < len(word2):
            buildup += word2[min_len:]  
        else:
            buildup += word1[min_len:]  
        return buildup