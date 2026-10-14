# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        level = [root]

        while level:
            vals = []
            next_level = []
            for node in level:
                if node:
                    vals.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            
            if vals:
                res.append(vals)
                
            level = next_level
        
        return res




