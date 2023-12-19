import itertools

class Solution:
    # def __init__(self):
    #     self.tree = {}

    # def insert(self, word: str) -> None:
    #     node = self.tree
    #     node['isEnd'] = False
    #     for char in word:
    #         leaf = { 'isEnd': False }
    #         if char in node:
    #             leaf = node[char]
    #         else:
    #             node[char] = leaf
    #         node = leaf
    #     node['isEnd'] = True

    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # permut = list(map(lambda item: "".join(item), list(itertools.permutations(words))))
        # print(permut)
        for word in words:
            self.insert(word)
        subLength = len("".join(words))
        indices = []
        # print(self.tree)

        for r, char in enumerate(s):
            nextNode = self.tree.get(char, None)    
            counter = 0

            while nextNode and counter <= subLength and r + counter < len(s)-1:
                counter += 1
                nextChar = s[r + counter]
                nextNode = nextNode.get(nextChar, None)
    
            if counter == subLength:
                indices.append(r)
            elif nextNode:
                if (counter == subLength - 1 and nextNode['isEnd']):
                    indices.append(r)

        
        return indices
    
a = 'barfoothefoobarman', ["foo","bar"]
b = "wordgoodgoodgoodbestword", ["word","good","best","word"]
c = "barfoofoobarthefoobarman", ["bar","foo","the"]
d = "wordgoodgoodgoodbestword", ["word","good","best","good"]


# e = 11, [1,2,3,4,5]

tests = [a,b,c,d]

for i, j in tests:
    ans = Solution().findSubstring(i, j)
    print(ans)  
    print()