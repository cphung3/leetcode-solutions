class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        r = 0
        total = 0
        minSize = 0
        
        while l < len(nums):
            val = nums[r]
            total += val
            if total >= target:
                #backtrack to see if the length can be shorter
                while total >= target:
                    total -= nums[l]
                    l += 1

                l -= 1
                total += nums[l]
                if minSize != 0:
                   minSize = min(minSize, r-l+1)
                else:
                    minSize = r-l + 1
                if minSize == 1:
                    return minSize
            r += 1

            if r >= len(nums):
                break

        return minSize
    
class Solution2:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res, curSum, l = len(nums)+1, 0, 0
        
        for r, n in enumerate(nums):
            curSum += n
            while curSum >= target and l <=r:
                res = min(res, r - l + 1)
                curSum -=nums[l]
                l +=1

        return res % (len(nums)+1)
    
a = 7, [2,3,1,2,4,3]
b = 4, [1,4,4]
c = 11, [1,1,1,1,1,1,1,1]
d = 80, [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
e = 11, [1,2,3,4,5]

tests = [a,b,c,d,e]

for i, j in tests:
    ans = Solution().minSubArrayLen(i, j)
    print(ans)  
    print()