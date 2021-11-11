class Trie:

    def __init__(self):
        self.tree = {}
        self.dictionary = set()
        

    def insert(self, word: str) -> None:
        node = self.tree
        for char in word:
            leaf = {}
            if char in node:
                leaf = node[char]
            else:
                node[char] = leaf
            node = leaf
        self.dictionary.add(word)

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
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Runtime: 124 ms, faster than 96.48% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 27.6 MB, less than 94.02% of Python3 online submissions for Implement Trie (Prefix Tree).
# Next challenges: