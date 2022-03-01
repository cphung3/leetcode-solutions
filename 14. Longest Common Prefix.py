class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        minLen = min([len(s) for s in strs])
        for idx in range(minLen):
            seqPreserved = False
            curChar = ""
            for s in strs:
                char = s[idx]
                # print(curChar)
                if len(curChar) != 0 and char == curChar:
                    seqPreserved = True
                elif len(curChar) != 0 and char != curChar:
                    seqPreserved = False
                    break
                elif len(curChar) == 0:
                    seqPreserved = True
                    curChar = char
                else:
                    break
                    
            # print(curChar, seqPreserved, char, idx)
            if seqPreserved:
                output += curChar
                curChar = ""
            else:
                break
        # print()
        return output

        
# Runtime: 41 ms, faster than 65.53% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14 MB, less than 80.10% of Python3 online submissions for Longest Common Prefix.