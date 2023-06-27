class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


l1 = [7,8,9,0,0,0]
l2 = [2,5,6]

# l1 = [2, 0]
# l2 = [1]

# l1 = [4,0,0,0,0,0]
# l2 = [1,2,3,5,6]

# l1 = [0,0,3,0,0,0,0,0,0]
# l2 = [-1,1,1,1,2,3]

a = Solution().merge(l1, 3, l2, 3)
print(l1)