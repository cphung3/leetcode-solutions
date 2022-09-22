class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.dictionary = set()

    def addWord(self, word: str) -> None:
        node = self.trie
        for idx, char in enumerate(word):
            leaf = {}
            if idx == len(word) - 1:
                leaf = {'!': {}}
            if char in node:
                leaf = node[char]
            else:
                node[char] = leaf
            node = leaf
        self.dictionary.add(word)

    def search(self, word: str) -> bool:
        # print()
        # print("new search: ", word)        
        if '.' in word:
            return self.startsWith(word)
        return word in self.dictionary

    def startsWith(self, prefix, node=None) -> bool:
        # print('is node falsy', node is None, node)
        if node is None: node = self.trie
        for idx, char in enumerate(prefix):
            # print('outside: ', idx, char, prefix, node)
            if char == '.':
                # loop through all the characters we have
                for start in node:
                    if start == "!": continue
                    # no more letters but we still have possible characters
                    # print('passing into new start node', start, idx + 1 > len(prefix)-1, '.' not in node[start], prefix[idx+1:], node[start])
                    if idx + 1 > len(prefix)-1 and '!' not in node[start]:
                        return False

                    res = self.startsWith(prefix[idx+1:], node[start])
                    # print(start, res, char, idx, prefix[idx+1:], node[start])
                    if res:
                        return True
                return False
            if char in node:
                node = node[char]
            else:
                return False
        return True


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)