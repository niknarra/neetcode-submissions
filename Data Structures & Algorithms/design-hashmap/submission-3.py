class ListNode:
    def __init__(self, val, value):
        self.val = val
        self.values = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hashMap = [ListNode(0, -1) for i in range(10**4)]
    
    def hash(self, key):
        index = key % 10000

        return index

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        curr = self.hashMap[index]

        while curr.next:
            if curr.next.val == key:
                curr.next.values = value
                return
            curr = curr.next
        
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.hashMap[index]

        while curr.next:
            if curr.next.val == key:
                return curr.next.values
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.hashMap[index]

        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)