class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        buildup = "("
        close = 1
        start = 1
        queue = [")"]
        combinations = []
        def recurse(buildup, start, close, queue):
            if close == 0 and start == n:
                combinations.append(buildup) 
                return
            elif abs(close) > n or abs(start) > n:
                return
            
            if queue:
                addRight = buildup + ")"
                queue.pop()
                recurse(addRight, start, close-1, queue)
            
            if not (close < 0 and start < n):
                addLeft = buildup + "("
                queue.append(")")
                recurse(addLeft, start+1, close+1, queue)
        
        recurse(buildup, start, close, queue)
        return combinations

# Runtime: 59 ms, faster than 34.04% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14 MB, less than 99.16% of Python3 online submissions for Generate Parentheses.