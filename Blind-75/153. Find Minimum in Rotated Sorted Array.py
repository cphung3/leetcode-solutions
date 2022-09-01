class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = nums[0]

        while r >= l:
            mid = (l + r) // 2

            if nums[mid] < minVal:
                minVal = nums[mid]
            
            # left side is sorted 
            # 2,3,6,1,2 so look in the right
            if nums[l] <= nums[mid]:
                # look in right side
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right side is sorted
            # 6,1,2,3,4 so look in the left
            else:
                # look in the left side
                if nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

        return minVal

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while r >= l:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            
            # left side is sorted 
            # 2,3,6,1,2 so look in the right
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return res


# Runtime: 92 ms, faster than 5.13% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.3 MB, less than 23.73% of Python3 online submissions for Find Minimum in Rotated Sorted Array.