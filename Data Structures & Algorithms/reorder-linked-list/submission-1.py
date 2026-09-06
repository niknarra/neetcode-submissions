# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # O(n) SC & TC; not optimal
        nodes = []

        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        left = 0
        right = len(nodes) - 1

        while left < right:
            # Link left and right
            nodes[left].next = nodes[right]
            left += 1
            
            # If we reach the middle, no need to link further and cause loops, so break
            if left == right:
                break
            
            # Link right to the next element in original order
            nodes[right].next = nodes[left]
            right -= 1
        
        # Remove the link as this is the new last element
        nodes[left].next = None