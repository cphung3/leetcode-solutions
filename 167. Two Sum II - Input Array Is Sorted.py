class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while r >= l:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]            
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
        return

# Runtime: 349 ms, faster than 5.04% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 14.8 MB, less than 99.26% of Python3 online submissions for Two Sum II - Input Array Is Sorted.