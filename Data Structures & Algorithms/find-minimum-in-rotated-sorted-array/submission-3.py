class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [(1), 2, 3, 4, 5]
        [2, 3, 4, 5, (1)]
        [3, 4, 5, (1), 2]
        we can view this as two separate sorted sub-arrays.
        the sub-array with the highest values will always be at the left, if theres a shift.

        """
        # case of non-rotated array:
        if nums[-1] >= nums[0]:
            return nums[0]

        # case of rotated array.
        left, right = 0, len(nums) - 1
        min_element = nums[right]

        # [4,5,6,7,0,1,2]
        while left < right:
            mid = left + ((right - left ) // 2)

            if nums[mid] > nums[right]: # the middle is greater than the end, theres a pivot.
                # search right
                left = mid + 1

            else:
                # search left
                right = mid
                
        return nums[left]