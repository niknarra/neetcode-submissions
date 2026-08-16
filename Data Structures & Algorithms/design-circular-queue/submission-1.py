class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.curSize = 0
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        last = self.tail.prev

        last.next = node
        node.prev = last
        node.next = self.tail

        self.tail.prev = node
    
    def remove(self):
        curr = self.head.next
        curr.next.prev = self.head
        self.head.next = curr.next

    def enQueue(self, value: int) -> bool:
        if self.curSize < self.capacity:
            self.curSize += 1
            temp = ListNode(value)

            self.insert(temp)

            return True
        
        return False
        

    def deQueue(self) -> bool:
        if self.curSize > 0:
            self.remove()
            self.curSize -= 1
            return True
        
        return False

    def Front(self) -> int:
        if self.curSize > 0:
            return self.head.next.val
        return -1

    def Rear(self) -> int:
        if self.curSize > 0:
            return self.tail.prev.val
        return -1

    def isEmpty(self) -> bool:
        return self.curSize == 0

    def isFull(self) -> bool:
        return self.curSize == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()