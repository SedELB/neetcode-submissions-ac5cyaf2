class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maximum = 0

        for x in hashset: # {0, 2, 4, 5, 6, 7, -1, -8, -4, -3, -2}
            if x-1 not in hashset: # sequence starter
                currentNum = x
                currentStreak = 1

                while currentNum + 1 in hashset:
                    currentNum += 1
                    currentStreak += 1
                
                maximum = max(maximum, currentStreak)

        return maximum
                
