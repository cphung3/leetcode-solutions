class Trie:
    def __init__(self) -> None:
        self.children = {}
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['EOW'] = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.values():
                        if child == 'EOW': continue
                        if dfs(i+1, cur[child]):
                            return True
                    return False
                else:
                    if c not in cur:
                        return False
                    cur = cur[c]
            return 'EOW' in cur
        return dfs(0, self.root)

    # def startsWith(self, prefix, node=None) -> bool:
        # print('is node falsy', node is None, node)
        # if node is None: node = self.trie
        # for idx, char in enumerate(prefix):
        #     # print('outside: ', idx, char, prefix, node)
        #     if char == '.':
        #         # loop through all the characters we have
        #         for start in node:
        #             if start == "!": continue
        #             # no more letters but we still have possible characters
        #             # print('passing into new start node', start, idx + 1 > len(prefix)-1, '.' not in node[start], prefix[idx+1:], node[start])
        #             if idx + 1 > len(prefix)-1 and '!' not in node[start]:
        #                 return False

        #             res = self.startsWith(prefix[idx+1:], node[start])
        #             # print(start, res, char, idx, prefix[idx+1:], node[start])
        #             if res:
        #                 return True
        #         return False
        #     if char in node:
        #         node = node[char]
        #     else:
        #         return False
        # return True


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['EOW'] = True
        # print(self.root)

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.values():
                        # print(child, cur, cur.values())
                        if child == True: continue
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur:
                        return False
                    cur = cur[c]
            return 'EOW' in cur
        return dfs(0, self.root)