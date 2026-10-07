class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        # [0,2,0,3,1,0,1,3,2,1]
        leftMax, rightMax = height[l], height[r]
        # leftMax = 0, rightMax = 1
        # leftMax is the tallest bar on the left of height[l]
        # rightMax is the tallest bar on the right of height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res





