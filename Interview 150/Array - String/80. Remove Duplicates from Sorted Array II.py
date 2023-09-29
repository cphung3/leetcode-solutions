class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 2:
            return len(nums)

        currentIndex = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[currentIndex - 2]:
                nums[currentIndex] = nums[i]
                currentIndex += 1

        return currentIndex



nums = [1,1,2]
val = 3

nums = [0,0,1,1,1,1,1,2,2,3,3,4]
val = 2

# nums = [0]
# val = 2

a = Solution().removeDuplicates(nums)
print(nums)  