class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # see which of the single digit numbers there are
        all = '23456789'
        single = '2357'
        availableDigits = set()
        isSorted = nums[-1] > nums[0]
        if not isSorted:
            nums.sort()
        for i in all:
            if int(i) in nums:
                availableDigits.add(int(i))
        allSubsets = {}
        twoSubset = set([4,6,8]) & availableDigits
        threeSubset = set([6,9]) & availableDigits

        for key in availableDigits:
            buildup = []
            for n in nums:
                if key % n == 0 or n % key == 0:
                    buildup.append(n)
            allSubsets[key] = buildup
        print(allSubsets)

        for s in allSubsets:
            

        maxlen = []
        for subset in allSubsets.values():
            if len(subset) > len(maxlen):
                maxlen = subset
        return maxlen
        