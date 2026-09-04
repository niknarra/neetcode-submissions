# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        def getGCD(a, b):
            res = 1
            for i in range(2, max(a,b)):
                if a % i == 0 and b % i == 0:
                    res = max(res, i)
            
            return res

        while curr.next:
            # Store the next value of the main list
            forward = curr.next

            # Get the GCD for the current two values
            gcd = getGCD(curr.val, curr.next.val)

            # Create a new Node with the GCD value and add it to the list
            curr.next = ListNode(gcd)
            curr.next.next = forward
            
            # Move curr forward and skip the newly added GCD node
            curr = forward

        return head