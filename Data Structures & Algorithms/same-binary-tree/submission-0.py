# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        1. what does my function return ?
        starting from a root, are the children the exact same in position and value.

        2. What is the base case
        2.1 Both nodes are the same: return true
        2.2 One node is null, return False
        2.3 Both nodes are null: return true

        3. If my children give me their answer, how do I calculate mine ?
        I check if my root is the same as the other root and return true.
        """

        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        