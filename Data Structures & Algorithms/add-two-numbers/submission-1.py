# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        res = ListNode(-1)
        ans = res
        
        carry = 0

        while curr1 or curr2 or carry:
            digit1 = curr1.val if curr1 else 0
            digit2 = curr2.val if curr2 else 0
            
            digit = (digit1 + digit2 + carry)

            newNode = ListNode(digit%10)

            carry = digit//10

            res.next = newNode

            res = res.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        return ans.next