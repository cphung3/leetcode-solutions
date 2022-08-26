class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for k, v in enumerate(nums):
            if v in numDict:
                numDict[v].append(k)
            else:
                numDict[v] = [k]
        ans1,ans2 = 0, 1
        for val in numDict:
            diff = target - val
            if (diff == val and len(numDict[diff]) > 1):
                ans1, ans2 = numDict[diff][0], numDict[diff][1]
                return [ans1, ans2] 
            elif (diff in numDict):
                ans1, ans2 = numDict[diff][0], numDict[val][0]
                if ans1 != ans2:
                    return [ans1, ans2] 

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in prevDict:
                return [prevDict[diff], idx]
            else:
                prevDict[val] = idx
        return []                

# Runtime: 63 ms, faster than 95.29% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 50.22% of Python3 online submissions for Two Sum.
                