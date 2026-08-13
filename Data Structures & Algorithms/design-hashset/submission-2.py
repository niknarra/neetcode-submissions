class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self):
        self.hashSet = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % 10000
        curr = self.hashSet[index]

        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)


    def remove(self, key: int) -> None:
        index = key % 10000
        curr = self.hashSet[index]

        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next


    def contains(self, key: int) -> bool:
        index = key % 10000
        curr = self.hashSet[index]

        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)