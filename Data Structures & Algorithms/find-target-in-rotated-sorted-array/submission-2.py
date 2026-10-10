class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        """
        [3,4,5,6,1,2] target = 3
        pass 1 = [3,4,(5mid),6,1,2]

        lets search for the minimal element, which we already did,
        then the pivot will be nums[left] - 1
        then apply binary search on both sub-arrays.
        """
        while left < right:
            mid = left + ((right - left ) // 2)
            
            if nums[mid] > nums[right]:
                # search right
                left = mid + 1
            else:
                # search left
                right = mid
        
        pivot_index = left - 1 if left > 0 else len(nums) - 1

        # Figure out target is in which sub-array:
        left, right = 0, len(nums) - 1
        if target >= nums[0] and target <= nums[pivot_index]: # target is in the first sub-array
            right = pivot_index
        else:
            left = pivot_index + 1

        # one binary search on the selected subarray
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1     