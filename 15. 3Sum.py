# class Solution:
#     def threeSum(self, nums):
#         num_indices = {}
#         results = []
#         ans_set = set()
#         # get how many times a number occurs
#         for idx, val in enumerate(nums):
#             if val in num_indices:
#                 num_indices[val].append(idx)
#             else:
#                 num_indices[val] = [idx]
#         for first in range(len(nums)-1):
#             for second in range(first+1, len(nums)):
#                 a = nums[first]

#                 b = nums[second]

#                 first_two_sum = a + b
#                 c = -1*first_two_sum
#                 added = False
#                 if c in num_indices:
#                     for indx in num_indices[c]:
#                         if indx != first and indx != second:
#                             break
#                         else:
#                             added = True
#                         # print("indices", idx, first, second, added)
#                     if not added:
#                         for answers in results:
#                             if set([a,b,c]) == set(answers):
#                                 added = True
#                                 break
#                     if not added:
#                         results.append([a,b,c])

#                 # print(a,b,c,results,num_indices)
#         return results

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        ls = len(nums)
        for i, x in enumerate(nums):
            # not first value and same value as before
            # don't reuse the same value
            if i > 0 and x == nums[i-1]:
                continue
            l, r = i + 1, ls - 1
            while l < r:
                if nums[l] + nums[r] == -x:
                    res.append([x, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1        
                elif nums[l] + nums[r] < -x:
                    l += 1
                else:
                    r -= 1
        return res

nums = [-1,0,1,2,-1,-4]
nums2 = [-2, 0, 0, 2, 2]
nums3 = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
nums4 = [0,0,0]
ans = Solution().threeSum(nums3)
print(ans)

# Runtime: 1060 ms, faster than 53.52% of Python3 online submissions for 3Sum.
# Memory Usage: 17.5 MB, less than 74.28% of Python3 online submissions for 3Sum.

# Runtime: 1501 ms, faster than 42.76% of Python3 online submissions for 3Sum.
# Memory Usage: 18.1 MB, less than 39.52% of Python3 online submissions for 3Sum.