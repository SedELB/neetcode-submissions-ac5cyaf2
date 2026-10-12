# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # phase 1: detect if a cycle exists:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast: return False

            # if slow and fast meet, there is a cycle
            if slow == fast:
                return True
        
        return False
                
