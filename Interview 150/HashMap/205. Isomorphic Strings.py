class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # count the number of the new characters in order.
        # if the value of the new character is not the same at 
        # the same position, then not isomorphic.
        s_idx, t_idx = 0, 0
        s_set, t_set = {}, {}
        s_compare, t_compare = 0, 0

        for i, j in zip(s, t):
            if i not in s_set:
                s_set[i] = s_idx
                s_compare = s_idx
                s_idx += 1
            else:
                s_compare = s_set[i]


            # print('at j', j, t_idx, t_set)
            if j not in t_set:
                t_set[j] = t_idx
                t_compare = t_idx
                t_idx += 1
            else:
                t_compare = t_set[j]

            # print(s_compare, t_compare)

            if s_compare != t_compare:
                return False
        return True


a = "abc", "abd"
b = "egg", "add"
c = "awfa", "ahbc"
d = "", ""
e = "paper", "title"

tests = [a,b,c,d,e]

for i, j in tests:
    a = Solution().isIsomorphic(i, j)
    print(a)  
    print()