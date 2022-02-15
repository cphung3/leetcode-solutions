class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0 # Current index of input array nums1[] 
        j = 0 # Current index of input array nums2[] 
        m1, m2 = -1, -1 
        even = (m + n) % 2 == 0
    
        # Since there are (n+m) elements, 
        # There are following two cases 
        # if n+m is odd then the middle 
        # index is median i.e. (m+n)/2 
        for count in range(((n + m) // 2) + 1) :
            m2 = m1     
            
            if(i != n and j != m) :            
                if nums1[i] > nums2[j] :
                    m1 = nums2[j]
                    j += 1
                else :
                    m1 = nums1[i]
                    i += 1            
            elif(i < n) :            
                m1 = nums1[i]
                i += 1
        
            # for case when j<m, 
            else:            
                m1 = nums2[j]
                j += 1        
        #     print('m1m2', m1, m2, i, j)
        # print()
        if even: return (m1+m2)/2
        return m1

# Runtime: 121 ms, faster than 54.12% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.1 MB, less than 90.98% of Python3 online submissions for Median of Two Sorted Arrays.