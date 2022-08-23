

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convertHistogram(word):
            list_str = [0 for i in range(26)]
            for char in word: 
                asc = ord(char) - 97
                if asc > 25: continue
                list_str[asc] += 1
            return list_str

        word_dict = {}
        for word in strs:
            hist = convertHistogram(word)
            word_dict.setdefault([str(hist)], []).append(word)

        return [item for item in word_dict.values()]



