class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Dictionary:
        # original node -> copied node
        #
        # We add None -> None so that when curr.next or curr.random
        # is None, copies[...] still works.
        copies = {None: None}

        curr = head

        # STEP 1:
        # Create a copy of every node.
        #
        # At this point, we are NOT connecting next or random yet.
        while curr:
            newNode = Node(curr.val)

            # Store the relationship:
            # original node -> copied node
            copies[curr] = newNode

            curr = curr.next

        # Go back to the beginning of the original list
        curr = head

        # STEP 2:
        # Connect the next and random pointers of the copied nodes.
        while curr:
            # Get the copy of the current original node
            newNode = copies[curr]

            # curr.next is an ORIGINAL node.
            # copies[curr.next] gives us its COPY.
            #
            # If curr.next is None, copies[None] gives us None.
            newNode.next = copies[curr.next]

            # Same idea for the random pointer.
            # We want the copied node's random pointer
            # to point to the COPY of curr.random.
            newNode.random = copies[curr.random]

            # Move through the original list
            curr = curr.next

        # Return the copy of the original head
        return copies[head]