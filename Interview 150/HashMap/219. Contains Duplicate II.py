class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        ans = False
        for idx, j in enumerate(nums):
            if j in hash:
                ans = abs(hash[j] - idx) <= k
                if ans:
                    return ans
            hash[j] = idx
        return ans 