class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverso(head):
            curr = head
            prev = None

            while curr:
                fwd = curr.next
                curr.next = prev
                prev = curr
                curr = fwd
            
            return prev
        
        rev = reverso(slow.next)
        slow.next = None

        curr = head

        while rev:
            fwd = curr.next
            revNext = rev.next
            
            curr.next = rev
            rev.next = fwd

            curr = fwd
            rev = revNext
