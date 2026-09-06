class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverser(head, linkNext):
            curr = head
            prev = linkNext

            while curr != linkNext:
                fwd = curr.next
                curr.next = prev
                prev = curr
                curr = fwd
            
            return prev
        
        curr = head
        start = head
        cnt = 0

        # This will be the node before the first group.
        # We use it to connect the previous reversed group
        # to the current reversed group.
        prevGroup = None

        while curr:
            cnt += 1

            if cnt == k:
                # Save the beginning of the next group
                linkNext = curr.next

                # Reverse the current group
                newCurr = reverser(start, linkNext)

                # If this is the first group,
                # newCurr becomes the new head.
                if prevGroup is None:
                    head = newCurr
                else:
                    # Connect previous group to current group
                    prevGroup.next = newCurr

                # start is now the END of the reversed group
                prevGroup = start

                # Move to the next group
                start = linkNext
                curr = linkNext
                cnt = 0

            else:
                curr = curr.next

        return head
