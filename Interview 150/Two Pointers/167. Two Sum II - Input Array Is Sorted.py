class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            lval = numbers[l]
            rval = numbers[r]
            total = lval + rval

            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1
        return []