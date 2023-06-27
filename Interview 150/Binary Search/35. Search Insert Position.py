class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        mid = len(nums)//2

        end = len(nums)
        start = 0
        for i in range(mid):
            if target > nums[mid]:
                start = mid
                mid =  ( end + start )// 2
            elif target < nums[mid]:
                end = mid 
                mid = ( end + start )// 2
            else:
                return mid
        if target == nums[mid]:
            return mid
        
        if target > nums[mid]:
            return mid + 1 
        return mid
            
a = [0,1,2,4,5,7], 4
b = [1,2,3,4], 0
c = [1,3,5,6,7,8], 9
d = [1,3,5], 4
e = [1], 2

tests = [a,b,c,d,e]

for i, j in tests:
    a = Solution().searchInsert(i, j)
    print(a)  
    print()