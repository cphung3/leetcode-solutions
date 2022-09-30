# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.

# The test cases are generated such that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total): 
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # branch 1: add current value
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # branch 2: don't add current value, skip to next
            cur.pop()
            dfs(i+1, cur, total)
            
        dfs(0, [], 0)
        return res
            