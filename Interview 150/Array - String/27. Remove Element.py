# class Solution:
#     def removeElement(self, nums, val) -> int:
#         pointer = 0
#         end = len(nums) - 1
#         if pointer == end:
#             # print(nums, pointer)
#             return 1 if nums[pointer] != val else 0
#         while pointer < end:
#             num = nums[pointer]
#             endVal = nums[end]
#             if num == val:
#                 while endVal == val:
#                     end -= 1
#                     endVal = nums[end]
#                 else:
#                     nums[pointer], nums[end] = nums[end], nums[pointer]
#             pointer += 1
#         # print(nums, pointer)
#         return pointer

class Solution:
    def removeElement(self, nums, val) -> int:
        newList = nums
        count = 0
        original = 0
        for idx, i in enumerate(newList):
            if i != val:
                nums[original] = i
                count += 1
                original += 1
            # print(newList, nums, i, idx)
        return count
    
class Solution2:
    def removeElement(self, nums, val) -> int:
        pointer = 0
        for idx, i in enumerate(nums):
            if i != val:
                temp = nums[pointer]
                nums[pointer] = i
                nums[idx] = temp
                pointer += 1
            # print(newList, nums, i, idx)
        # print(nums)
        return pointer
            
            

nums = [3,2,2,3]
val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

# nums = [0]
# val = 2

a = Solution2().removeElement(nums, val)
print(a)  