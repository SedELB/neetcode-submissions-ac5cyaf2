class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            somme = numbers[left] + numbers[right]
            if somme == target:
                return [left+1, right+1]
            
            if somme > target:
                right -= 1
                continue
            
            if somme < target:
                left += 1
                continue
            
            # [2, 3, 4, 5, 10, 20, 30, 40] target = 24
            # 2 + 40 = 42 > 24 right-- car on doit reduire
            # 2 + 30 = 32 > 24 right --
            # 2 + 20 = 22 < 24 left++
            # 3 + 20 = 23 < 24 left ++
            # 4 + 20 = 24 == 24