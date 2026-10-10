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
        
        pivot_index = left - 1

        # two binary searches, one on each sub-array:
        l1, r1 = 0, pivot_index
        l2, r2 = pivot_index + 1, len(nums) - 1
        while l1 <= r1:
            m1 = l1 + ((r1 - l1) // 2)
            if nums[m1] == target:
                return m1
            
            if nums[m1] > target:
                r1 = m1 - 1
            else:
                l1 = m1 + 1
        
        while l2 <= r2:
            m2 = l2 + ((r2 - l2) // 2)
            if nums[m2] == target:
                return m2
            
            if nums[m2] > target:
                r2 = m2 - 1
            else:
                l2 = m2 + 1

        return -1     