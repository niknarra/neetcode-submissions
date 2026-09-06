# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge(head1, head2):
            dummy = ListNode(-1)
            curr = dummy
            left = head1
            right = head2

            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                
                curr = curr.next
            
            if left:
                curr.next = left
            
            if right:
                curr.next = right
            
            return dummy.next
        
        interval = 1

        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i+interval])
            
            interval *= 2
        
        return lists[0]
        

