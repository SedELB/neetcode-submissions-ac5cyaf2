# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        (1, head) -> (2) -> (3) -> None
        we want to reverse it.
        None <- (1) <- (2) <- (3, head)
        each node has a self.val (int) and self.next (ListNode)
        """
        prev, curr = None, head
        while curr:
            nxt = curr.next # (2) status: (1, curr) -> (2) -> (3) -> None
            curr.next = prev # status: None <- (1, curr) (2) -> (3) -> None
            prev = curr # status: None <- (1,curr,prev) (2) -> (3) -> None
            curr = nxt  # status: None <- (1, prev) (2, curr) -> (3) -> None
            
        return prev
        
    
