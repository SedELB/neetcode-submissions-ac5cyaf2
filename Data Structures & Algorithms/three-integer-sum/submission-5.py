class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # allows for 2p to have a logic to inc. l or dec. r
        # [-4, -1, -1, 0, 1, 2] and -nums[i] = nums[j] + nums[k]

        for i in range(len(nums)):
            # To avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            l, r = i+1, len(nums) - 1

            while l < r:
                s = nums[l] + nums[r]
                # Case 1: we hit the target.
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # Skip identical nums[l]'s
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                # Case 2: the sum is smaller, we need to add bigger values, by inc. left
                if nums[l] + nums[r] < target:
                    l += 1
                
                # Case 3: the sum is higher, we need to add smaller values by dec. right
                else:
                    r -= 1

        return res





            


