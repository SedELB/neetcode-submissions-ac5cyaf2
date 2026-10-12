# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            dummy_head = ListNode(0)
            curr = dummy_head
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    curr = curr.next
                    list1 = list1.next
                else:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next
            
            # add the rest of the remaining list
            if list1:
                curr.next = list1
                curr = curr.next
            else:
                curr.next = list2
                curr = curr.next
            
            head = dummy_head.next
            return head
        
        """
        We iterate on the i lists starting at 1 and we mergeTwoLists(lists[i], lists[i-1])
        then we replace lists[i] with the new sortedlist, iteratively.
        Update: this solution is O(n*k) but exceeds time limit bruh.
        New solution: divide and conquer on the iterations.
        """
        # edge cases
        if not lists: return None
        if len(lists) == 1: return lists[0]

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i+1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None

                merged_list = mergeTwoLists(l1, l2)
                merged_lists.append(merged_list)
            # lists = [[1, 2], [3,4], [5,6], [7,8]]
            # pass 1: lists = merged_lists = [[1,2,3,4], [5,6,7,8]]
            # len(lists) > 1 ? true so we do it again, to have [[1,2,3,4,5,6,7,8]]
            # which we return.
            lists = merged_lists
        
        return lists[0]



        

