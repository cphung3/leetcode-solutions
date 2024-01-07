import math

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        prevVal, nextVal = nums[0], nums[0]
        nextPos = 0
        looped = False
        if k == 0:
            return

        gcf = math.gcd(k, length)
        cycles = length // gcf

        for iters in range(gcf):
            nextPos =  iters%length
            prevVal = nums[iters%length]

            for idx in range(cycles):
                nextPos = (nextPos + k) % (length)
                if looped and nextPos == 0:
                    return nums
                nextVal = nums[nextPos]
                nums[nextPos] = prevVal
                prevVal = nextVal
            looped = True

        return nums
                
a = [-1,-100,3,99], 3
b = [1,20], 3
c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54], 45
d = [1,2,3,4,5,6], 4
e = [1,2,3,4,5,6], 3
f = [1,2,3,4,5,6,7], 3

tests = [a,b,c,e,f]

for i, j in tests:
    ans = Solution().rotate(i, j)
    print(ans)  
    print()
