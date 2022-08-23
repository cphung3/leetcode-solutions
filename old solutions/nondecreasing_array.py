class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        first = False
        # high = nums[0]
        prev = nums[0]
        split = nums[0]
        high = -float('inf')
        size = 1
        for i in range(1,len(nums)):
            if nums[i] >= high:
                high = nums[i]
            if nums[i] < prev:
                if first and i != 1:
                    return False
                first = True
                split = prev
                # if nums[i] < halfMin:
                #     halfMin = nums[i]
            else:
                if first:
                    if nums[i] < high and size != 1:
                        print(split, high)
                        if split != high:
                            return False
                else:
                    size += 1
            # if not first:

            prev = nums[i]
        # if high > halfMin: return False
        return True

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        prev = nums[0]
        forw = nums[-1]
        for i in range(1, len(nums)):
            if nums[i] < prev:
                nums[i-1] = nums[i]
            prev = nums[i]
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < prev:
                return False
            prev = nums[i]
        return True
