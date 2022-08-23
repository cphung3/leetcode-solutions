class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -float('inf')
        second = -float('inf')
        third = -float('inf')

        for i in nums:
            if i > third and second != -float('inf'):
                if i < second:
                    third = i
                else:
                    if i != second:
                        third = second
            if i > second and first != -float('inf'):
                if i < first:
                    second = i
                else:
                    if i != first:
                        second = first
            if i > first:
                first = i

        if third != -float('inf'):
            return third
        return max(nums)
