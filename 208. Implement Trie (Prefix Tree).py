class Trie:
    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        node = self.tree
        node['isEnd'] = False
        for char in word:
            leaf = { 'isEnd': False }
            if char in node:
                leaf = node[char]
            else:
                node[char] = leaf
            node = leaf
        node['isEnd'] = True

    def search(self, word: str) -> bool:
        return word in self.dictionary

    def startsWith(self, prefix: str) -> bool:
        node = self.tree
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
# obj.insert('word')
# obj.insert('wor')
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# print(obj.tree)
import json 

with open('corncob_words.txt') as topo_file:
    for line in topo_file:
        # print(line.rstrip('\n'))  # The comma to suppress the extra new line char
        obj.insert(line.rstrip('\n'))

with open("dictionary_words.json", "w") as outfile:
    json.dump(obj.tree, outfile)

# Runtime: 124 ms, faster than 96.48% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 27.6 MB, less than 94.02% of Python3 online submissions for Implement Trie (Prefix Tree).
# Next challenges: