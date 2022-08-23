
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, begin, end):
            while(begin >= 0 and end <= len(s) - 1 and s[begin] == s[end]):
                begin -= 1
                end += 1
            return s[begin + 1: end]

        if not s or len(s) <= 1:
            return s
        longest = s[0: 1]
        for i, char in enumerate(s):
            temp = expand(s, i, i)
            if (len(temp) > len(longest)):
                longest = temp
            temp = expand(s, i , i + 1)
            if (len(temp) > len(longest)):
                longest = temp

        return longest




'''
const longestPalindrome = s => {
  if(!s || s.length <= 1) {
    return s
  }
  let longest = s.substring(0, 1)
  for(let i = 0; i < s.length; i++) {
    let temp = expand(s, i, i)
    if(temp.length > longest.length) {
      longest = temp
    }
    temp = expand(s, i, i + 1)
    if(temp.length > longest.length) {
      longest = temp
    }
  }
  return longest
}

const expand = (s, begin, end) => {
  while(begin >= 0 && end <= s.length - 1 && s[begin] === s[end]) {
    begin--
    end++
  }
  return s.substring(begin + 1, end)
}
'''