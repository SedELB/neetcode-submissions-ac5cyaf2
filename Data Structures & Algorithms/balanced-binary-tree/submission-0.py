# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0
            
            L, R = dfs(root.left), dfs(root.right)
            if abs(L - R) > 1 or L == -1 or R == -1: return -1
            return 1 + max(L, R)

        return dfs(root) != -1
