class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value:index
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[nums[i]] = i 
        return

# [3,4,5,6] target = 7
# Pass 1: hashmap = {}, index = 0
# [(3), 4, 5, 6] difference = 7 - 3 = 4
# 4 isnt in hashmap so we add 3 -> hashmap = {3: 0}

# [3, (4), 5, 6] difference = 7 - 4 = 3
# 3 is in hashmap! return hashmap[3] = 0 and i = 1 -> [0,1]



