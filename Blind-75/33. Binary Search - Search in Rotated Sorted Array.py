class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        def binary_search(nums, l, r, target):
            if r >= l:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                
                # left side
                if nums[l] <= nums[mid]:
                    # look in right side
                    if target > nums[mid] or target < nums[l]:
                        return binary_search(nums, mid + 1, r, target)
                    else:
                        return binary_search(nums, l, mid - 1, target)
                # right side
                else:
                    if target < nums[mid] or target > nums[r]:
                        return binary_search(nums, l, mid - 1, target)
                    else:
                        return binary_search(nums, mid + 1, r, target)
            else:
                return -1

        return binary_search(nums, l, r, target) 

    # iterative
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            # Essentially you're continuously looking for where the split is
            # left side is sorted 
            if nums[l] <= nums[mid]:
                # look in right side
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right side
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

def binarySearch(arr, l, r, x):
  
    # Check base case
    if r >= l:
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
  
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
  
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
  
    else:
        # Element is not present in the array
        return -1