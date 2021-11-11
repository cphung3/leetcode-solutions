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