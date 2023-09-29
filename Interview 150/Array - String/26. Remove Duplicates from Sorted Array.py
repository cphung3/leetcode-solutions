class Solution:
    def removeDuplicates(self, nums) -> int:
        pointer = 1
        previous = nums[0]
        for idx, i in enumerate(nums):
            if i != previous:
                temp = nums[pointer]
                nums[pointer] = i
                nums[idx] = temp
                pointer += 1
            previous = i
        return pointer

class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) <= 1:
            return len(nums)

        currentIndex = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[currentIndex - 1]:
                nums[currentIndex] = nums[i]
                currentIndex += 1

        return currentIndex



nums = [1,1,2]
val = 3

nums = [0,0,1,1,1,2,2,3,3,4]
val = 2

# nums = [0]
# val = 2

a = Solution().removeDuplicates(nums)
print(nums)  