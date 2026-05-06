class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum = 0

        while left < right:
            volume = (right-left) * min(heights[left], heights[right])
            if volume > maximum:
                maximum = volume
            
            if heights[left] < heights[right]:
                left += 1
                continue

            if heights[left] >= heights[right]:
                right -= 1
                continue
        
        return maximum
        


