class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # convert nums2 into a dict
        nums2_map = {v:k for k, v in enumerate(nums2)}
        ans = []
        for n in nums1:
            idx = nums2_map[n]
            for subrange in range(idx, len(nums2)):
                if nums2[subrange] > n:
                    ans.append(nums2[subrange])
                    break
            else:
                ans.append(-1)
        return ans

# Runtime: 52 ms, faster than 60.47% of Python3 online submissions for Next Greater Element I.
# Memory Usage: 14.7 MB, less than 14.67% of Python3 online submissions for Next Greater Element I.