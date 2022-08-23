# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(n: int) -> int:
    
    dp = {}
    def recurse(n, memo):
        if n in memo: return memo[n]
        if n == 0 or n == 1:
            return 1
        else: 
            one = recurse(n-1, memo)
            two = recurse(n-2, memo)
            result = one + two
            memo[n] = result
            return result

    ans = recurse(n, dp)
    return ans


a = climbStairs(10)
print(a)