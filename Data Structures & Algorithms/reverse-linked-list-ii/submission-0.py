# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        def reverse(sub_head):
            curr = sub_head
            prev = None
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev
        
        dummy = ListNode(0)
        dummy.next = head

        before_sublist = dummy
        for _ in range(left - 1):
            before_sublist = before_sublist.next
        
        leftHead = before_sublist.next
        rightHead = leftHead
        for _ in range(right - left):
            rightHead = rightHead.next

        tail = rightHead.next
        rightHead.next = None

        reverso = reverse(leftHead)

        before_sublist.next = reverso

        newCurr = reverso

        while newCurr.next:
            newCurr = newCurr.next
        
        newCurr.next = tail
        
        return dummy.next 