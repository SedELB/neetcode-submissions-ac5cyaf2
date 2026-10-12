# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        nodes = [] # nodes contains nodes, not values.
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        left, right = 0, len(nodes)-1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right: break
            nodes[right].next = nodes[left]
            right -= 1
            
        # The last points to None instead of itself
        nodes[right].next = None

