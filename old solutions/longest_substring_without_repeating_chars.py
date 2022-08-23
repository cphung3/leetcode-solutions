'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         #keep a dict of seen chars
#         seen = {}

#         #track longest length
#         lengths = set([])
#         max_length = 0
#         if not s: return 0

#         #iterate over string
#         pos = 0
#         start_sub = 0
#         seen[s[0]] = 0

#         for char in range(1, len(s)):
#             if s[char] not in seen: 
#                 seen[s[char]] = char
#             else: 
#                 previous_occ = seen[s[char]]

#                 if previous_occ >= start_sub: 
#                     curr_len = char - start_sub
#                     if curr_len > max_length: 
#                         max_length = curr_len
#                     start_sub = previous_occ + 1
#                 seen[s[char]] = char

#         if max_length < char - start_sub:
#             max_length = char - start_sub

#         return max_length


'''
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            // try to extend the range [i, j]
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                set.remove(s.charAt(i++));
            }
        }
        return ans;
    }
}

'''


def lengthOfLongestSubstring(s):
    d,m,c,st={},0,0,0
    for i, e in enumerate(s): 
        # if char already seen start substring idx < seen char
        if e in d and d[e]>=st: 
            # take the max of the max length and the current substring length
            # current substring length = current index - length of previous char
            # starting substring becomes the start of the seen char +1 (ie the next char)
            m,c,st=max(m,c),i-d[e],d[e]+1
            print(m, c, st)
        # if not seen before, add the char to the current substring len
        else: c+=1
        # set the char's last seen in the dict to the current index
        d[e]=i
    return max(m,c)

print(lengthOfLongestSubstring("abcabcbb"))