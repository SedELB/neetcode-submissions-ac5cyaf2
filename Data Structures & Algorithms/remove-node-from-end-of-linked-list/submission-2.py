# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Nth node from the end means that
        nth node from the start is k = len(list) - n.
        """
        curr = head
        list_len = 0
        # counting the list length.
        while curr:
            list_len += 1
            curr = curr.next
        
        k = list_len - n
        # k is now the kth node from the start to remove.
        # if k == 0, it means the node to remove is the head, so we return the rest of the list.
        if k == 0:
            return head.next

        curr = head
        count = 0
        while curr:

            if count == k - 1:
                curr.next = curr.next.next
                break
            else:
                count += 1
                curr = curr.next
        
        return head

