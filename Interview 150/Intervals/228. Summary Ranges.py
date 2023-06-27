class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        l = 0
        r = 0
        ans = []
        temp = 0

        for r, n in enumerate(nums):
            if n == nums[temp]:
                pass
            elif n == nums[temp] + 1:
                pass
            else:
                a, b = nums[l], nums[temp]
                if a == b:
                    interval = "{}".format(a)
                else:
                    interval = "{}->{}".format(a,b)
                ans.append(interval)
                l = r
            temp = r

        if r == len(nums) - 1:
            a, b = nums[l], nums[r]
            if a == b:
                interval = "{}".format(a)
            else:
                interval = "{}->{}".format(a,b)
            ans.append(interval)
        return ans
    
a = [0,1,2,4,5,7]
b = [0,1,2,4,5,7,9]
c = [0,2,3,68,80,90]
d = [0,1000]
e = []

tests = [a,b,c,d,e]

for i in tests:
    a = Solution().summaryRanges(i)
    print(a)  
    print()